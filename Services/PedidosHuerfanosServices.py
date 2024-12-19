from PySide6.QtWidgets import QWidget
from views.DetallesPedido import Ui_Pedido
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox,QCheckBox
from PySide6.QtGui import QColor
import random
import re
from views.PedidosHuerfano import Ui_Form
from PySide6.QtWidgets import QDialog
import json
import os

class PedidosHuerfano (QDialog, Ui_Form):
    def __init__(self,row, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.row= row
        self.url_DatosDePedidos= r'.\repository\DatosDePedidos.json'
        self.url_Pedidos= r'.\repository\Pedidos.json'
        self.populate_table()
        self.BotonMas_2.clicked.connect(self.agregar_un_pedido)
        self.BotonListo_2.clicked.connect(self.Listo)
        

    
    def populate_table(self):
        columnas_deseadas = ['Nombre Cliente', 'Fecha de la Cita', 'Numero de Pedido', 'Codigo Cliente', 
                            'Codigo SKU', 'Descripcion SKU', 'Zona de Entrega', 'Cant. Programada', 
                            'TM Programadas', 'Total paletas']
        self.PedidosHuerfanos.setColumnCount(len(columnas_deseadas))
        self.PedidosHuerfanos.setHorizontalHeaderLabels(columnas_deseadas)

        # Leer el archivo JSON
        with open(self.url_Pedidos, 'r', encoding='utf-8') as file:
            data = json.load(file)
            pedidos_no_planificados = data.get("PedidosNoPlanificados", [])

        # Llenar la tabla con los datos
        self.PedidosHuerfanos.setRowCount(len(pedidos_no_planificados))
        for row_index, pedido in enumerate(pedidos_no_planificados):
            for col_index, columna in enumerate(columnas_deseadas):
                item = QTableWidgetItem(pedido.get(columna, ""))
                self.PedidosHuerfanos.setItem(row_index, col_index, item)
        
        # Obtener zonas únicas de la columna "Zona de Entrega" (índice 6)
        zonas_unicas = set()
        for row_idx in range(self.PedidosHuerfanos.rowCount()):
            item = self.PedidosHuerfanos.item(row_idx, 6)  # Columna 6 (Zona de Entrega)
            if item:
                zonas_unicas.add(item.text())  # Añadir el texto si el item no es None

        # Crear un diccionario de colores para cada zona única
        colores_zonas = {zona: self.generar_color() for zona in zonas_unicas}

        # Ahora iteramos sobre las filas y columnas de la tabla para aplicar colores a las zonas
        for row_idx in range(self.PedidosHuerfanos.rowCount()):
            row_data = []
            for col_idx in range(self.PedidosHuerfanos.columnCount()):
                # Obtenemos el valor de la celda
                item = self.PedidosHuerfanos.item(row_idx, col_idx)
                value = item.text() if item else ''
                row_data.append(value)  # Añadimos el valor a row_data

            # Aquí ya tienes la fila con todos los datos
            zona_entrega = row_data[6]  # La zona está en la columna 6 (índice 6)

            # Si la zona tiene un color asignado, lo aplicamos
            if zona_entrega in colores_zonas:
                color = colores_zonas[zona_entrega]
                for col in range(self.PedidosHuerfanos.columnCount()):
                    item = self.PedidosHuerfanos.item(row_idx, col)
                    if item:  # Asegúrate de que el item no sea None
                        item.setBackground(color)  # Aplicamos el color a cada celda de la fila


    def agregar_un_pedido(self):
        selected_row = self.PedidosHuerfanos.currentRow()    
        if selected_row < 0:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para sacar.")
            return

        # Obtener los datos de la fila seleccionada
        fila_datos = {}
        for column in range(self.PedidosHuerfanos.columnCount()):
            header = self.PedidosHuerfanos.horizontalHeaderItem(column).text()
            item = self.PedidosHuerfanos.item(selected_row, column)
            fila_datos[header] = item.text() if item else ""

        self.Guardar_json_Planificado(fila_datos)
        self.PedidosHuerfanos.removeRow(selected_row)
     
    def Guardar_json_Planificado(self, fila_datos):
        # Abrir el archivo JSON para cargar los datos
        with open(self.url_Pedidos, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            
        with open(self.url_DatosDePedidos, 'r', encoding='utf-8') as file:
            data2 = json.load(file)
        
        # Obtener las listas de PedidosNoPlanificados y PedidosPlanificados
        pedidos_no_planificados = data.get("PedidosNoPlanificados", [])
        pedidos_planificados = data.get("PedidosPlanificados", [])
        # Buscar el pedido en PedidosNoPlanificados y eliminarlo
        pedido_a_transferir = None
        for pedido in pedidos_no_planificados:
            if pedido == fila_datos:
                pedido_a_transferir = pedido
                break

        # Si se encontró el pedido, lo eliminamos de PedidosNoPlanificados
        if pedido_a_transferir:
            pedidos_no_planificados.remove(pedido_a_transferir)
            # Lo agregamos a PedidosPlanificados
            pedidos_planificados.append(pedido_a_transferir)
            carro_encontrado = False
            for carro in data2:
                if carro['Carro'] == self.row:
                    carro['Informacion']['Pedidos'].append(pedido_a_transferir)
                    break

            # Guardamos el archivo JSON actualizado
            with open(self.url_Pedidos, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)    
         # Guardamos el archivo JSON actualizado
            with open(self.url_DatosDePedidos, 'w', encoding='utf-8') as file:
                json.dump(data2, file, indent=4, ensure_ascii=False)
          
        else:

            pass

        
    def Listo(self):
   
        file_path = r'.\repository\bandera.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                datos = json.load(file)
        except FileNotFoundError:
            datos = {}

        datos['bandera'] = 1

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(datos, file, ensure_ascii=False, indent=4)
        self.close()

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