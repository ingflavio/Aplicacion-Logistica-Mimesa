from PySide6.QtWidgets import QWidget, QFileDialog, QPushButton, QLineEdit, QMessageBox
from views.CargarArchivos import Ui_CargarArchivo
from Services.PlanificacionServices import PlanificacionServices
import json
class CargarArchivoWindos(QWidget, Ui_CargarArchivo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ruta_status = ""
        self.ruta_inventario = ""
        self.ruta_planday = ""
        self.BotonStatus = self.findChild(QPushButton, "BotonStatus")
        self.BotonInventario = self.findChild(QPushButton, "BotonInventario")
        self.BotonPLanDay = self.findChild(QPushButton, "BotonPLanDay")
        self.BotonAceptar = self.findChild(QPushButton, "BotonAceptar")  
        self.StatusLine = self.findChild(QLineEdit, "StatusLine")
        self.InventarioLine = self.findChild(QLineEdit, "InventarioLine")
        self.PlanDayLine = self.findChild(QLineEdit, "PlanDayLine")
        self.BotonStatus.clicked.connect(self.abrir_dialogo_archivo_status)
        self.BotonInventario.clicked.connect(self.abrir_dialogo_archivo_inventario)
        self.BotonPLanDay.clicked.connect(self.abrir_dialogo_archivo_planday)
        self.BotonAceptar.clicked.connect(self.abrir_nueva_ventana)
        self.urlRutasExcel=r'.\repository\ruta_excels.json'  
       
        

    def abrir_dialogo_archivo_status(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de status", "", "Archivos de Excel (*.xls *.xlsx)")

        if file_path:
            self.ruta_status = file_path
            self.StatusLine.setText(file_path)

    def abrir_dialogo_archivo_inventario(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de inventario", "", "Archivos de Excel (*.xls *.xlsx)")
        if file_path:
            self.ruta_inventario = file_path
            self.InventarioLine.setText(file_path)

    def abrir_dialogo_archivo_planday(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de PlanDay", "", "Archivos de Excel (*.xls *.xlsx)")
        if file_path:
            self.ruta_planday = file_path
            self.PlanDayLine.setText(file_path)

    def abrir_nueva_ventana(self):
        if not self.ruta_status or not self.ruta_inventario or not self.ruta_planday:
            QMessageBox.warning(self, "Advertencia", "Debe cargar todos los de pedidos antes de continuar.")
        else:
            self.nueva_ventana = PlanificacionServices(self.ruta_status, self.ruta_planday, self.ruta_inventario) 
            # self.nueva_ventana = PruebaTablaWindos(self.ruta_status, self.ruta_planday, self.ruta_inventario)

            # Datos a guardar en el JSON
            datosJson = {
                "Status": self.ruta_status,
                "Inventario": self.ruta_inventario,
                "PlayDay": self.ruta_planday
            }

            try:
                # Borrar el contenido anterior del archivo y crear una lista vacía
                with open(self.urlRutasExcel, 'w') as file:
                    file.truncate(0)  # Borra el contenido del archivo
                    
                # Leer datos existentes y agregar nuevos
                with open(self.urlRutasExcel, 'r') as file:
                    contenido = file.read()
                    if contenido:
                        datos_existentes = json.loads(contenido)
                    else:
                        datos_existentes = []
            except (FileNotFoundError, json.JSONDecodeError):
                # Si no existe el archivo o no tiene un formato JSON válido, inicializar como lista vacía
                datos_existentes = []

            # Agregar los nuevos datos
            datos_existentes.append(datosJson)

            # Guardar los datos actualizados en el archivo JSON
            with open(self.urlRutasExcel, 'w') as file:
                json.dump(datos_existentes, file, indent=4)

            # Mostrar la nueva ventana
            self.nueva_ventana.show()
            self.close()

            

            
            
