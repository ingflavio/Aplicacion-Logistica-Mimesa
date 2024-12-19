import os
import sys
from PySide6.QtWidgets import QApplication
from Services.LoginServices import LoginWindos

os.environ["QT_PLUGIN_PATH"] = "C:/Users/ff23107/OneDrive - CARGILL DE VENEZUELA, S.R.L/Desktop/Aplicacion Para Logistica Python/env/Lib/site-packages/PySide6/plugins"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindos()
    login_window.show()    
    sys.exit(app.exec())
