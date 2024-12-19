from PySide6.QtWidgets import QWidget
from views.DetallesPedido import Ui_Pedido
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox,QCheckBox
from PySide6.QtGui import QColor
import random
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QTableWidgetItem
import random
from PySide6.QtWidgets import QDialog
from views.DetallesPedido import Ui_Pedido
import json
from Services.PedidosHuerfanosServices import PedidosHuerfano
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
import os
import pandas as pd


class DetallesPedido(QDialog, Ui_Pedido):
    def __init__(self,row, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.url_DatosDePedidos= r'.\repository\DatosDePedidos.json'
        self.url_Pedidos= r'.\repository\Pedidos.json'
        self.row=row+1
        self.populate_table()
        self.cargar_planificador()
        self.BotonMas.clicked.connect(self.Agregar_Un_Pedido)
        self.BotonListo.clicked.connect(self.boton_listo)
        self.BotonMenos.clicked.connect(self.boton_descartar)
        self.url_maestrico_producto=0
        self.cargar_planificador()
        self.TipoVehi.currentIndexChanged.connect(self.tarifa)
        
        
         
    def populate_table(self):
        columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 'Codigo Cliente', 
                            'Codigo SKU', 'Descripcion SKU', 'Zona de Entrega', 'Cant. Programada', 
                            'TM Programadas', 'Total paletas']
        self.TablaDetalles.setColumnCount(len(columnas_deseadas))
        self.TablaDetalles.setHorizontalHeaderLabels(columnas_deseadas)
        try:
            with open(self.url_DatosDePedidos, 'r') as f:
                datos_json = json.load(f)

            for item in datos_json:
                if item['Carro'] == self.row:
                    pedidos = item['Informacion'].get('Pedidos', [])  # Usamos get para evitar None en caso de clave ausente

                    # Verificamos si la lista de Pedidos no está vacía
                    if pedidos:
                        for pedido in pedidos:
                            fila = [
                                pedido.get('Nombre Cliente', ''),
                                pedido.get('Fecha de la Cita', ''),
                                pedido.get('Numero de Pedido', ''),
                                pedido.get('Codigo Cliente', ''),
                                pedido.get('Codigo SKU', ''),
                                pedido.get('Descripcion SKU', ''),
                                pedido.get('Zona de Entrega', ''),
                                pedido.get('Cant. Programada', ''),
                                pedido.get('TM Programadas', ''),
                                pedido.get('Total paletas', '')
                            ]
                            self.agregar_fila_a_tabla(fila)
                            self.llenar_datos()
                            zonas_unicas = set(self.TablaDetalles.item(row_idx, 6).text() for row_idx in range(self.TablaDetalles.rowCount()))
                            colores_zonas = {zona: self.generar_color() for zona in zonas_unicas}

                            # Ahora iteramos sobre las filas y columnas de la tabla
                            for row_idx in range(self.TablaDetalles.rowCount()):
                                row_data = []
                                
                                for col_idx in range(self.TablaDetalles.columnCount()):
                                    # Obtenemos el valor de la celda
                                    item = self.TablaDetalles.item(row_idx, col_idx)
                                    value = item.text() if item else ''
                                    row_data.append(value)  # Añadimos el valor a row_data
                                
                                # Aquí ya tienes la fila con todos los datos
                                zona_entrega = row_data[6]  # La zona está en la columna 6 (índice 6)
                                
                                # Si la zona tiene un color asignado, la aplicamos
                                if zona_entrega in colores_zonas:
                                    color = colores_zonas[zona_entrega]
                                    for col in range(self.TablaDetalles.columnCount()):
                                        item = self.TablaDetalles.item(row_idx, col)
                                        item.setBackground(color)  # Aplicamos el color a cada celda de la fila

                        else:
                            pass

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al leer el archivo JSON: {e}")

   
    def cargar_planificador(self):
        file_path = r".\\repository\\organizador.json"
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        self.Planificador.setText(data["selected_user"])
                    
    def llenar_datos(self): 
        tm_programadas_col = self.TablaDetalles.columnCount() - 2  
        total_paletas_col = self.TablaDetalles.columnCount() - 1  
        tm_total = 0
        total_paletas = 0

        # Recorremos todas las filas de la tabla para sumar los valores de TM Programadas y Total Paletas
        for row in range(self.TablaDetalles.rowCount()):
            tm_value = self.TablaDetalles.item(row, tm_programadas_col)
            paletas_value = self.TablaDetalles.item(row, total_paletas_col)
            if tm_value and tm_value.text():
                tm_total += float(tm_value.text()) 
            if paletas_value and paletas_value.text():
                total_paletas += float(paletas_value.text())  
                    
        try:
            with open(self.url_DatosDePedidos, 'r') as f:
                datos_json = json.load(f)

            # Actualizamos los valores de TM Totales y Total Paletas en la interfaz
            self.TMtotales.setText(str(round(tm_total, 2)))  
            self.TotalPaletas.setText(str(round(total_paletas, 2)))

            # Buscar el carro correspondiente en el archivo JSON
            tipo_vehiculo = ''
            proveedor = ''
            zona_pagar=''
            observaciones=''
            chofer=None
            placa=None
            cedula=None
            Diccionario_Sku_TmProgrmada={}
            Peso_Real=0
            Peso_Real_Total=0
            df = pd.read_excel(".\excels\maestro Productos.xlsx")
            

            # Buscar el carro que corresponde a la fila actual
            for item in datos_json:
                if item['Carro'] == self.row:  # Suponiendo que self.row es el carro que estamos buscando
                    tipo_vehiculo = item['Informacion'].get('TipoDeVehiculo', '')
                    proveedor = item['Informacion'].get('Proveedor', '')
                    zona_pagar=item['Informacion'].get('Zona', '')
                    tarifa=item['Informacion'].get('Tarifa', '')
                    observaciones=item['Informacion'].get('Observaciones', '')
                    if item['Informacion']['DatosChofer']:
                        chofer_info = item['Informacion']['DatosChofer'][0]
                        chofer = chofer_info.get('Chofer', '')
                        placa = chofer_info.get('Placa', '')
                        cedula = chofer_info.get('Cedula', '')
                    self.Planificador.setText(self.cargar_planificador())
                    self.ZonaApagar.setText(zona_pagar)
                    self.Chofer.setText(chofer)
                    self.Placa.setText(placa)
                    self.Cedula.setText(cedula)
                    self.Observaciones.setText(observaciones)
                    self.pesosistema=float(self.TMtotales.text())*1000
                    self.PesoSistema.setText(str(round(self.pesosistema,2)))
                    for pedido in item['Informacion']['Pedidos']:
                        sku = pedido['Codigo SKU']
                        cantidad_programada = float(pedido['Cant. Programada'])
                        Diccionario_Sku_TmProgrmada[sku] = cantidad_programada

                        # Buscar el peso real en el DataFrame del Excel
                        peso_real_fila = df[df['SKU'] == sku]['Peso real']
                        if not peso_real_fila.empty:
                            peso_real = float(peso_real_fila.values[0])
                            Peso_Real_Total += round(peso_real * cantidad_programada,2)
                            
                    self.PesoReal.setText(str(round(Peso_Real_Total,2)))
             
                    break  #

           
            # Establecemos el valor de Tipo de Vehículo en el ComboBox
            for index in range(self.TipoVehi.count()):
                if self.TipoVehi.itemText(index) == tipo_vehiculo:
                    self.TipoVehi.setCurrentIndex(index)
                    break

            # Establecemos el valor de Proveedor en el ComboBox
            for index in range(self.Provedor.count()):
                if self.Provedor.itemText(index) == proveedor:
                    self.Provedor.setCurrentIndex(index)
                    break
        
            self.Tarifa.setText(str(tarifa))
        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al leer el archivo JSON: {e}")
  
    def agregar_fila_a_tabla(self,fila):
        row_position = self.TablaDetalles.rowCount()
        self.TablaDetalles.insertRow(row_position)
        for col, valor in enumerate(fila):
            self.TablaDetalles.setItem(row_position, col, QTableWidgetItem(str(valor)))    
        
    def Agregar_Un_Pedido(self):
        self.Limpiar_Json()
        self.pedidos = PedidosHuerfano(self.row, self)
        self.pedidos.setWindowModality(Qt.ApplicationModal) 
        self.pedidos.exec()
        if(self.bandera() == True):
          
            self.Agregar_Pedidos_Agregados()
            self.llenar_datos()
 
        else: 
            print("no lo pulso")
        
    def Agregar_Pedidos_Agregados(self):
        while self.TablaDetalles.rowCount() > 0:
            self.TablaDetalles.removeRow(0)

        columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 'Codigo Cliente', 
                            'Codigo SKU', 'Descripcion SKU', 'Zona de Entrega', 'Cant. Programada', 
                            'TM Programadas', 'Total paletas']

        try:
            with open(self.url_DatosDePedidos, 'r', encoding='utf-8') as file:
                datos_pedidos = json.load(file)
        except FileNotFoundError:
            QMessageBox.warning(self, "Advertencia", "El archivo DatosDePedidos.json no se encontró.")
            return
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Advertencia", "El archivo DatosDePedidos.json está vacío o tiene un formato incorrecto.")
            return

        carro_id = self.row  
        carro = None
        for item in datos_pedidos:
            if item["Carro"] == carro_id:
                carro = item
                break

        if not carro:
            QMessageBox.warning(self, "Advertencia", f"No se encontró el carro con ID {carro_id} en DatosDePedidos.")
            return

        # Extraer los pedidos del carro encontrado
        pedidos_del_carro = carro["Informacion"]["Pedidos"]
        # Obtener zonas únicas y asignar colores
        zonas_unicas = {pedido['Zona de Entrega'][:3] for pedido in pedidos_del_carro}  # Usamos solo los primeros 3 caracteres
        colores_zonas = {zona: self.generar_color() for zona in zonas_unicas}
        # Insertar los pedidos en la tabla
        for pedido in pedidos_del_carro:
            row_position = self.TablaDetalles.rowCount()
            self.TablaDetalles.insertRow(row_position)
            
            # Insertar cada columna en la fila
            for column, header in enumerate(columnas_deseadas):
                item_text = pedido.get(header, "")
                item = QTableWidgetItem(item_text)
                
                # Aplicar color basado en la zona de entrega
                zona_entrega = pedido['Zona de Entrega'][:3]  # Usamos solo los primeros 3 caracteres de la zona
                if zona_entrega in colores_zonas:
                    color = colores_zonas[zona_entrega]
                    item.setBackground(color)
                
                self.TablaDetalles.setItem(row_position, column, item)

        # Calcular los totales de TM Programadas y Total paletas
        tm_programadas_col = self.TablaDetalles.columnCount() - 2  # TM Programadas
        total_paletas_col = self.TablaDetalles.columnCount() - 1    # Total paletas

        tm_total = 0
        total_paletas = 0
        clientes = set()
        zonas = set()
        for row in range(self.TablaDetalles.rowCount()):
            tm_value = self.TablaDetalles.item(row, tm_programadas_col)
            paletas_value = self.TablaDetalles.item(row, total_paletas_col)
            
            # Sumar los valores de TM y Total paletas
            if tm_value and tm_value.text():
                tm_total += float(tm_value.text())
            if paletas_value and paletas_value.text():
                total_paletas += float(paletas_value.text())

            # Obtener nombres de clientes y zonas
            cliente_value = self.TablaDetalles.item(row, columnas_deseadas.index('Nombre Cliente'))
            zona_value = self.TablaDetalles.item(row, columnas_deseadas.index('Zona de Entrega'))
            
            if cliente_value and cliente_value.text():
                clientes.add(cliente_value.text())
            if zona_value and zona_value.text():
                zonas.add(zona_value.text()[:3]) 

        try:
            
            planificador = self.Planificador.text()
            tmtotales = self.TMtotales.text()
            peso_real = self.PesoReal.text()
            peso_sistema = self.PesoSistema.text()
            total_paletas2 = self.TotalPaletas.text()
            cedula = self.Cedula.text()
            chofer = self.Chofer.text()
            observaciones = self.Observaciones.text()
            placa = self.Placa.text()
            provedor = self.Provedor.currentText()
            tipo_vehi = self.TipoVehi.currentText()
            zona_apagar = self.ZonaApagar.text()
            
            if all([planificador, tmtotales, peso_real, peso_sistema, total_paletas2, cedula, chofer, observaciones, placa, provedor, tipo_vehi, zona_apagar]):
                     datos_a_guardar = {
                        "Listo": True, 
                        "NombreDeClientes": ' + '.join(clientes),
                        "Zonas": ','.join(zonas),
                        "CantidadTM": round(tm_total, 2),
                        "Total_paletas": round(total_paletas, 2),
                        "TipoDeVehiculo": self.TipoVehi.currentText(),
                        "Proveedor": self.Provedor.currentText(),
                        "Tarifa": self.Tarifa.text(),
                        "Zona": self.ZonaApagar.text(),
                        "DatosChofer":[{
                                    "Chofer": self.Chofer.text(),
                                    "Cedula": self.Cedula.text(),
                                    "Placa": self.Placa.text()
                                    }],
                        "Observaciones":self.Observaciones.text()
                    }
            else: 
                   datos_a_guardar = {
                       "Listo": None, 
                        "NombreDeClientes": ' + '.join(clientes),
                        "Zonas": ','.join(zonas),
                        "CantidadTM": round(tm_total, 2),
                        "Total_paletas": round(total_paletas, 2),
                        "TipoDeVehiculo": self.TipoVehi.currentText(),
                        "Proveedor": self.Provedor.currentText(),
                        "Tarifa": self.Tarifa.text(),
                        "Zona": self.ZonaApagar.text(),
                        "DatosChofer":[{
                                    "Chofer": self.Chofer.text(),
                                    "Cedula": self.Cedula.text(),
                                    "Placa": self.Placa.text()
                                    }],
                        "Observaciones":self.Observaciones.text()
                    }

                # Buscar el carro específico y actualizar la información
            for item in datos_pedidos:
                    if item["Carro"] == carro_id:
                        item["Informacion"].update(datos_a_guardar)
                        break
            

            # Guardar los cambios en el archivo JSON
            with open(self.url_DatosDePedidos, 'w', encoding='utf-8') as file:
                json.dump(datos_pedidos, file, ensure_ascii=False, indent=4)

            print(f"Datos actualizados en carro {carro_id}: {datos_a_guardar}")

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error al guardar los datos: {e}")
            print(f"Error al guardar los datos: {e}")

        # Actualizar los totales en la interfaz
        self.TMtotales.setText(str(round(tm_total, 2)))  
        self.TotalPaletas.setText(str(round(total_paletas, 2)))

    def Limpiar_Json(self):
        file_path = r'.\repository\bandera.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                datos = json.load(file)
        except FileNotFoundError:
            datos = {}

        datos['bandera'] = 0

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(datos, file, ensure_ascii=False, indent=4)
            
            
        file_path2 = r'.\repository\planificados.json'
    
        try:
            # Verificar si el archivo existe
            if os.path.exists(file_path2):
                # Sobrescribir el archivo con una lista vacía
                with open(file_path2, 'w', encoding='utf-8') as file:
                    json.dump([], file, ensure_ascii=False, indent=4)
                
            else:
               pass
        
        except Exception as e:
            pass
    
    def bandera(self):
        file_path = r'.\repository\bandera.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                datos = json.load(file)
                
            if (datos.get('bandera') == 1): 
                return True
            else:
                return False
            
        except FileNotFoundError:
            pass
                

    def tarifa(self):
        df_tarifas = pd.read_excel("./excels/Flete.xlsx")
        df_tarifas['Capacidad TM'] = pd.to_numeric(df_tarifas['Capacidad TM'], errors='coerce')
        df_tarifas['Vehículo'] = df_tarifas['Vehículo'].str.strip()
        df_tarifas = df_tarifas.dropna(subset=['Capacidad TM', 'Vehículo'])
        df_tarifas = df_tarifas[df_tarifas['Capacidad TM'] > 0]
        df_tarifas['Tarifa USD'] = pd.to_numeric(df_tarifas['Tarifa USD'], errors='coerce')
        
        # Convertir la columna de zonas a string
        df_tarifas['Zona'] = df_tarifas['Zona'].astype(str)
        
        selected_vehiculo = self.TipoVehi.currentText()
        selected_provedor = self.Provedor.currentText()
        zona_a_pagar = self.ZonaApagar.text()
        
        # Filtrar por proveedor, vehículo y zona
        df_filtrado = df_tarifas[
            (df_tarifas['Nombre Proveedor'] == selected_provedor) &
            (df_tarifas['Vehículo'] == selected_vehiculo) &
            (df_tarifas['Zona'] == zona_a_pagar)
        ]
        
        if not df_filtrado.empty:
            tarifa = df_filtrado['Tarifa USD'].iloc[0]
            self.Tarifa.setText(str(tarifa))
        else:
            return "No se encontró tarifa para los criterios seleccionados."

    
                
    def generar_color(self):
        while True:
            # Generar componentes de color con valores altos para obtener colores claros
            red = random.randint(150, 255)
            green = random.randint(150, 255)
            blue = random.randint(150, 255)
            color = QColor(red, green, blue)
            # Excluir colores muy oscuros
            if color.value() > 150:  # Ajusta este umbral según sea necesario
                return color

    def boton_listo(self):
        self.Agregar_Pedidos_Agregados()
        planificador = self.Planificador.text()
        tmtotales = self.TMtotales.text()
        peso_real = self.PesoReal.text()
        peso_sistema = self.PesoSistema.text()
        total_paletas = self.TotalPaletas.text()
        cedula = self.Cedula.text()
        chofer = self.Chofer.text()
        observaciones = self.Observaciones.text()
        placa = self.Placa.text()
        provedor = self.Provedor.currentText()
        tipo_vehi = self.TipoVehi.currentText()
        zona_apagar = self.ZonaApagar.text()
        
            # Verificar si todos los campos están llenos
        if all([planificador, tmtotales, peso_real, peso_sistema, total_paletas, cedula, chofer, observaciones, placa, provedor, tipo_vehi, zona_apagar]):
            # Mostrar mensaje de éxito
            QMessageBox.information(self, "Éxito", "Guardado Con Exito Listo Para Despacho")
            self.close()
        else:
            # Mostrar mensaje de error
            QMessageBox.warning(self, "Alerta", "Faltan Informacion Por Cargar Para Poder Despachar")
            self.close()

    def boton_descartar(self):
        selected_row = self.TablaDetalles.currentRow()    
        if selected_row < 0:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para sacar.")
            return

        # Obtener los datos de la fila seleccionada
        fila_datos = {}
        for column in range(self.TablaDetalles.columnCount()):
            header = self.TablaDetalles.horizontalHeaderItem(column).text()
            item = self.TablaDetalles.item(selected_row, column)
            fila_datos[header] = item.text() if item else ""

        self.Eliminar_json_planificados(fila_datos)
        self.TablaDetalles.removeRow(selected_row)

    def Eliminar_json_planificados(self, fila_datos):
        # Cargar los datos de los JSON
        with open(self.url_Pedidos, 'r') as file:
            pedidos_data = json.load(file)
        with open(self.url_DatosDePedidos, 'r') as file:
            datos_pedidos_data = json.load(file)
        
        # Obtener las listas de pedidos
        pedidos_planificados = pedidos_data.get("PedidosPlanificados", [])
        pedidos_no_planificados = pedidos_data.get("PedidosNoPlanificados", [])

        # Buscar y mover el pedido de PedidosPlanificados a PedidosNoPlanificados
        pedido_encontrado = None
        for pedido in pedidos_planificados:
            if pedido['Numero de Pedido'] == fila_datos['Numero de Pedido']:
                pedido_encontrado = pedido
                break
        
        if pedido_encontrado:
            pedidos_planificados.remove(pedido_encontrado)
            pedidos_no_planificados.append(pedido_encontrado)
        
        # Actualizar el diccionario con las listas modificadas
        pedidos_data["PedidosPlanificados"] = pedidos_planificados
        pedidos_data["PedidosNoPlanificados"] = pedidos_no_planificados

        # Guardar los cambios en el archivo Pedidos.json
        with open(self.url_Pedidos, 'w') as file:
            json.dump(pedidos_data, file, indent=4)
        
        # Buscar y eliminar el pedido de DatosDePedidos
        for pedido in datos_pedidos_data:
            if any(p['Numero de Pedido'] == fila_datos['Numero de Pedido'] for p in pedido['Informacion']['Pedidos']):
                pedido['Informacion']['Pedidos'] = [p for p in pedido['Informacion']['Pedidos'] if p['Numero de Pedido'] != fila_datos['Numero de Pedido']]
                break
        
        # Guardar los cambios en el archivo DatosDePedidos.json
        with open(self.url_DatosDePedidos, 'w') as file:
            json.dump(datos_pedidos_data, file, indent=4)
        
