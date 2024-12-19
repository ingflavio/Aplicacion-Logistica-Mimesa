import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from views.PruebaTabla import Ui_TodosPedidos
import pandas as pd
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from Services.EnRutarServices import EnRutar
import matplotlib.pyplot as plt
from geopy.distance import geodesic

class PruebaTablaWindos(QWidget, Ui_TodosPedidos):
    def __init__(self, ruta_status, ruta_play, ruta_inventario, parent=None):
        super().__init__(parent)
        self.ruta_status = ruta_status
        self.ruta_play = ruta_play
        self.ruta_inventario = ruta_inventario
        self.setupUi(self)
        self.load_data()
        self.setup_tables_columns()
        self.TablaPorcentaje.setVisible(False)
        self.comboBox.currentIndexChanged.connect(self.handle_combobox_change)
        self.plainTextEdit.textChanged.connect(self.apply_filter)
        self.AgregarCargamento.clicked.connect(self.agregar_cargamento)
        self.SacarCargamento.clicked.connect(self.sacar_cargamento)
        self.BotonPorcentaje.clicked.connect(self.verTablaPorcentaje)
        self.planificado_counts = {}
        self.bandera=True;
        self.botontodo.clicked.connect(self.BajarTodo)
        self.pedidos_planificados = {}
        self.Enrutar.clicked.connect(self.VentanaEnrutar)

    def handle_combobox_change(self):
        if self.comboBox.currentIndex() > 0:  
            self.plainTextEdit.setEnabled(True)
        else:
            self.plainTextEdit.setText("")
            self.plainTextEdit.setEnabled(False)
            
    def apply_filter(self):
        filter_text = self.plainTextEdit.text().lower() 
        column_name = self.comboBox.currentText()
        
        if column_name in self.df_original.columns:
            column_data = self.df_original[column_name].fillna('').astype(str)
            filtered_df = self.df_original[column_data.str.lower().str.contains(filter_text)]
            self.show_data_in_table(filtered_df)
        else:
            QMessageBox.warning(self, "Advertencia", "La columna seleccionada no existe.")


    def load_data(self):
        try:
            df_status = pd.read_excel(self.ruta_status, parse_dates=['Fecha cancel', 'Fecha factura'])
            df_play = pd.read_excel(self.ruta_play)
            df_inventory = pd.read_excel(self.ruta_inventario)
            df_maestroProductos = pd.read_excel(".\excels\maestro Productos.xlsx")
        
            def determine_status(row):
                if pd.isna(row['Último estado']):
                    return 'SIN ESTADO'
                try:
                    estado = int(row['Último estado'])
                except ValueError:
                    return 'ESTADO INVÁLIDO'  

                if estado in [617, 620]:
                    return 'FACTURADO'
                elif pd.notna(row['Fecha cancel']):
                    return 'CANCELADO'
                elif len(str(row['Cd ret'])) > 1 or len(str(row['Hd Cd2'])) > 1:
                    return 'RETENIDO'
                elif estado in [520, 521, 527]:
                    return 'POR DESPACHAR'
                elif estado == 598:
                    return 'DESPACHO PARCIAL'
                elif estado == 914:
                    return 'DESPACHADO'
                elif estado == 560:
                    return 'PROCESADO'
                elif estado == 980:
                    return 'CANCELADO'
                elif estado == 995:
                    return 'NO APROBADO'
                else:
                    return 'ESTADO DESCONOCIDO'

            df_status['Status'] = df_status.apply(determine_status, axis=1)
            df_merged = df_play.merge(df_status, left_on='Numero de Pedido', right_on='Número orden', how='left')
            df_merged = df_merged.merge(df_inventory, left_on='Codigo SKU', right_on='Número artículo', how='left')

            def calculate_total_paletas(row):
                if row['Codigo SKU'] == 20532:
                    return 'paletas'
                else:
                    sku_value = df_maestroProductos.loc[df_maestroProductos['Cod'] == row['Codigo SKU'], 'PALETIZADO'].values
                    if len(sku_value) > 0:
                        total_paletas = row['Cant. Programada'] / float(sku_value) 
                        return round(total_paletas, 2)  

            df_merged['Total paletas'] = df_merged.apply(calculate_total_paletas, axis=1)

            def calculate_inv_vs_pedido(row):
                inventory_rows = df_inventory[df_inventory['Número artículo'] == row['Codigo SKU']]
                if not inventory_rows.empty:
                    total_existencias = inventory_rows['Cantidad existencias'].sum()
                    inv_remanente =total_existencias - row['Cant. Programada']
                    return pd.Series([total_existencias, inv_remanente, 'Disponible' if inv_remanente >= 0 else 'No disponible'])
                return pd.Series([0, row['Cant. Programada'], 'No disponible'])


            df_merged[['Inv Existente', 'Inv vs Pedido', 'Disponibilidad Inv']] = df_merged.apply(calculate_inv_vs_pedido, axis=1)

            df_merged['Inv Remanente'] = ''

            df_final = df_merged[['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 'Codigo Cliente', 
                      'Codigo SKU', 'Descripcion SKU', 'Zona de Entrega', 'Cant. Programada', 
                      'TM Programadas', 'Total paletas', 'Status', 'Inv Existente', 'Inv vs Pedido',
                       'Inv Remanente', 'Disponibilidad Inv']]


            df_final = df_final.drop_duplicates(subset=['Numero de Pedido', 'Codigo SKU'])
            df_final['Fecha de la Cita'] = df_final['Fecha de la Cita'].dt.strftime('%d-%m-%Y') 
            self.show_data_in_table(df_final)
            self.df_original = df_final

        except Exception as e:
            print(f"Error: {str(e)}")
            QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo:\n{str(e)}")

    def show_data_in_table(self, df):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setHorizontalHeaderLabels(df.columns.tolist())
        
        for row in df.itertuples(index=False):
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, column, item)
                item.setBackground(QColor(255, 255, 255)) 
                if df.columns[column] == 'Disponibilidad Inv':
                    if value == 'Disponible':
                        item.setBackground(QColor(0, 255, 0))  
                    else:
                        item.setBackground(QColor(255, 0, 0))  

    def actualizar_colores(self, table):
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                item.setBackground(QColor(255, 255, 255))  
                if item and table.horizontalHeaderItem(column).text() == 'Disponibilidad Inv':
                    if item.text() == 'Disponible':
                        item.setBackground(QColor(0, 255, 0)) 
                    else:
                        item.setBackground(QColor(255, 0, 0)) 

    def setup_tables_columns(self):
        self.tableWidget.setColumnCount(len(self.df_original.columns))
        self.tableWidget.setHorizontalHeaderLabels(self.df_original.columns.tolist())
        self.TablaPlanificado.setColumnCount(len(self.df_original.columns))
        self.TablaPlanificado.setHorizontalHeaderLabels(self.df_original.columns.tolist())
        
        
    def agregar_cargamento(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para agregar.")
            return

        sku = self.tableWidget.item(selected_row, 4).text()
        numero_pedido = self.tableWidget.item(selected_row, 2).text()

        # Agregar el pedido a la lista de planificados
        self.pedidos_planificados[(numero_pedido, sku)] = sku  

        row_data = []
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(selected_row, column)
            row_data.append(item.text() if item else "")

        row_position = self.TablaPlanificado.rowCount()
        self.TablaPlanificado.insertRow(row_position)
        for column, value in enumerate(row_data):
            self.TablaPlanificado.setItem(row_position, column, QTableWidgetItem(value))

        self.tableWidget.removeRow(selected_row)
        self.actualizar_peso_total()

        cantidad_programada = float(row_data[7])  
        self.planificado_counts[sku] = self.planificado_counts.get(sku, 0) + cantidad_programada
        self.update_inv_remanente(sku)
        self.actualizarTablaPorcentaje()



    def sacar_cargamento(self):
        selected_row = self.TablaPlanificado.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para sacar.")
            return

        sku = self.TablaPlanificado.item(selected_row, 4).text()
        cantidad_programada = float(self.TablaPlanificado.item(selected_row, 7).text())

        if sku in self.planificado_counts:
            self.planificado_counts[sku] -= cantidad_programada
            if self.planificado_counts[sku] <= 0:
                del self.planificado_counts[sku]

        row_data = []
        for column in range(self.TablaPlanificado.columnCount()):
            item = self.TablaPlanificado.item(selected_row, column)
            if item:
                row_data.append(item.text())
            else:
                row_data.append("")

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        for column, value in enumerate(row_data):
            self.tableWidget.setItem(row_position, column, QTableWidgetItem(value))

        self.TablaPlanificado.removeRow(selected_row)
        self.actualizar_peso_total()
        self.update_inv_remanente(sku)
        self.actualizarTablaPorcentaje()


    def update_inv_remanente(self, sku):
        total_programado = self.planificado_counts.get(sku, 0)
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 4).text() == sku:
                inv_existente = float(self.tableWidget.item(row, 11).text())
                inv_remanente = inv_existente - total_programado
                self.tableWidget.setItem(row, 13, QTableWidgetItem(str(inv_remanente)))
                
                if inv_remanente < 0:
                    disponibilidad = 'No disponible'
                else:
                    disponibilidad = 'Disponible'
                self.tableWidget.setItem(row, 14, QTableWidgetItem(disponibilidad))
                self.actualizar_colores(self.tableWidget)

        for row in range(self.TablaPlanificado.rowCount()):
            if self.TablaPlanificado.item(row, 4).text() == sku:
                inv_existente = float(self.TablaPlanificado.item(row, 11).text())
                inv_remanente = inv_existente - total_programado
                self.TablaPlanificado.setItem(row, 13, QTableWidgetItem(str(inv_remanente)))

                if inv_remanente < 0:
                    disponibilidad = 'No disponible'
                else:
                    disponibilidad = 'Disponible'
                self.TablaPlanificado.setItem(row, 14, QTableWidgetItem(disponibilidad))
                self.actualizar_colores(self.TablaPlanificado)
    

    def actualizar_peso_total(self):
        total_tm = 0
        for row in range(self.TablaPlanificado.rowCount()):
            tm_item = self.TablaPlanificado.item(row, 8)
            if tm_item and tm_item.text():
                try:
                    total_tm += float(tm_item.text())
                except ValueError:
                    pass  

        self.label_2.setText(f"Peso Total: {round(total_tm, 3)} TM")
        
    def verTablaPorcentaje(self):
           if self.bandera: 
               self.TablaPlanificado.setVisible(False)
               self.TablaPorcentaje.setVisible(True)
               self.bandera = False
           else: 
                self.TablaPlanificado.setVisible(True)
                self.TablaPorcentaje.setVisible(False)
                self.bandera = True
     
        
    def actualizarTablaPorcentaje(self):
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
                

    def BajarTodo(self):
        if self.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "Advertencia", "No hay pedidos para bajar.")
            return

        filas_a_bajar = []
        
       
        for row in range(self.tableWidget.rowCount()):
            filas_a_bajar.append(row)

        for row in reversed(filas_a_bajar):
            self.tableWidget.selectRow(row)
            self.agregar_cargamento()
        
        total_bajados = len(filas_a_bajar)
        QMessageBox.information(self, "Información", f"Se han bajado {total_bajados} pedidos a la tabla de planificados.")

    def VentanaEnrutar(self):
        # Crear una lista para almacenar los datos de la tabla planificada
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
        self.cargar_archivo_window.show()
        self.close()
