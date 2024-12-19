from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox,QPushButton
from views.Enrutador import Ui_EnRutador
from PySide6.QtGui import QColor
import pandas as pd
from PySide6.QtCore import Qt
import random
from scipy.optimize import linprog
import numpy as np
from geopy.distance import geodesic
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox,QCheckBox
from PySide6.QtGui import QColor
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PySide6.QtGui import QIcon
from Services.DetallesDePedidoServices import DetallesPedido
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
import json
import os
from datetime import datetime

class EnRutar(QWidget, Ui_EnRutador):
    def __init__(self, planificados_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.planificados_data=planificados_data
        self.copia=planificados_data
        self.columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 
                             'Codigo Cliente', 'Codigo SKU', 'Descripcion SKU', 
                             'Zona de Entrega', 'Cant. Programada', 'TM Programadas', 
                             'Total paletas']
        self.cargar_datos(planificados_data)
        self.data_dict={}
        self.planificados =planificados_data
        self.inicializar_tabla_factura()
        self.add_add_button_row()
        self.BotonSugerir.clicked.connect(self.sugerencia)
        self.Coordenas_Valencia=(10.180189, -67.962975)
        self.camiones = {}
        self.factura_data = []
        self.lista_de_tabla_planificado=[]
        self.url_DatosDePedidos= r'.\repository\DatosDePedidos.json'
        self.url_Pedidos= r'.\repository\Pedidos.json'
        self.url_Excels= r'repository\ruta_excels.json'
        self.Limpiar_Json()
        self.Agregar_Planificados_Json()
        self.BotonMapa.clicked.connect(self.mapa)
        self.BotonMapa_2.clicked.connect(self.imprimir)
        self.Reiniciar.clicked.connect(self.ir_hacia_atras)
     
    def cargar_datos(self,planificados_data):
        self.TablaPlanificacion.setRowCount(len(planificados_data))
        self.TablaPlanificacion.setColumnCount(len(self.columnas_deseadas))
        self.TablaPlanificacion.setHorizontalHeaderLabels(self.columnas_deseadas)

        zonas_unicas = set(row[6] for row in planificados_data)
        colores_zonas = {zona: self.generar_color() for zona in zonas_unicas}

        for row_idx, row_data in enumerate(planificados_data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.TablaPlanificacion.setItem(row_idx, col_idx, item)

            zona_entrega = row_data[6]
            if zona_entrega in colores_zonas:
                color = colores_zonas[zona_entrega]
                for col in range(len(self.columnas_deseadas)):
                    item = self.TablaPlanificacion.item(row_idx, col)
                    item.setBackground(color)
    
    def cargar_excels(self):
        df_tarifas = pd.read_excel("./excels/Flete.xlsx")
        df_coordenadas = pd.read_excel("./excels/Coordenadas.xlsx")
        df_tarifas['Capacidad TM'] = pd.to_numeric(df_tarifas['Capacidad TM'], errors='coerce')
        df_tarifas['Vehículo'] = df_tarifas['Vehículo'].str.strip()
        df_tarifas = df_tarifas.dropna(subset=['Capacidad TM', 'Vehículo'])
        df_tarifas = df_tarifas[df_tarifas['Capacidad TM'] > 0]
        df_tarifas['Tarifa USD'] = pd.to_numeric(df_tarifas['Tarifa USD'], errors='coerce')
        data_dict = {
            'tarifas': df_tarifas,
            'coordenadas': df_coordenadas
        }
        return data_dict
  
    def listar_vehiculos(self, data_dict):
        df_tarifas = data_dict['tarifas']
        unique_vehicles = df_tarifas[['Vehículo', 'Capacidad TM']].drop_duplicates()
        vehicle_list = []
        for index, row in unique_vehicles.iterrows():
            vehicle_list.append((row['Vehículo'], row['Capacidad TM']))

        vehicle_list.sort(key=lambda x: x[1])
        return vehicle_list
        
     
    def Zonas_Por_Provedor(self,df_tarifas):
        zona_to_proveedor = {
            str(row['Zona']).zfill(3): (row['Nombre Proveedor'], 
                                        row['Capacidad TM'], 
                                        row['Vehículo']) 
            for index, row in df_tarifas.iterrows()
        }
        return zona_to_proveedor

    
    def Zonas_Planificado(self,df_coordenadas):
        zona_to_coords = {
            str(row['Zona de Entrega']).zfill(3): (row['Latitude'], row['Longitude']) 
            for index, row in df_coordenadas.iterrows()
        }
        return zona_to_coords
        
        
    def Cargar_Planificado(self,planificados):
        for row in range(self.TablaPlanificacion.rowCount()):
            row_data = [
                self.TablaPlanificacion.item(row, col).text() if self.TablaPlanificacion.item(row, col) else ''
                for col in range(self.TablaPlanificacion.columnCount())
            ]
        planificados.append(row_data)

    def agrupar_entregas(self, planificados, zona_to_coords):
        grouped_deliveries = []
        visited = set()
        max_peso = 26  # Peso máximo permitido por camión (en TM)
        
        for i, pedido1 in enumerate(planificados):
            if i in visited:
                continue
            
            # Crear un nuevo grupo para el pedido actual
            group = [pedido1]
            visited.add(i)
            peso_acumulado = float(pedido1[8].replace(',', '.'))  # Peso inicial del grupo (TM Programadas)
            
            for j, pedido2 in enumerate(planificados):
                if j in visited:
                    continue 
                
                # Zona del segundo pedido
                zona2 = str(pedido2[6][:3]).zfill(3)
                
                if zona2 in zona_to_coords:
                    coords2 = zona_to_coords[zona2]
                    all_within_distance = True
                    
                    # Verificar la distancia con todos los pedidos del grupo actual
                    for pedido_in_group in group:
                        zona1 = str(pedido_in_group[6][:3]).zfill(3)
                        if zona1 in zona_to_coords:
                            coords1 = zona_to_coords[zona1]
                            
                            # Calcular distancia geográfica
                            distance = geodesic(coords1, coords2).km
                            if distance >= 100:  # Condición de distancia máxima
                                all_within_distance = False
                                break
                    
                    # Verificar el peso acumulado del grupo si se agrega el pedido
                    nuevo_peso = peso_acumulado + float(pedido2[8].replace(',', '.'))
                    print(f"Evaluando pedido {j}: Peso acumulado={nuevo_peso}, Distancia válida={all_within_distance}")
                    
                    # Condiciones para agregar el pedido al grupo actual
                    if all_within_distance and nuevo_peso <= max_peso:
                        group.append(pedido2)
                        visited.add(j)
                        peso_acumulado = nuevo_peso  # Actualizar el peso acumulado
            
            # Asegurarse de que el grupo no exceda el límite de peso
            if peso_acumulado > max_peso:
                print(f"Error: El grupo excede el peso máximo permitido (26 TM): {peso_acumulado} TM")
            
            grouped_deliveries.append(group)
        
        return grouped_deliveries

    def obtener_zona_mas_lejana(self,group, zona_to_coords,Coordenas_Valencia):
        max_distance = -1
        zona_mas_lejana = None
        for pedido in group:
            zona = str(pedido[6][:3]).zfill(3)
            if zona in zona_to_coords:
                coords = zona_to_coords[zona]
                distance = geodesic(Coordenas_Valencia, coords).km
                if distance > max_distance:
                    max_distance = distance
                    zona_mas_lejana = zona
        
        return zona_mas_lejana
          
      
    def asignar_camion(self, grouped_deliveries, vehicle_list, zona_to_proveedor, zona_to_coords, tarifa_dict):
        for group_index, group in enumerate(grouped_deliveries):
            if not group:  
                continue

            first_zone = self.obtener_zona_mas_lejana(group, zona_to_coords, self.Coordenas_Valencia)
            unique_zones = set(str(pedido[6][:3]).zfill(3) for pedido in group)

            total_tm = sum(float(pedido[8].replace(',', '.')) for pedido in group)
            clientes = '+ '.join(pedido[0] for pedido in group)
            zonas = ', '.join(unique_zones)

            proveedor, capacidad, tipo_vehiculo = zona_to_proveedor.get(first_zone, (None, None, None))

            current_vehicle = None
            tarifa_usd = float('inf')
            mejor_proveedor = None

            for vehicle in vehicle_list:
                vehicle_tipo, vehicle_capacity = vehicle
                if vehicle_capacity >= total_tm:
                    current_vehicle = vehicle_tipo
                    for (prov, zona, veh), t in tarifa_dict.items():
                        if zona == first_zone and veh == current_vehicle and t < tarifa_usd:
                            tarifa_usd = t
                            mejor_proveedor = prov
                    break

            # Verificar que los valores se asignen correctamente
            self.camiones[group_index + 1] = (
                clientes or "Sin clientes",  # Valor por defecto
                current_vehicle or "Sin vehículo asignado",  # Valor por defecto
                total_tm,
                first_zone or "Zona desconocida",  # Valor por defecto
                zonas or "Zonas desconocidas",  # Valor por defecto
                tarifa_usd if tarifa_usd != float('inf') else 0,  # Tarifa predeterminada si no se encuentra
                mejor_proveedor or "Sin proveedor"  # Valor por defecto
            )

        return self.camiones
    def preparar_tarifas(self,df_tarifas):
        # Asegúrate de que las columnas necesarias existen en el DataFrame
        columnas_necesarias = ['Nombre Proveedor', 'Zona', 'Vehículo', 'Tarifa USD']
        if not all(col in df_tarifas.columns for col in columnas_necesarias):
            raise ValueError(f"Faltan columnas necesarias en el DataFrame: {columnas_necesarias}")
        
        # Crear un diccionario con las columnas seleccionadas
        tarifa_dict = {
            (str(row['Nombre Proveedor']).strip(),
            str(row['Zona']).zfill(3),
            str(row['Vehículo']).strip()): float(row['Tarifa USD'])
            for _, row in df_tarifas.iterrows()
        }
        
        return tarifa_dict    


    def sugerencia(self):
        # Cargar el JSON y obtener los pedidos no planificados
        with open(self.url_Pedidos, "r") as json_file:
            data_json = json.load(json_file)
        
        pedidos_no_planificados = data_json["PedidosNoPlanificados"]

        # Transformar los pedidos al formato esperado por self.agrupar_entregas
        pedidos_transformados = [
            [
                pedido["Nombre Cliente"],
                pedido["Fecha de la Cita"],
                pedido["Numero de Pedido"],
                pedido["Codigo Cliente"],
                pedido["Codigo SKU"],
                pedido["Descripcion SKU"],
                pedido["Zona de Entrega"],
                pedido["Cant. Programada"],
                pedido["TM Programadas"],
                pedido["Total paletas"]
            ]
            for pedido in pedidos_no_planificados
        ]

        # Continuar con la lógica actual, usando los datos transformados
        data_dict = self.cargar_excels()

        # Listar vehículos
        vehicle_list = self.listar_vehiculos(data_dict)
        tarifa_dict = self.preparar_tarifas(data_dict["tarifas"])

        # Crear diccionarios de zonas
        zona_to_proveedor = self.Zonas_Por_Provedor(data_dict["tarifas"])
        zona_to_coords = self.Zonas_Planificado(data_dict["coordenadas"])
        current_row_count = self.TablaFacturar.rowCount()

        # Reemplazar self.planificados con pedidos_transformados
        grouped_deliveries = self.agrupar_entregas(pedidos_transformados, zona_to_coords)
        camiones = self.asignar_camion(grouped_deliveries, vehicle_list, zona_to_proveedor, zona_to_coords, tarifa_dict)

        for group_index, (clientes, tipo_vehiculo, tm_programadas, zona, zonas, tarifa_usd, proveedor) in camiones.items():
            self.add_row_to_factura_table(
                carro=group_index + current_row_count,
                clientes=clientes,
                tipo_vehiculo=tipo_vehiculo,
                tm_programadas=round(tm_programadas,2),
                zona=zona,
                zonas=zonas,
                tarifa_usd=round(tarifa_usd,2),
                proveedor=proveedor
            )
            self.eliminar_de_tabla_planificacion(clientes, zonas)

    def inicializar_tabla_factura(self):
        columnas_facturar = ['*', 'Listo', 'Carro', 'Nombre de clientes', 'Tipo de vehiculo', 
                            'Cantidad TM', 'Zona', 'Zonas', 'Tarifa', 'Proveedor']
        self.TablaFacturar.setRowCount(0)
        self.TablaFacturar.setColumnCount(len(columnas_facturar))
        self.TablaFacturar.setHorizontalHeaderLabels(columnas_facturar)
        self.add_add_button_row()
        
    def agregar_fila_vacia(self):
        row_position = self.TablaFacturar.rowCount() - 1  # Antes de la fila de "agregar"
        self.TablaFacturar.insertRow(row_position)

        # Botón para acciones
        boton = QPushButton()
        boton.setIcon(QIcon('assets/3punticos.jpg'))
        boton.clicked.connect(lambda _, r=row_position: self.on_button_clicked(r))
        self.TablaFacturar.setCellWidget(row_position, 0, boton)

        # Checkbox de "listo"
        check_box = QCheckBox()
        self.TablaFacturar.setCellWidget(row_position, 1, check_box)

        # Rellenar la columna 'Carro' con el número de fila correspondiente
        self.TablaFacturar.setItem(row_position, 2, QTableWidgetItem(str(row_position + 1)))  # Asume que la columna 'Carro' es la 2
        carro = float(row_position + 1)
        # Celdas vacías para el resto de las columnas
        for col in range(3, self.TablaFacturar.columnCount()):  # Empieza desde la columna 3 (después de 'Carro')
            self.TablaFacturar.setItem(row_position, col, QTableWidgetItem(''))

        color =self.generar_color()
        for col in range(self.TablaFacturar.columnCount()):
            item = self.TablaFacturar.item(row_position, col)
            if item:
                item.setBackground(color)
         
        datos= {}
        self.factura_data.append(datos)
        datosJson= {
        'Carro': carro,
        'Informacion': {
            'Listo': False,
            'NombreDeClientes': None,
            'TipoDeVehiculo': None,
            'CantidadTM': None,
            'Zona': None,
            'Zonas': None,
            'Tarifa': None,
            'Proveedor': None,
            'Pedidos': [],
            'DatosChofer':[] ,
            'Observaciones': None 
        }
    }
        self.Agregar_a_json(datosJson)
    
    def agregar_fila_factura(self, datos):
        """
        Agrega una fila a la tabla de facturación con los datos proporcionados.
        """
        row_position = self.TablaFacturar.rowCount() - 1  # Antes de la fila de "agregar"
        self.TablaFacturar.insertRow(row_position)

        # Botón para acciones
        boton = QPushButton()
        boton.setIcon(QIcon('assets/3punticos.jpg'))
        boton.clicked.connect(lambda _, r=row_position: self.on_button_clicked(r))
        self.TablaFacturar.setCellWidget(row_position, 0, boton)

        # Checkbox de "listo"
        check_box = QCheckBox()
        self.TablaFacturar.setCellWidget(row_position, 1, check_box)

        # Agregar datos a las celdas
        for col, key in enumerate(['Carro', 'Nombre de clientes', 'Tipo de vehiculo', 'Cantidad TM',
                                    'Zona', 'Zonas', 'Tarifa', 'Proveedor'], start=2):
            valor = datos.get(key, '')
            self.TablaFacturar.setItem(row_position, col, QTableWidgetItem(str(valor)))

        # Colorear la fila aleatoriamente
        color = self.generar_color()
        for col in range(self.TablaFacturar.columnCount()):
            item = self.TablaFacturar.item(row_position, col)
            if item:
                item.setBackground(color)
                
    def actualizar_fila_agregar(self):
        if (self.TablaFacturar.rowCount() == 0 or 
            not isinstance(self.TablaFacturar.cellWidget(self.TablaFacturar.rowCount() - 1, 0), QPushButton)):
            self.add_add_button_row()
            
            
    def add_add_button_row(self):
        if self.TablaFacturar.rowCount() == 0 or not isinstance(self.TablaFacturar.cellWidget(self.TablaFacturar.rowCount() - 1, 0), QPushButton):
            row_position = self.TablaFacturar.rowCount()
            self.TablaFacturar.insertRow(row_position)

            add_button = QPushButton()
            add_button.setIcon(QIcon('assets/Mas.png'))
            add_button.setStyleSheet("border: none;")
            add_button.clicked.connect(self.agregar_fila_vacia)
            self.TablaFacturar.setCellWidget(row_position, 0, add_button)

    def add_row_to_factura_table(self, carro, clientes, tipo_vehiculo, tm_programadas, zona, zonas, tarifa_usd, proveedor):
       
        carro = self.TablaFacturar.rowCount()
        datos = {
            'Carro': carro,
            'Nombre de clientes': clientes,
            'Tipo de vehiculo': tipo_vehiculo,
            'Cantidad TM': tm_programadas,
            'Zona': zona,
            'Zonas': zonas,
            'Tarifa': tarifa_usd,
            'Proveedor': proveedor
        }
        
        coincidencias = []
        
        for planificado in self.planificados:
            nombre_cliente = planificado[0].strip()
            zona_planificada = planificado[6].split('-')[0].strip()    
            if nombre_cliente in clientes and zona_planificada in zonas:  
                pedido = {
                    'Nombre Cliente': planificado[0],
                    'Fecha de la Cita': planificado[1],
                    'Numero de Pedido': planificado[2],
                    'Codigo Cliente': planificado[3],
                    'Codigo SKU': planificado[4],
                    'Descripcion SKU': planificado[5],
                    'Zona de Entrega': planificado[6],
                    'Cant. Programada': planificado[7],
                    'TM Programadas': planificado[8],
                    'Total paletas': planificado[9]
                }
                
                coincidencias.append(pedido)
      
        datosJson= {
        'Carro': carro,
        'Informacion': {
            'Listo': False,
            'NombreDeClientes': clientes,
            'TipoDeVehiculo': tipo_vehiculo,
            'CantidadTM': tm_programadas,
            'Zona': zona,
            'Zonas': zonas,
            'Tarifa': tarifa_usd,
            'Proveedor': proveedor,
            'Pedidos': coincidencias,
            'DatosChofer':[],
            'Observaciones':""
        }
    }
        self.factura_data.append(datos)
        self.agregar_fila_factura(datos)
        self.actualizar_fila_agregar()
        self.Agregar_a_json(datosJson)
        

    def on_button_clicked(self, row):
            self.details_window = DetallesPedido(row, self)
            self.details_window.setWindowModality(Qt.ApplicationModal) 
            self.details_window.exec()
            self.actualizar_valores()
            
         
    def eliminar_de_tabla_planificacion(self, clientes, zonas):
        nombres_clientes = set(nombre.strip() for nombre in clientes.split('+'))
        zonas_entrega = set(zona.strip() for zona in zonas.split(','))

        # Abrir el archivo JSON
        if os.path.exists(self.url_Pedidos):
            with open(self.url_Pedidos, 'r') as f:
                try:
                    self.json_data = json.load(f)
                    # Si el JSON contiene una lista vacía, corregimos la estructura
                    if isinstance(self.json_data, list):
                        self.json_data = {"PedidosNoPlanificados": [], "PedidosPlanificados": self.json_data}
                except json.JSONDecodeError:
                    # Si el archivo está vacío o corrupto, inicializamos un JSON vacío
                    self.json_data = {"PedidosNoPlanificados": [], "PedidosPlanificados": []}
        else:
            # Si el archivo no existe, inicializamos un JSON vacío
            self.json_data = {"PedidosNoPlanificados": [], "PedidosPlanificados": []}

        filas_a_eliminar = []
        for row in range(self.TablaPlanificacion.rowCount()):
            # Obtener los valores de las celdas para nombre de cliente y zona
            nombre_cliente = self.TablaPlanificacion.item(row, 0).text().strip()
            zona_planificada = self.TablaPlanificacion.item(row, 6).text().split('-')[0].strip()

            # Verificamos si la fila cumple con las condiciones de eliminación
            if nombre_cliente in nombres_clientes and zona_planificada in zonas_entrega:
                filas_a_eliminar.append(row)

        # Guardamos los datos a eliminar en "PedidosNoPlanificados" antes de eliminarlos de la tabla y el JSON
        for row in filas_a_eliminar:
            pedido = {}
            for col, columna in enumerate(self.columnas_deseadas):
                # Obtenemos el valor de la celda de la fila y columna actual
                item = self.TablaPlanificacion.item(row, col)
                if item is not None:
                    pedido[columna] = item.text()  # Usamos el texto de la celda
                else:
                    pedido[columna] = ""  # Si no hay valor, asignamos un string vacío

            # Eliminar el mismo pedido de "PedidosNoPlanificados" si ya existe
            self.json_data["PedidosNoPlanificados"] = [
                p for p in self.json_data["PedidosNoPlanificados"] if p != pedido
            ]

            # Añadimos el pedido a la lista de PedidosPlanificados
            self.json_data["PedidosPlanificados"].append(pedido)

        # Ahora eliminamos las filas de la tabla
        for row in reversed(filas_a_eliminar):
            self.TablaPlanificacion.removeRow(row)

        # Guardamos los cambios de vuelta en el archivo JSON
        with open(self.url_Pedidos, 'w') as f:
            json.dump(self.json_data, f, indent=4)
            

    def guardar_datos_tabla(self):
        self.lista_de_tabla_planificado.clear()
        for row in range(self.TablaPlanificacion.rowCount()):
            row_data = {}
            for column in range(self.TablaPlanificacion.columnCount()):
                header = self.TablaPlanificacion.horizontalHeaderItem(column).text()
                item = self.TablaPlanificacion.item(row, column)
                row_data[header] = item.text() if item else ""
            self.lista_de_tabla_planificado.append(row_data)

    def Agregar_a_json(self, datosJson):
        try:
            with open(self.url_DatosDePedidos, 'r') as file:
                contenido = file.read()
                if contenido:
                    datos_existentes = json.loads(contenido)
                else:
                    datos_existentes = []
        except (FileNotFoundError, json.JSONDecodeError):
            datos_existentes = []

        datos_existentes.append(datosJson)
        
        with open(self.url_DatosDePedidos, 'w') as file:
            json.dump(datos_existentes, file, indent=4)
        

    def Agregar_Planificados_Json(self):
        columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 
                            'Codigo Cliente', 'Codigo SKU', 'Descripcion SKU', 
                            'Zona de Entrega', 'Cant. Programada', 'TM Programadas', 
                            'Total paletas']

        # Aseguramos que el archivo JSON existe, si no, inicializamos un JSON vacío
        if not os.path.exists(self.url_Pedidos):
            self.json_data = {"PedidosNoPlanificados": [], "PedidosPlanificados": []}
        else:
            # Abrimos el archivo JSON en modo lectura y cargamos su contenido
            with open(self.url_Pedidos, 'r') as f:
                try:
                    self.json_data = json.load(f)
                    
                    # Si el archivo contiene solo una lista vacía, lo corregimos
                    if isinstance(self.json_data, list):
                        self.json_data = {"PedidosNoPlanificados": [], "PedidosPlanificados": self.json_data}
                except json.JSONDecodeError:
                    # Si el archivo está vacío o corrupto, inicializamos un JSON vacío
                    self.json_data = {"PedidosNoPlanificados": [], "PedidosPlanificados": []}

        # Aseguramos que "PedidosPlanificados" esté presente en el JSON
        if "PedidosPlanificados" not in self.json_data:
            self.json_data["PedidosPlanificados"] = []

        # Iteramos sobre las filas del QTableWidget
        for row in range(self.TablaPlanificacion.rowCount()):  # Iterar sobre las filas
            fila = []
            for col in range(self.TablaPlanificacion.columnCount()):  # Iterar sobre las columnas
                # Obtenemos el valor de cada celda y lo añadimos a la fila
                item = self.TablaPlanificacion.item(row, col)
                if item is not None:
                    fila.append(item.text())  # Añadimos el texto de la celda a la fila
                else:
                    fila.append("")  # Si no hay valor, ponemos un string vacío

            # Creamos un diccionario para cada fila y lo agregamos a los pedidos planificados
            pedido = {}
            for idx, columna in enumerate(columnas_deseadas):
                if idx < len(fila):  # Asegurarnos de que la fila tiene suficientes datos
                    pedido[columna] = fila[idx]
                else:
                    pedido[columna] = ""  # Si faltan datos, dejamos un valor vacío

            self.json_data["PedidosNoPlanificados"].append(pedido)
            
 
        # Guardamos los cambios de vuelta en el archivo JSON
        with open(self.url_Pedidos, 'w') as f:
            json.dump(self.json_data, f, indent=4)

    def Limpiar_Json(self):
            try:
                
                if os.path.exists(self.url_DatosDePedidos):
                    with open(self.url_DatosDePedidos, 'w', encoding='utf-8') as file:
                        json.dump([], file, ensure_ascii=False, indent=4)
                    
                else:
                    pass

                if os.path.exists(self.url_Pedidos):
                    with open(self.url_Pedidos, 'w', encoding='utf-8') as file:
                        json.dump([], file, ensure_ascii=False, indent=4)
                    
                else:
                    pass         
            except Exception as e:
                pass
        
    def actualizar_valores(self):
        while self.TablaPlanificacion.rowCount() > 0:
            self.TablaPlanificacion.removeRow(0)
            
        try:
            with open(self.url_Pedidos, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            QMessageBox.warning(self, "Advertencia", "El archivo DatosDePedidos.json no se encontró.")
            return
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Advertencia", "El archivo DatosDePedidos.json está vacío o tiene un formato incorrecto.")
            return
        
        pedidos_no_planificados = data.get("PedidosNoPlanificados", [])
        self.TablaPlanificacion.setRowCount(len(pedidos_no_planificados))
        
        # Actualización de TablaPlanificacion
        for row_index, pedido in enumerate(pedidos_no_planificados):
            for col_index, columna in enumerate(self.columnas_deseadas):
                item = QTableWidgetItem(pedido.get(columna, ""))
                self.TablaPlanificacion.setItem(row_index, col_index, item)

        # Actualización de TablaFacturar
        try:
            with open(self.url_DatosDePedidos, 'r', encoding='utf-8') as file:
                datos_pedidos = json.load(file)
        except FileNotFoundError:
            QMessageBox.warning(self, "Advertencia", "El archivo DatosDePedidos.json no se encontró.")
            return
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Advertencia", "El archivo DatosDePedidos.json está vacío o tiene un formato incorrecto.")
            return

        # Recorremos los datos de la tabla de pedidos
        for pedido in datos_pedidos:
            carro = pedido.get("Carro", None)
            if carro is None:
                continue
            
            # Buscamos la fila que coincida con el "Carro" en la tabla TablaFacturar
            for row_index in range(self.TablaFacturar.rowCount()):
                item = self.TablaFacturar.item(row_index, 2)  # Columna 2 es "Carro"
                if item and float(item.text()) == carro:
                    # Obtenemos los datos de la fila "Informacion"
                    info = pedido.get("Informacion", {})
                    listo = info.get("Listo", None)
                    nombre_cliente = info.get("NombreDeClientes", None)
                    tipo_vehiculo = info.get("TipoDeVehiculo", None)
                    cantidad_tm = info.get("CantidadTM", None)
                    zona = info.get("Zona", None)
                    zonas = info.get("Zonas", None)
                    tarifa = info.get("Tarifa", None)
                    proveedor = info.get("Proveedor", None)
                    first_row_item = self.TablaFacturar.item(row_index, 6)  # Primera fila, columna "Zona"
                    if first_row_item:
                        color = first_row_item.background()  # Obtiene el color de fondo de la primera fila
                    # Actualizamos las columnas correspondientes
                    #self.TablaFacturar.setItem(row_index, 1, QTableWidgetItem(str(listo) if listo is not None else ""))
                    #self.TablaFacturar.setItem(row_index, 2, QTableWidgetItem(str(carro)))
                    self.TablaFacturar.setItem(row_index, 3, QTableWidgetItem(nombre_cliente if nombre_cliente is not None else ""))
                    self.TablaFacturar.setItem(row_index, 4, QTableWidgetItem(tipo_vehiculo if tipo_vehiculo is not None else ""))
                    self.TablaFacturar.setItem(row_index, 5, QTableWidgetItem(str(cantidad_tm) if cantidad_tm is not None else ""))
                    self.TablaFacturar.setItem(row_index, 6, QTableWidgetItem(zona if zona is not None else ""))
                    self.TablaFacturar.setItem(row_index, 7, QTableWidgetItem(zonas if zonas is not None else ""))
                    self.TablaFacturar.setItem(row_index, 8, QTableWidgetItem(str(tarifa) if tarifa is not None else ""))
                    self.TablaFacturar.setItem(row_index, 9, QTableWidgetItem(proveedor if proveedor is not None else ""))
                  

                    # Si encontramos un color, lo aplicamos a toda la fila
                    for col in range(self.TablaFacturar.columnCount()):
                        item = self.TablaFacturar.item(row_index, col)
                        if item:  # Asegúrate de que el item no sea None
                            item.setBackground(color)  # Aplicamos el color a cada celda de la fila
                            
                    check_box = self.TablaFacturar.cellWidget(row_index, 1)  # Columna 1 es donde está el checkbox
                    if check_box:  # Asegúrate de que el checkbox existe
                        print("Check box existe")
                        if(listo is not None and listo is not False): 
                            check_box.setChecked(True)
                            print("checkbox true")
                        else:
                            check_box.setChecked(False)
                            print("checkbox false")
              
        # Ahora agregamos las zonas de la tabla Planificacion a un conjunto único
        zonas_unicas = set()
        for row_idx in range(self.TablaPlanificacion.rowCount()):
            item = self.TablaPlanificacion.item(row_idx, 6)  # Columna 6 (Zona de Entrega)
            if item:
                zonas_unicas.add(item.text())  # Añadir el texto si el item no es None

        colores_zonas = {zona: self.generar_color() for zona in zonas_unicas}

        # Aplicamos los colores a las filas de la TablaPlanificacion
        for row_idx in range(self.TablaPlanificacion.rowCount()):
            row_data = []
            for col_idx in range(self.TablaPlanificacion.columnCount()):
                # Obtenemos el valor de la celda
                item = self.TablaPlanificacion.item(row_idx, col_idx)
                value = item.text() if item else ''
                row_data.append(value)  # Añadimos el valor a row_data

            # Aquí ya tienes la fila con todos los datos
            zona_entrega = row_data[6]  # La zona está en la columna 6 (índice 6)

            # Si la zona tiene un color asignado, lo aplicamos
            if zona_entrega in colores_zonas:
                color = colores_zonas[zona_entrega]
                for col in range(self.TablaPlanificacion.columnCount()):
                    item = self.TablaPlanificacion.item(row_idx, col)
                    if item:  # Asegúrate de que el item no sea None
                        item.setBackground(color)
                                         
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
          
    
    def ir_hacia_atras(self):
        from Services.PlanificacionServices import PlanificacionServices
        with open(self.url_Excels, 'r') as d:
            planday = json.load(d)
            
            
        Playday = planday[0].get('PlayDay', 'ruta_predeterminada.xlsx')
        inventario = planday[0].get('Inventario', 'ruta_predeterminada.xlsx')
        status = planday[0].get('Status', 'ruta_predeterminada.xlsx')
        self.nueva_ventana = PlanificacionServices(status, Playday, inventario) 
        self.nueva_ventana.show()
        self.close()
        
       
    
    def load_excel(self, path, **kwargs):
        return pd.read_excel(path, **kwargs)
    
    def mapa(self):  
        # Cargar el archivo JSON
        with open(self.url_DatosDePedidos, 'r') as file:
            datos = json.load(file)

    # Extraer nombres de clientes únicos y sus zonas por carro
        clientes_zonas_por_carro = {}
        for carro in datos:
            carro_id = carro['Carro']
            clientes_zonas_por_carro[carro_id] = []
            for pedido in carro['Informacion']['Pedidos']:
                cliente = pedido['Nombre Cliente']
                zona = pedido['Zona de Entrega']
                if cliente not in [cz['cliente'] for cz in clientes_zonas_por_carro[carro_id]]:
                    clientes_zonas_por_carro[carro_id].append({'cliente': cliente, 'zona': zona})

        # Cargar el archivo Excel con las coordenadas
        df_coordenadas = pd.read_excel('./excels/Coordenadas.xlsx')

        # Filtrar las coordenadas de los clientes únicos por carro
        coordenadas_clientes_por_carro = {}
        for carro_id, clientes_zonas in clientes_zonas_por_carro.items():
            coordenadas_clientes_por_carro[carro_id] = df_coordenadas[df_coordenadas['Nombre Cliente Padre'].isin([cz['cliente'] for cz in clientes_zonas])]

        # Graficar las coordenadas en un mapa con una imagen de fondo
        img = mpimg.imread('assets/mapa.jpg')
        fig, ax = plt.subplots()
        ax.imshow(img, extent=[-73.5, -59.8, 0.5, 12.5])  # Ajustar según las coordenadas del mapa

        # Colores para cada carro
        colors = plt.cm.get_cmap('tab10', len(coordenadas_clientes_por_carro))

        for i, (carro_id, coordenadas_clientes) in enumerate(coordenadas_clientes_por_carro.items()):
            color = colors(i)
            ax.scatter(coordenadas_clientes['Longitude'], coordenadas_clientes['Latitude'], c=[color], label=f'Carro {carro_id}')

        plt.legend()
        plt.show()
        
        
    def imprimir(self):    
            # Cargar el archivo JSON (puedes adaptarlo a tu caso)
        with open(self.url_DatosDePedidos, 'r') as f:
            json_data = json.load(f)
            
        file_path = r".\\repository\\organizador.json"
        with open(file_path, 'r') as json_file:
            planificador = json.load(json_file)
       
        with open(self.url_Excels, 'r') as d:
            planday = json.load(d)
            
            
        excel_file = planday[0].get('PlayDay', 'ruta_predeterminada.xlsx')

        # Llamar a la función para generar el Excel
        self.generar_excel(json_data, excel_file,planificador)
        


    def generar_excel(self, json_data, excel_file, planificador):
        def calcular_peso_sistema(tm_programadas):
            tm_programadas = float(tm_programadas) * 1000
            return round(tm_programadas, 2)

        def calcular_peso_real(cantidad_programada, sku):
            df = pd.read_excel(".\excels\maestro Productos.xlsx")
            Peso_Real_Total = 0
            cantidad_programada = float(cantidad_programada)
            peso_real_fila = df[df['SKU'] == sku]['Peso real']
            if not peso_real_fila.empty:
                peso_real = float(peso_real_fila.values[0])
                Peso_Real_Total += round(peso_real * cantidad_programada, 2)
            return round(Peso_Real_Total, 2)

        def palea_por_sku(cantidad_programada, sku):
            cantidad_programada = float(cantidad_programada)
            df = pd.read_excel(".\excels\maestro Productos.xlsx")
            if sku == "20532":
                return 'paletas'
            sku_value = df.loc[df['Cod'] == sku, 'PALETIZADO'].values
            if sku_value.size > 0:
                return round(cantidad_programada / float(sku_value), 2)
            else:
                return 'Granel'

        # Cargar el archivo Excel en un DataFrame
        df_excel = pd.read_excel(excel_file)

        # Crear un objeto de Excel para escribir los datos
        with pd.ExcelWriter('salida_pedidos.xlsx', engine='openpyxl') as writer:
            # Asegurarse de que al menos una hoja esté visible (puede ser vacía al principio)
            pd.DataFrame().to_excel(writer, sheet_name='Hoja Inicial', index=False)
            
            # Crear una lista vacía para almacenar las filas del nuevo Excel
            filas_nuevas = []

            # Iterar sobre los carros en el JSON
            for carro in json_data:
                if carro['Informacion']['Listo']:  # Solo procesar carros con 'Listo': True
                    chofer_data = carro['Informacion']['DatosChofer'][0]  # Datos del chofer del carro

                    # Iterar sobre los pedidos del carro
                    for pedido in carro['Informacion']['Pedidos']:
                        # Buscar información en el DataFrame de Excel
                        codigo_cliente_hijo = pedido["Codigo Cliente"]
                        numero_pedido = pedido["Numero de Pedido"]
                        
                        # Filtrar el DataFrame con el código de cliente hijo y número de pedido
                        filtro_excel = df_excel[(df_excel['Codigo Cliente'] == float(codigo_cliente_hijo)) & 
                                                (df_excel['Numero de Pedido'] == float(numero_pedido))]

                        if not filtro_excel.empty:
                            # Depuración: si encontró una coincidencia, mostrar los valores encontrados
                            pedidos_encontrados = True

                            # Tomar las columnas relevantes del Excel para este pedido
                            region_venta = filtro_excel['Region de Venta'].values[0]
                            rif = filtro_excel['Rif'].values[0]
                            direccion_cliente_hijo = filtro_excel['Direccion cliente hijo'].values[0]
                            codigo_sica = filtro_excel['Codigo SICA'].values[0]

                            # Validación para 'TipoDeVehiculo'
                            tipo_transporte = pedido.get('TipoDeVehiculo', 'Desconocido')  # Si no existe, asigna 'Desconocido'

                            # Crear la fila con todos los datos necesarios
                            fila = {
                                'concat': f"{pedido['Numero de Pedido']} {pedido['Codigo SKU']}",
                                'PEDIDOS': pedido['Numero de Pedido'],
                                'Codigo cliente padre': filtro_excel['Codigo Cliente Padre'].values[0],
                                'Codigo cliente Hijo': pedido['Codigo Cliente'],
                                'Nombre Cliente': pedido['Nombre Cliente'],
                                'Codigo SKU': pedido['Codigo SKU'],
                                'Descripcion SKU': pedido['Descripcion SKU'],
                                'Zona de Entrega': pedido['Zona de Entrega'],
                                'Region de Venta': region_venta,
                                'Rif': rif,
                                'Direccion cliente hijo': direccion_cliente_hijo,
                                'Codigo SICA': codigo_sica,
                                'Cant unidad de venta': pedido['Cant. Programada'],
                                'Toneladas': pedido['TM Programadas'],
                                'PLANIFICADOR': planificador["selected_user"],
                                'TIPO TRANSPORTE': carro['Informacion']['TipoDeVehiculo'],
                                'TRANSPORTE': carro['Informacion']['Proveedor'],
                                'CHOFER': chofer_data['Chofer'],
                                'CEDULA': chofer_data['Cedula'],
                                'PLACA': chofer_data['Placa'],
                                'ZONA A PAGAR': carro['Informacion']['Zona'],
                                'OBSERVACIONES': carro['Informacion']['Observaciones'],
                                'Paletas': palea_por_sku(pedido['Cant. Programada'], pedido['Codigo SKU']),
                                'FECHA DE DESPACHO': datetime.now().strftime('%d-%m-%Y'),
                                'Peso Sistema': calcular_peso_sistema(pedido['TM Programadas']),
                                'Peso Real': calcular_peso_real(pedido['Cant. Programada'], pedido['Codigo SKU']),
                                'TIPO CARGA': 'PT' if isinstance(palea_por_sku(pedido['Cant. Programada'], pedido['Codigo SKU']), (int, float)) else 'Granel',
                                'MES': datetime.now().strftime('%m'),
                            }

                            # Añadir la fila a la lista de filas
                            filas_nuevas.append(fila)
                        else:
                            # Depuración: si no encontró coincidencia, mostrar un mensaje
                            print(f"No se encontró ninguna coincidencia para Código Cliente Hijo: {codigo_cliente_hijo} y Número de Pedido: {numero_pedido}")

            # Si hay filas para escribir, guardarlas en una nueva hoja
            if filas_nuevas:
                df_to_write = pd.DataFrame(filas_nuevas)
                df_to_write.to_excel(writer, index=False, sheet_name='Pedidos Detallados')
                # Mostrar mensaje de éxito
                self.mostrar_mensaje("Éxito", "El archivo de pedidos ha sido generado exitosamente.")
            else:
                # Mostrar mensaje si no hay pedidos que facturar
                self.mostrar_mensaje("Advertencia", "No hay pedidos listos para facturar.")

                
                
                
    def mostrar_mensaje(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  # Puedes cambiar el icono si lo deseas
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.exec()
 
"""
'concat' Numero de Pedido + Codigo SKU json
'PEDIDOS' Numero de Pedido
'Codigo cliente padre' Buscar enxcel
'Codigo cliente Hijo'  Buscar en el excel
'Nombre Cliente'	Nombre de Cliente
'Codigo SKU' Codigo SKU json
'Descripcion SKU' Descripcion SKU json
'Zona de Entrega' Zona de Entrega json	
'Region de Venta' buscar en el excel 	
'Rif' buscar en el excel	
'Direccion cliente hijo' buscar en el excel	
'Codigo SICA'	buscar en el excel
'Cant unidad de venta'	Cant. Programada jso 
'Toneladas'	TM Programadas json
'PLANIFICADOR'	Json Planificador
'TIPO TRANSPORTE' TipoDeVehiculo json	
'TRANSPORTE' Proveedor	json
'CHOFER' Lista de DatosChofer : Chofer json
'CEDULA' Lista de DatosChofer : Cedula	json
'PLACA'	 Lista de DatosChofer : Placa json
'ZONA A PAGAR' Zona	json
'OBSERVACIONES' Observaciones json	
'Paletas' Paletas	json
'FECHA DE DESPACHO'	fecha de hoy
'Peso Sistema'	Calcular
'Peso Real'	 Calcular
'TIPO CARGA' Si Tm es un numero PT de lo contrario Grandel
'MES' tomar el mes actual	        
"""