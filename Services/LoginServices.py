from PySide6.QtWidgets import QWidget, QMessageBox
from views.login import Ui_InicioSesion
from Services.CargarArchivosServices import CargarArchivoWindos
import json

class LoginWindos(QWidget, Ui_InicioSesion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aceptar.clicked.connect(self.boton_iniciar)
        
    def boton_iniciar(self):
        selected_user1 = self.comboBox.currentText()
        if selected_user1 in ["Gregory Sevilla", "Ysmeira Floiran"]:
            self.guardar_usuario(selected_user1)
            self.cargar_archivo_window = CargarArchivoWindos()
            self.cargar_archivo_window.show()
            self.close()  
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione un usuario válido.")
                    
    def guardar_usuario(self,selected_user):
        file_path = r".\\repository\\organizador.json"
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Actualizar el usuario seleccionado
        data["selected_user"] = selected_user
        
        # Escribir los cambios de vuelta al archivo JSON
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return data["selected_user"]