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


class EnRutar(QWidget, Ui_EnRutador):
    def __init__(self, planificados_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.planificados_data=planificados_data
        self.populate_table(planificados_data)
        self.BotonSugerir.clicked.connect(self.Sugerir)
        self.factura_data = []
        self.populate_factura_table()
        self.add_add_button_row()
    def populate_table(self, planificados_data):
        columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 
                             'Codigo Cliente', 'Codigo SKU', 'Descripcion SKU', 
                             'Zona de Entrega', 'Cant. Programada', 'TM Programadas', 
                             'Total paletas']
        
        self.TablaPlanificacion.setRowCount(len(planificados_data))
        self.TablaPlanificacion.setColumnCount(len(columnas_deseadas))
        self.TablaPlanificacion.setHorizontalHeaderLabels(columnas_deseadas)

        zonas_unicas = set(row[6] for row in planificados_data)
        colores_zonas = {zona: QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for zona in zonas_unicas}

        for row_idx, row_data in enumerate(planificados_data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.TablaPlanificacion.setItem(row_idx, col_idx, item)

            zona_entrega = row_data[6]
            if zona_entrega in colores_zonas:
                color = colores_zonas[zona_entrega]
                for col in range(len(columnas_deseadas)):
                    item = self.TablaPlanificacion.item(row_idx, col)
                    item.setBackground(color)

    def Sugerir(self):

        df_tarifas = pd.read_excel("./excels/Flete.xlsx")
        df_coordenadas = pd.read_excel("./excels/Coordenadas.xlsx")
        df_tarifas['Capacidad TM'] = pd.to_numeric(df_tarifas['Capacidad TM'], errors='coerce')
        df_tarifas['Vehículo'] = df_tarifas['Vehículo'].str.strip()   
        df_tarifas = df_tarifas.dropna(subset=['Capacidad TM', 'Vehículo'])
        df_tarifas = df_tarifas[df_tarifas['Capacidad TM'] > 0] 
        df_tarifas['Tarifa USD'] = pd.to_numeric(df_tarifas['Tarifa USD'], errors='coerce')
        tarifa_dict = {}
    
        for index, row in df_tarifas.iterrows():
            proveedor = row['Nombre Proveedor']
            zona = str(row['Zona']).zfill(3) 
            vehiculo = row['Vehículo']
            tarifa = row['Tarifa USD']
            if (proveedor, zona, vehiculo) not in tarifa_dict or tarifa < tarifa_dict[(proveedor, zona, vehiculo)]:
                tarifa_dict[(proveedor, zona, vehiculo)] = tarifa

        
        unique_vehicles = df_tarifas[['Vehículo', 'Capacidad TM']].drop_duplicates()
       
        # Crear una lista de vehículos únicos y sus capacidades
        vehicle_list = []
        for index, row in unique_vehicles.iterrows():
            vehicle_list.append((row['Vehículo'], row['Capacidad TM']))

        
        # Ordenar la lista de vehículos por capacidad (ascendente)
        vehicle_list.sort(key=lambda x: x[1])
        
        zona_to_proveedor = {
            str(row['Zona']).zfill(3): (row['Nombre Proveedor'], 
                                        row['Capacidad TM'], 
                                        row['Vehículo']) 
            for index, row in df_tarifas.iterrows()
        }
        
        zona_to_coords = {
            str(row['Zona de Entrega']).zfill(3): (row['Latitude'], row['Longitude']) 
            for index, row in df_coordenadas.iterrows()
        }

        planificados = []
        for row in range(self.TablaPlanificacion.rowCount()):
            row_data = [
                self.TablaPlanificacion.item(row, col).text() if self.TablaPlanificacion.item(row, col) else ''
                for col in range(self.TablaPlanificacion.columnCount())
            ]
            planificados.append(row_data)

        grouped_deliveries = []
        visited = set()

        for i, pedido1 in enumerate(planificados):
            if i in visited:
                continue
            
            group = [pedido1]
            visited.add(i)
            
            for j, pedido2 in enumerate(planificados):
                if j in visited:
                    continue
                
                zona1 = str(pedido1[6][:3]).zfill(3)  # Normalizar a string
                zona2 = str(pedido2[6][:3]).zfill(3)
                if zona1 in zona_to_coords and zona2 in zona_to_coords:
                    coords1 = zona_to_coords[zona1]
                    coords2 = zona_to_coords[zona2]
                    
                    distance = geodesic(coords1, coords2).km
                    if distance <= 100:
                        group.append(pedido2)
                        visited.add(j)
            
            grouped_deliveries.append(group)

        # Asignar camiones a grupos
        results = []
        
        for group_index, group in enumerate(grouped_deliveries):
            unique_zones = set(str(pedido[6][:3]).zfill(3) for pedido in group)
            
            # Asumir la primera zona para la asignación del camión
            first_zone = next(iter(unique_zones))
            proveedor, capacidad, tipo_vehiculo = zona_to_proveedor.get(first_zone, (None, None, None))

            total_tm = sum(float(pedido[8].replace(',', '.')) for pedido in group)  
            
            # Salida de depuración
            print(f"Grupo {group_index + 1}:")
            print(f"  Zona: {first_zone}")
            print(f"  Total TM Programadas: {total_tm}")
            
            # Buscar el vehículo con la capacidad más cercana a la carga total
            for vehicle in vehicle_list:
                vehicle_tipo, vehicle_capacity = vehicle
                if vehicle_capacity >= total_tm:
                    current_capacity = vehicle_capacity
                    current_vehicle = vehicle_tipo
                    print(f"  Asignando vehículo: {current_vehicle} con capacidad {current_capacity}")
                    break
            else:
                print("  No se encontró un vehículo adecuado.")
                current_capacity = None
                current_vehicle = None

            # Preparar la cadena de salida
            result_str = (f"Carro {group_index + 1} "
                        f"Tipo de vehículo: {current_vehicle}, "
                        f"Capacidad: {current_capacity} TM, "
                        f"Carga: {total_tm} TM, "
                        f"Pedidos: {', '.join([pedido[2] for pedido in group])}")
            results.append(result_str)

        # Mostrar resultados en el PlainTextEdit ResumenText
        resumen_texto = ""
        clientes_sin_coordenadas = []
        
        for group_index, group in enumerate(grouped_deliveries):
            unique_zones = set(str(pedido[6][:3]).zfill(3) for pedido in group)
            
            first_zone = next(iter(unique_zones))
            
            total_tm = sum(float(pedido[8].replace(',', '.')) for pedido in group)
            
            clientes_pedidos = {}
            
            for pedido in group:
                cliente_nombre = pedido[4]  # Asumiendo que el nombre del cliente está en la columna 4
                if cliente_nombre not in clientes_pedidos:
                    clientes_pedidos[cliente_nombre] = []
                clientes_pedidos[cliente_nombre].append(pedido[2])  # Asumiendo que el número de pedido está en la columna 2
                
                # Verificar si el cliente tiene coordenadas
                zona = str(pedido[6][:3]).zfill(3)
                if zona not in zona_to_coords:
                    clientes_sin_coordenadas.append(cliente_nombre)
            
            resumen_texto += f"Camion {group_index + 1}:\n"
            resumen_texto += f"  Carga Total: {total_tm} TM\n"
            resumen_texto += f"  Tipo De Vehiculo: {current_vehicle}\n"
            resumen_texto += "   Clientes:\n"
            
            for cliente, pedidos in clientes_pedidos.items():
                resumen_texto += f"     - Nombre de cliente: {cliente}: {', '.join(pedidos)}\n"
            
            resumen_texto += f"\n    Zona: {first_zone}\n\n"
        
        if clientes_sin_coordenadas:
            resumen_texto += "Clientes No representados en el mapa por falta de ubicación:\n"
            for cliente in set(clientes_sin_coordenadas):
                resumen_texto += f"{cliente}\n"
        
        self.ResumenText.setPlainText(resumen_texto)

    

        def plot_customers_by_truck(grouped_deliveries, zona_to_coords):
                # Crear un mapa de colores para los camiones
                trucks = range(len(grouped_deliveries))
                colors = plt.cm.get_cmap('tab20', len(trucks))
                
                # Cargar la imagen del mapa de Venezuela
                img = mpimg.imread('assets\mapa.jpg')
                
                # Graficar clientes por longitud y latitud con el mapa de fondo
                plt.figure(figsize=(10, 6))
                
                plt.imshow(img, extent=[-73.5, -59.8, 0.5, 12.5], aspect='auto')  # Ajusta los límites según el mapa
                
                clientes_sin_coordenadas = []
                
                for truck_index, group in enumerate(grouped_deliveries):
                    truck_color = colors(truck_index)
                    first_zone = str(group[0][6][:3]).zfill(3)
                    
                    for pedido in group:
                        zona = str(pedido[6][:3]).zfill(3)
                        if zona in zona_to_coords:
                            coords = zona_to_coords[zona]
                            plt.scatter(coords[1], coords[0], color=truck_color)
                        else:
                            clientes_sin_coordenadas.append(pedido[4])  # Asumiendo que el nombre del cliente está en la columna 4
                    
                    plt.scatter([], [], color=truck_color, label=f'Camion {truck_index + 1}: Zona {first_zone}')
                
                plt.xlabel('Longitude')
                plt.ylabel('Latitude')
                plt.title('Clientes por Longitud y Latitud')
                plt.legend()
                
                if clientes_sin_coordenadas:
                    plt.figtext(0.5, 0.01, "Clientes No representados en el mapa por falta de ubicación:\n" + "\n".join(set(clientes_sin_coordenadas)), ha="center", fontsize=8, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
                
                plt.show()


        plot_customers_by_truck(grouped_deliveries, zona_to_coords)
        
        self.populate_factura_table()
        camiones = {}
        
        for group_index, group in enumerate(grouped_deliveries):
            unique_zones = set(str(pedido[6][:3]).zfill(3) for pedido in group)
            first_zone = next(iter(unique_zones))

            total_tm = sum(float(pedido[8].replace(',', '.')) for pedido in group)
            clientes = '+ '.join(pedido[0] for pedido in group)
            zonas = ', '.join(unique_zones)  # Crear la cadena de zonas separadas por comas

            # Asignar el vehículo adecuado para el grupo actual
            proveedor, capacidad, tipo_vehiculo = zona_to_proveedor.get(first_zone, (None, None, None))

            # Inicializar variables para tarifa mínima
            current_vehicle = None
            tarifa_usd = float('inf')  # Inicializar como infinito
            mejor_proveedor = None

            # Buscar el vehículo adecuado
            for vehicle in vehicle_list:
                vehicle_tipo, vehicle_capacity = vehicle
                if vehicle_capacity >= total_tm:
                    current_vehicle = vehicle_tipo
                    # Buscar el proveedor más barato para el tipo de vehículo y la zona
                    for (prov, zona, veh), t in tarifa_dict.items():
                        if zona == first_zone and veh == current_vehicle and t < tarifa_usd:
                            tarifa_usd = t
                            mejor_proveedor = prov
                    break  # Salir del bucle una vez encontrado el vehículo adecuado

            # Agregar a camiones con el formato adecuado
            camiones[group_index + 1] = (clientes, current_vehicle, total_tm, first_zone, zonas, tarifa_usd, mejor_proveedor)

        # Agregar filas a la tabla de facturas
        for carro, (clientes, tipo_vehiculo, tm_programadas, zona, zonas, tarifa_usd, proveedor) in camiones.items():
            self.add_row_to_factura_table(carro, clientes, tipo_vehiculo, tm_programadas, zona, zonas, tarifa_usd, proveedor)

        self.ResumenText.setPlainText(resumen_texto)


    def populate_factura_table(self):
        columnas_facturar = ['*', 'Listo', 'Carro', 'Nombre de clientes', 'Tipo de vehiculo', 'Cantidad TM', "Zona", "Zonas", "Tarifa", "Proveedor"]
        
        self.TablaFacturar.setRowCount(0)
        self.TablaFacturar.setColumnCount(len(columnas_facturar))
        self.TablaFacturar.setHorizontalHeaderLabels(columnas_facturar)
        
        self.add_add_button_row()

    def add_empty_row(self):
        row_position = self.TablaFacturar.rowCount() - 1 
        self.TablaFacturar.insertRow(row_position)

        button = QPushButton()
        button.setIcon(QIcon('assets/3punticos.jpg'))
        button.clicked.connect(lambda _, r=row_position: self.on_button_clicked(r))
        self.TablaFacturar.setCellWidget(row_position, 0, button)

        check_box = QCheckBox()
        self.TablaFacturar.setCellWidget(row_position, 1, check_box)

        for col in range(2, self.TablaFacturar.columnCount()):  
            self.TablaFacturar.setItem(row_position, col, QTableWidgetItem(''))

    def add_add_button_row(self):
        # Verificar si ya existe una fila con el botón de "más"
        if self.TablaFacturar.rowCount() == 0 or not isinstance(self.TablaFacturar.cellWidget(self.TablaFacturar.rowCount() - 1, 0), QPushButton):
            row_position = self.TablaFacturar.rowCount()
            self.TablaFacturar.insertRow(row_position)

            add_button = QPushButton()
            add_button.setIcon(QIcon('assets/Mas.png'))
            add_button.setStyleSheet("border: none;")
            
            add_button.clicked.connect(self.add_empty_row)
            self.TablaFacturar.setCellWidget(row_position, 0, add_button)

    def update_add_button_row(self):
        if self.TablaFacturar.rowCount() > 0 and not isinstance(self.TablaFacturar.cellWidget(self.TablaFacturar.rowCount() - 1, 0), QPushButton):
            self.add_add_button_row()

    def on_button_clicked(self, row):
            if row < len(self.factura_data):
                factura = self.factura_data[row]
                if not factura.get('Nombre de clientes') or not factura.get('Zonas'):
                    # Si no tiene datos, crear ventana de detalles vacío
                    print("No hay pedido asignado. Abriendo ventana de detalles vacío.")
                    self.details_window = DetallesPedido({}, self.planificados_data, self)
                else:
                    # Si tiene datos, abrir con esos datos
                    self.details_window = DetallesPedido(factura, self.planificados_data, self)

                self.details_window.setWindowModality(Qt.ApplicationModal) 
                self.details_window.exec()
            else:
                self.details_window = DetallesPedido({}, self.planificados_data, self)
                self.details_window.setWindowModality(Qt.ApplicationModal) 
                self.details_window.exec()

    def add_row_to_factura_table(self, carro, clientes, tipo_vehiculo, tm_programadas, zona,zonas, tarifa_usd, proveedor):
        row_position = self.TablaFacturar.rowCount() - 1
        self.TablaFacturar.insertRow(row_position)

        button = QPushButton()
        button.setIcon(QIcon('assets/3punticos.jpg'))
        button.clicked.connect(lambda _, r=row_position: self.on_button_clicked(r))
        self.TablaFacturar.setCellWidget(row_position, 0, button)

        check_box = QCheckBox()
        self.TablaFacturar.setCellWidget(row_position, 1, check_box)
        print("Datos que se agregarán a la tabla:", carro, clientes, tipo_vehiculo, tm_programadas, zona, zonas, tarifa_usd, proveedor)

        data = {
            'Carro': carro,
            'Nombre de clientes': clientes,
            'Tipo de vehiculo': tipo_vehiculo,
            'Cantidad TM': tm_programadas,
            'Zona': zona,
            "Zonas":zonas, 
            'Tarifa': tarifa_usd,
            'Proveedor': proveedor,
            'Planificador': '',
            'Chofer': '',
            'Cédula': '',
            'Placa': '',
            'Observaciones': '',
            'Zona a pagar': '',
            'Total paletas': '',
            'Parciales': '',
            'Peso sistema': ''
        }

        for col, (key, value) in enumerate(data.items(), start=2):
            self.TablaFacturar.setItem(row_position, col, QTableWidgetItem(str(value)))
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for col in range(self.TablaFacturar.columnCount()):
            item = self.TablaFacturar.item(row_position, col)
            if item:
                item.setBackground(color)
    

        self.factura_data.append(data)
        print("Datos en factura_data:", self.factura_data)


        self.update_add_button_row()

