import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from views.PruebaTabla import Ui_TodosPedidos
import pandas as pd
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
#from Services.EnRutarServices import EnRutar
from Services.EnRutamientoServices import EnRutar

class PlanificacionServices(QWidget, Ui_TodosPedidos):
    def __init__(self, ruta_status, ruta_play, ruta_inventario, parent=None):
        super().__init__(parent)
        self.ruta_status = ruta_status
        self.ruta_play = ruta_play
        self.ruta_inventario = ruta_inventario
        self.setupUi(self)
        self.tablaOriginal={}
        self.tablaCopia={}
        self.tablaPlanificado={}
        self.AgregarCargamento.clicked.connect(self.agregar_un_pedido)
        self.comboBox.currentIndexChanged.connect(self.DesbloquearComboBox)
        self.plainTextEdit.textChanged.connect(self.Filtrar)
        self.BotonPorcentaje.clicked.connect(self.ver_tabla_porcentaje)
        self.SacarCargamento.clicked.connect(self.descartar_un_pedido)
        self.TablaPorcentaje.setVisible(False)
        self.Enrutar.clicked.connect(self.siguiente_paso)  
        self.bandera=True;
        self.CargarExcels()
        self.Agregar_Columnas_a_planificacion()
        self.planificado_counts = {}
        self.Skus_Parciales=  set()
        self.botontodo.clicked.connect(self.agregar_todo_los_pedidos)
        self.df_maestroProductos = self.load_excel(".\excels\maestro Productos.xlsx") 

        
    def DesbloquearComboBox(self):
        if self.comboBox.currentIndex() > 0:  
            self.plainTextEdit.setEnabled(True)
        else:
            self.plainTextEdit.setText("")
            self.plainTextEdit.setEnabled(False)
            
    def Filtrar(self):
        filter_text = self.plainTextEdit.text().lower() 
        column_name = self.comboBox.currentText()
        column_names = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
        if column_name in column_names:
            column_index = column_names.index(column_name)
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, column_index)
                if item and filter_text in item.text().lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)
        else:
            QMessageBox.warning(self, "Advertencia", "La columna seleccionada no existe.")

        
    def load_excel(self, path, **kwargs):
        return pd.read_excel(path, **kwargs)
  
  
    def CargarExcels(self):
        try:
            df_status = self.load_excel(self.ruta_status, parse_dates=['Fecha cancel', 'Fecha factura'])
            df_play = self.load_excel(self.ruta_play)
            df_inventory = self.load_excel(self.ruta_inventario)
            df_maestroProductos = self.load_excel(".\excels\maestro Productos.xlsx") 
            df_status['Status'] = df_status.apply(self.determinar_status, axis=1)
            df_merged = self.mezclar_tablas(df_play, df_status, df_inventory)
            df_final = self.ProcesoFinal(df_merged, df_maestroProductos,df_inventory)   
            self.tablaOriginal = df_final
            self.tablaCopia= df_final
            self.MostrarTablaPedidos(self.tablaOriginal)
            
        except Exception as e:
            print(f"Error: {str(e)}")
            QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo:\n{str(e)}")         
            
    def mezclar_tablas(self, df_play, df_status, df_inventory):
        df_merged = df_play.merge(df_status, left_on='Numero de Pedido', right_on='Número orden', how='left')
        return df_merged.merge(df_inventory, left_on='Codigo SKU', right_on='Número artículo', how='left')
    
    def determinar_status(self, row):
        if pd.isna(row['Último estado']):
            return 'SIN ESTADO'
        try:
            estado = int(row['Último estado'])
        except ValueError:
            return 'ESTADO INVÁLIDO'  

        status_mapping = {
            617: 'FACTURADO',
            620: 'FACTURADO',
            None: 'CANCELADO' if pd.notna(row['Fecha cancel']) else 'RETENIDO',
            520: 'POR DESPACHAR',
            521: 'POR DESPACHAR',
            527: 'POR DESPACHAR',
            598: 'DESPACHO PARCIAL',
            914: 'DESPACHADO',
            560: 'PROCESADO',
            980: 'CANCELADO',
            995: 'NO APROBADO'
        }
        
        return status_mapping.get(estado, 'ESTADO DESCONOCIDO')

    def CalcularTotalPaletas(self, row, df_maestroProductos):
        if row['Codigo SKU'] == 20532:
            return 'paletas'
        
        # Convertir Codigo SKU a texto
        codigo_sku_texto = str(row['Codigo SKU'])
        
        # Buscar el valor en df_maestroProductos
        sku_value = df_maestroProductos.loc[df_maestroProductos['Cod'].astype(str) == codigo_sku_texto, 'PALETIZADO'].values
        
        if sku_value.size > 0:
            return round(row['Cant. Programada'] / float(sku_value), 2)
        else:
            return 'Granel'


    def calculate_inv_vs_pedido(self, row, df_inventory):
        inventory_rows = df_inventory[df_inventory['Número artículo'] == row['Codigo SKU']]
        if not inventory_rows.empty:
            total_existencias = inventory_rows['Cantidad existencias'].sum()
            inv_remanente = total_existencias - row['Cant. Programada']

            return pd.Series([total_existencias, inv_remanente, 'Disponible' if inv_remanente >= 0 else 'No disponible'])
        return pd.Series([0, -row['Cant. Programada'], 'No disponible'])
    def ProcesoFinal(self, df_merged, df_maestroProductos, df_inventory):
        df_merged['Total paletas'] = df_merged.apply(lambda row: self.CalcularTotalPaletas(row, df_maestroProductos), axis=1)
        df_merged[['Inv Existente', 'Inv vs Pedido', 'Disponibilidad Inv']] = df_merged.apply(lambda row: self.calculate_inv_vs_pedido(row, df_inventory), axis=1)
        
        df_final = df_merged[['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 'Codigo Cliente', 
                            'Codigo SKU', 'Descripcion SKU', 'Zona de Entrega', 'Cant. Programada', 
                            'TM Programadas', 'Total paletas', 'Status', 'Inv Existente', 'Inv vs Pedido']]
        
        df_final['Inv Remanente'] = ''
        df_final['Disponibilidad Inv'] = df_merged['Disponibilidad Inv']
        
        df_final = df_final.drop_duplicates(subset=['Numero de Pedido', 'Codigo SKU'])
        df_final['Fecha de la Cita'] = pd.to_datetime(df_final['Fecha de la Cita'], format='%d-%m-%Y')
        
        # Ordenar por fecha
        df_final = df_final.sort_values(by='Fecha de la Cita')
        
        df_final['Fecha de la Cita'] = df_final['Fecha de la Cita'].dt.strftime('%d-%m-%Y')
        
        return df_final

    def MostrarTablaPedidos(self, tablaOriginal):
        self.tableWidget.setRowCount(len(tablaOriginal))
        self.tableWidget.setColumnCount(len(tablaOriginal.columns))
        self.tableWidget.setHorizontalHeaderLabels(tablaOriginal.columns)

        for i, (index, row) in enumerate(tablaOriginal.iterrows()):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                
                if j == tablaOriginal.columns.get_loc('Disponibilidad Inv'):
                    if row['Disponibilidad Inv'] == 'Disponible':
                        item.setBackground(QColor(144, 238, 144)) 
                    elif row['Disponibilidad Inv'] == 'No disponible':
                        item.setBackground(QColor(255, 160, 122)) 
                else:
                    item.setBackground(QColor(255, 255, 255))  
                    
                self.tableWidget.setItem(i, j, item)


    def actualizar_colores(self, table):
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                item.setBackground(QColor(255, 255, 255))  
                if item and table.horizontalHeaderItem(column).text() == 'Disponibilidad Inv':
                    
                    if item.text()== 'Parcial':
                        item.setBackground(QColor(255, 128, 0)) 
                    
                    elif item.text() == 'Disponible':
                        item.setBackground(QColor(144, 238, 144)) 
        
                    else:
                        item.setBackground(QColor(255, 160, 122)) 

    def agregar_un_pedido(self):
        selected_row = self.tableWidget.currentRow()    
        remante=0  
        if selected_row < 0:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un pedido para sacar.")
            return

        row_data = []
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(selected_row, column)
            row_text = item.text() if item else ""
            row_data.append(row_text)

        try:
            sku = self.tableWidget.item(selected_row, 4).text()
            numero_pedido = self.tableWidget.item(selected_row, 2).text()

            self.pedidos_planificados[(numero_pedido, sku)] = sku 
          
        except AttributeError:
            print(f"No se pudo obtener SKU en la fila {selected_row}")

        try:
            numero_pedido = self.tableWidget.item(selected_row, 2).text()
            print(f"Número de pedido: {numero_pedido}") 
        except AttributeError:
            print(f"No se pudo obtener número de pedido en la fila {selected_row}")
            
        if(not row_data[13]):
            remante=float(row_data[11])
        else:
            remante=float(row_data[13])        
        if  not self.InvRemanante_Es_Zero(selected_row, 13):  
            if row_data[12] is None or row_data[12] == '':
                print()

            elif((remante-float(row_data[7])) < 0): 
                respuesta=self.mostrar_alerta()
                print((remante-float(row_data[7])))
                if(respuesta == QMessageBox.Yes):
                    row_position = self.TablaPlanificado.rowCount()
                    self.TablaPlanificado.insertRow(row_position) 
                    
                    
                    #Datos orignales
                    inventario= float(row_data[11])
                    cantidad_programada = float(row_data[7])
                    peso_tm= float(row_data[8])    
                    for column, value in enumerate(row_data):
                        if(column == 14):
                            self.TablaPlanificado.setItem(row_position, column, QTableWidgetItem("Parcial"))

                        self.TablaPlanificado.setItem(row_position, column, QTableWidgetItem(value))

                    nueva_cantidad_programada = (float(row_data[7])) - remante
                    nuevo_tm_total = (float(row_data[8]) / float(row_data[7])) * nueva_cantidad_programada
                    nueva_paleta=self.PaletaPorSku(sku,nueva_cantidad_programada)
                    self.tableWidget.setItem(selected_row, 14, QTableWidgetItem("Parcial"))
                    self.tableWidget.setItem(selected_row, 7, QTableWidgetItem(str(nueva_cantidad_programada)))
                    self.tableWidget.setItem(selected_row, 8, QTableWidgetItem(str(nuevo_tm_total)))
                    self.tableWidget.setItem(selected_row, 9, QTableWidgetItem(str(nueva_paleta))) 
                    self.actualizar_colores(self.tableWidget)
                    
                    row_data1 = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(selected_row, column)
                        row_text = item.text() if item else ""
                        row_data1.append(row_text)
                        
                    for column, value in enumerate(row_data1):
                        if(column == 14):
                            self.TablaPlanificado.setItem(row_position, column, QTableWidgetItem("Parcial"))

                        self.TablaPlanificado.setItem(row_position, column, QTableWidgetItem(value))
                        self.TablaPlanificado.setItem(row_position, 7, QTableWidgetItem(str(remante)))
                        self.TablaPlanificado.setItem(row_position, 8, QTableWidgetItem(str((inventario *peso_tm)/cantidad_programada)))
                        self.TablaPlanificado.setItem(row_position, 9, QTableWidgetItem(str(self.PaletaPorSku(sku,inventario)))) 
                        self.TablaPlanificado.setItem(row_position, 12, QTableWidgetItem(str(0)))
                    
                    self.actualizar_colores(self.TablaPlanificado)
                    self.actulizar_peso()
                    self.actulizar_tabla_porcenteja()
                    self.Skus_Parciales.add(sku)
                    self.planificado_counts[sku] = self.planificado_counts.get(sku, 0) + inventario
                    
                    self.update_inv_remanente(sku)
                else: 
                    pass
                
            else: 

                row_position = self.TablaPlanificado.rowCount()
                self.TablaPlanificado.insertRow(row_position)
                for column, value in enumerate(row_data):
                    self.TablaPlanificado.setItem(row_position, column, QTableWidgetItem(value))
                
                cantidad_programada = float(row_data[7])  
                self.planificado_counts[sku] = self.planificado_counts.get(sku, 0) + cantidad_programada
                
                self.tableWidget.removeRow(selected_row)
                self.actualizar_colores(self.TablaPlanificado)
                self.actulizar_peso()
                self.actulizar_tabla_porcenteja()
                self.update_inv_remanente(sku)
         
        else:
            self.mensaje_deface()

    def descartar_un_pedido(self):
        selected_row = self.TablaPlanificado.currentRow()    
        if selected_row < 0:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para sacar.")
            return
        item_sku = self.TablaPlanificado.item(selected_row, 4)
        if item_sku is None:
            return
        sku = item_sku.text()
        
        item_estado = self.TablaPlanificado.item(selected_row, 14)
        if item_estado is None:
            return
        estado = item_estado.text()
        
        bandera= None

        if estado == 'Parcial':
            numero_pedido = self.TablaPlanificado.item(selected_row, 2).text()
            for row in range(self.tableWidget.rowCount()):
                if (self.tableWidget.item(row, 2).text() == numero_pedido and 
                    self.tableWidget.item(row, 4).text() == sku):
                    inventario1= float(self.tableWidget.item(row, 7).text())
                    cantidad_programada1 = float(self.tableWidget.item(row, 8).text())
                    peso_paletas1= float(self.tableWidget.item(row, 9).text())    
                    inventario2= float(self.TablaPlanificado.item(selected_row, 7).text())
                    cantidad_programada2 = float(self.TablaPlanificado.item(selected_row, 8).text())
                    peso_paletas2= float(self.TablaPlanificado.item(selected_row, 9).text())      
                    self.tableWidget.setItem(row, 7, QTableWidgetItem(str(inventario1+inventario2)))
                    self.tableWidget.setItem(row, 8, QTableWidgetItem(str((cantidad_programada1+cantidad_programada2))))
                    self.tableWidget.setItem(row, 9, QTableWidgetItem(str(peso_paletas1+peso_paletas2))) 
                    self.tableWidget.setItem(row, 13, QTableWidgetItem(str(""))) 
                    self.tableWidget.setItem(row, 14, QTableWidgetItem(str("No Disponible"))) 

                    bandera=row
                    self.Skus_Parciales.remove(sku)
        cantidad_programada = float(self.TablaPlanificado.item(selected_row, 7).text())
        if sku in self.planificado_counts:
            self.planificado_counts[sku] -= cantidad_programada
            print("self.planificado_counts[sku]")
            print(self.planificado_counts[sku])
            if self.planificado_counts[sku] <= 0:
                del self.planificado_counts[sku]
        item_cantidad_programada = self.TablaPlanificado.item(selected_row, 7)
        if item_cantidad_programada is None:
            return
        cantidad_programada = float(item_cantidad_programada.text())
        row_data = []
        for column in range(self.TablaPlanificado.columnCount()):
            item = self.TablaPlanificado.item(selected_row, column)
            row_data.append(item.text() if item else "")
        row_position = self.tableWidget.rowCount()
        if estado == 'Parcial':
             self.tableWidget.setItem(bandera, 14, QTableWidgetItem(str("No Disponible"))) 
        else:
            self.tableWidget.insertRow(row_position)
        
        
        for column, value in enumerate(row_data):
            self.tableWidget.setItem(row_position, column, QTableWidgetItem(value))
            
        self.TablaPlanificado.removeRow(selected_row)  
        cantidad_programada = float(row_data[7])  
        self.planificado_counts[sku] = self.planificado_counts.get(sku, 0)
        self.update_inv_remanente(sku)
        self.actulizar_peso()
        self.actulizar_tabla_porcenteja()
        self.actualizar_colores(self.tableWidget)
        if(self.comboBox.currentIndex() > 0): 
                self.Filtrar()
                
    def agregar_todo_los_pedidos(self):
        if self.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "Advertencia", "No hay pedidos para bajar.")
            return

        reply = QMessageBox.question(self, "Confirmación", "¿Realmente quieres bajar todos los pedidos visibles?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return

        filas_a_bajar = []

        for row in range(self.tableWidget.rowCount()):
            if not self.tableWidget.isRowHidden(row):  # Solo agregar filas visibles
                filas_a_bajar.append(row)

        for row in reversed(filas_a_bajar):
            self.tableWidget.selectRow(row)
            self.agregar_un_pedido()

        total_bajados = len(filas_a_bajar)
        QMessageBox.information(self, "Información", f"Se han bajado {total_bajados} pedidos a la tabla de planificados.")
            
           
    def actulizar_peso(self):
        total_tm = 0
        for row in range(self.TablaPlanificado.rowCount()):
            tm_item = self.TablaPlanificado.item(row, 8)
            if tm_item and tm_item.text():
                try:
                    total_tm += float(tm_item.text())
                except ValueError:
                    pass  

        self.label_2.setText(f"Peso Total: {round(total_tm, 3)} TM")
        
        
        total_paletas = 0
        for row in range(self.TablaPlanificado.rowCount()):
            paleta_item = self.TablaPlanificado.item(row, 9)
            if  paleta_item and  paleta_item.text():
                try:
                     total_paletas += float(paleta_item.text())
                except ValueError:
                    pass  

        self.LabelPaletas.setText(f"Paletas Totales: {round(total_paletas, 3)}")

    def update_inv_remanente(self, sku):
        total_programado = self.planificado_counts.get(sku, 0)
        print("Total Programado ")
        print(total_programado)
        #TablaPedidos
        
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 4).text() == sku:
                disponibilidad = self.tableWidget.item(row, 14).text()
                cantidad_programada = float(self.tableWidget.item(row, 7).text())
                
                if disponibilidad == 'Parcial':
                    self.tableWidget.setItem(row, 13, QTableWidgetItem(str(0)))
                    self.Skus_Parciales.add(sku)
                elif(sku in self.Skus_Parciales): 
                    disponibilidad = 'No disponible'
                    self.tableWidget.setItem(row, 13, QTableWidgetItem(str(0)))
                    self.tableWidget.setItem(row, 14, QTableWidgetItem(str(0)))
                else:
                    inv_existente = float(self.tableWidget.item(row, 11).text())
                    inv_remanente = inv_existente -total_programado
                    #print(inv_remanente)
                    self.tableWidget.setItem(row, 13, QTableWidgetItem(str(inv_remanente)))
                    if inv_remanente <= 0:
                        disponibilidad = 'No disponible'
                    else:
                        disponibilidad = 'Disponible'

                self.tableWidget.setItem(row, 14, QTableWidgetItem(disponibilidad))
                self.actualizar_colores(self.tableWidget)

        #TablaPlanificado

        for row in range(self.TablaPlanificado.rowCount()):
            if self.TablaPlanificado.item(row, 4).text() == sku:
                disponibilidad = self.TablaPlanificado.item(row, 14).text()

                if disponibilidad == 'Parcial':
                    self.TablaPlanificado.setItem(row, 13, QTableWidgetItem(str(0)))
                    self.TablaPlanificado.setItem(row, 11, QTableWidgetItem(str(0)))
                elif(sku in self.Skus_Parciales): 
                    disponibilidad = 'No disponible'
                    self.TablaPlanificado.setItem(row, 13, QTableWidgetItem(str(0)))
                    self.TablaPlanificado.setItem(row, 11, QTableWidgetItem(str(0)))
                else:
                    inv_existente = float(self.TablaPlanificado.item(row, 11).text())
                    inv_remanente = inv_existente-total_programado 
                    self.TablaPlanificado.setItem(row, 13, QTableWidgetItem(str(inv_remanente)))

                    if inv_remanente <= 0:
                        disponibilidad = 'No disponible'
                    else:
                        disponibilidad = 'Disponible'

                self.TablaPlanificado.setItem(row, 14, QTableWidgetItem(disponibilidad))
                self.actualizar_colores(self.TablaPlanificado)
    
    def ver_tabla_porcentaje (self):
        if self.bandera: 
               self.TablaPlanificado.setVisible(False)
               self.TablaPorcentaje.setVisible(True)
               self.bandera = False
        else: 
                self.TablaPlanificado.setVisible(True)
                self.TablaPorcentaje.setVisible(False)
                self.bandera = True
          
    def siguiente_paso(self):
        planificados_data = []
        
        # Definir las columnas que deseas pasar
        columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 
                            'Codigo Cliente', 'Codigo SKU', 'Descripcion SKU', 
                            'Zona de Entrega', 'Cant. Programada', 'TM Programadas', 
                            'Total paletas']

        for row in range(self.TablaPlanificado.rowCount()):
            row_data = []
            for column_name in columnas_deseadas:
                # Encuentra el índice de la columna basada en el nombre
                column_index = -1
                for i in range(self.TablaPlanificado.columnCount()):
                    if self.TablaPlanificado.horizontalHeaderItem(i).text() == column_name:
                        column_index = i
                        break
                
                if column_index != -1:  # Verifica si se encontró la columna
                    item = self.TablaPlanificado.item(row, column_index)
                    row_data.append(item.text() if item else "")
            
            planificados_data.append(row_data)

        # Pasar los datos a la ventana EnRutar
        self.cargar_archivo_window = EnRutar(planificados_data)
        #self.cargar_archivo_window = EnRutar(planificados_data)
        self.cargar_archivo_window.show()
        self.close()
     
    def Agregar_Columnas_a_planificacion(self):

        if not self.tablaOriginal.empty:
           
            self.tableWidget.setColumnCount(len(self.tablaOriginal.columns))
            self.tableWidget.setHorizontalHeaderLabels(list(self.tablaOriginal.columns)) 
            self.TablaPlanificado.setColumnCount(len(self.tablaOriginal.columns))
            self.TablaPlanificado.setHorizontalHeaderLabels(list(self.tablaOriginal.columns))  
        else:
            print("Error: TablaOriginal está vacía o no se ha definido correctamente.")
            
            
    def InvRemanante_Es_Zero(self, row, column): 
        item = self.tableWidget.item(row, column)
        # Verificamos si el item es None antes de acceder a su texto
        if item is None:
            return False  # O puedes retornar un valor diferente según lo que quieras hacer en este caso
        texto = item.text()
        # Si el texto está vacío, puedes considerar ese caso también
        if texto == "":
            return False  # O lo que sea apropiado en caso de que no haya texto
        try:
            valor = float(texto)
        except ValueError:
            # Si no se puede convertir el texto a float, retorna False o lo que sea apropiado
            return False
        
        refencia = 0.0
        return valor < 0 or valor == refencia

    
    def actulizar_tabla_porcenteja(self):
    
                sku_data = {}
                total_tm = 0
                
                for row in range(self.TablaPlanificado.rowCount()):
                    sku = self.TablaPlanificado.item(row, 4).text()
                    cantidad = float(self.TablaPlanificado.item(row, 7).text())
                    tm = float(self.TablaPlanificado.item(row, 8).text())
                    
                    if sku not in sku_data:
                        sku_data[sku] = {
                            'descripcion': self.TablaPlanificado.item(row, 5).text(),
                            'cantidad': 0,
                            'tm': 0
                        }
                        
                    sku_data[sku]['cantidad'] += cantidad
                    sku_data[sku]['tm'] += tm
                    total_tm += tm
                
               
                self.TablaPorcentaje.setRowCount(0) 
                
                for sku, data in sku_data.items():
                    porcentaje = (data['tm'] / total_tm * 100) if total_tm > 0 else 0
                    
                    row_position = self.TablaPorcentaje.rowCount()
                    self.TablaPorcentaje.insertRow(row_position)
                    self.TablaPorcentaje.setItem(row_position, 0, QTableWidgetItem(sku))
                    self.TablaPorcentaje.setItem(row_position, 1, QTableWidgetItem(data['descripcion']))
                    self.TablaPorcentaje.setItem(row_position, 2, QTableWidgetItem(str(data['cantidad'])))
                    self.TablaPorcentaje.setItem(row_position, 3, QTableWidgetItem(str(data['tm'])))
                    self.TablaPorcentaje.setItem(row_position, 4, QTableWidgetItem(f"{porcentaje:.2f}%"))
                    for column in range(5): 
                        item = self.TablaPorcentaje.item(row_position, column)
                        item.setBackground(QColor(255, 255, 255))  

       
    def mostrar_alerta(self): 
        alerta = QMessageBox() 
        alerta.setText("No Existe Cantidad Suficiente En Inventario Para Despachar. \n Desea enviarlo de forma Parcial ? ") 
        alerta.setStandardButtons(QMessageBox.Yes | QMessageBox.No) 
        respuesta= alerta.exec()
        return respuesta

    def mensaje_deface(self):
        alerta = QMessageBox() 
        alerta.setText("No puedes Agregar Este Pedido, No Tienes Inventario Suficiente") 
        alerta.setStandardButtons(QMessageBox.Ok)
        respuesta= alerta.exec()
        return respuesta
   
    def PaletaPorSku(self,sku,cantidad):
        if sku == "20532":
            return 'paletas'
        sku_value = self.df_maestroProductos.loc[self.df_maestroProductos['Cod'] == sku, 'PALETIZADO'].values
        if sku_value.size > 0:
            return round(cantidad/ float(sku_value), 2)
        else:
            return 'Granel'
        
        """
        7 cantidad programada
        8 TM programadas
        9 total paletas
        10 status
        11 inv existente
        12 inv vs pedido
        13 inv remannte    
        """
        
        
""" 
0 Nombre Cliente 
1 Fecha de la Cita 
2 Numero de Pedido 
3 Codigo Cliente 
4 Codigo SKU 
5 Descripcion SKU
6 Zona de Entrega
7 Cant. Programada 
8 TM Programadas
9 Total paletas 
10 Status 
11 Inv Existente 
12 Inv vs Pedido
13 Inv Remanente
14 Disponibilidad Inv

11 - 12 - 13 < 0 
"""