# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CargarArchivos.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_CargarArchivo(object):
    def setupUi(self, CargarArchivo):
        if not CargarArchivo.objectName():
            CargarArchivo.setObjectName(u"CargarArchivo")
        CargarArchivo.resize(907, 472)
        palette = QPalette()
        brush = QBrush(QColor(0, 85, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(28, 60, 107, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        CargarArchivo.setPalette(palette)
        CargarArchivo.setStyleSheet(u"")
        self.frame = QFrame(CargarArchivo)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 921, 461))
        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        brush3 = QBrush(QColor(0, 128, 190, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush3)
        brush4 = QBrush(QColor(0, 106, 158, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        brush5 = QBrush(QColor(0, 43, 63, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush5)
        brush6 = QBrush(QColor(0, 57, 85, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 85, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(0, 42, 63, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush10 = QBrush(QColor(255, 255, 255, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(85, 170, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        brush12 = QBrush(QColor(0, 43, 63, 127))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush7)
        self.frame.setPalette(palette1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 461, 31))
        self.BotonStatus = QPushButton(self.frame)
        self.BotonStatus.setObjectName(u"BotonStatus")
        self.BotonStatus.setGeometry(QRect(230, 300, 41, 41))
        self.BotonStatus.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/SubidaDeArchivosIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonStatus.setIcon(icon)
        self.BotonStatus.setIconSize(QSize(35, 35))
        self.BotonStatus.setFlat(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 120, 301, 41))
        self.StatusLine = QLineEdit(self.frame)
        self.StatusLine.setObjectName(u"StatusLine")
        self.StatusLine.setGeometry(QRect(60, 310, 161, 22))
        self.StatusLine.setStyleSheet(u"QLineEdit {\n"
"        background-color: #f0f0f0;  /* Color de fondo */\n"
"        color: #333333;              /* Color del texto */\n"
"\n"
"    }\n"
"    \n"
"    QLineEdit:focus {\n"
"        border: 1px solid #0069c0;   /* Borde cuando est\u00e1 enfocado */\n"
"        background-color: #ffffff;   /* Color de fondo cuando est\u00e1 enfocado */\n"
"    }")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 170, 111, 121))
        self.label_3.setPixmap(QPixmap(u"./assets/ArchivoExcelSubida.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 115, 231, 51))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 170, 111, 121))
        self.label_5.setPixmap(QPixmap(u"./assets/ArchivoExcelSubida.png"))
        self.label_5.setScaledContents(True)
        self.BotonInventario = QPushButton(self.frame)
        self.BotonInventario.setObjectName(u"BotonInventario")
        self.BotonInventario.setGeometry(QRect(510, 300, 41, 41))
        self.BotonInventario.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        self.BotonInventario.setIcon(icon)
        self.BotonInventario.setIconSize(QSize(35, 35))
        self.BotonInventario.setFlat(True)
        self.InventarioLine = QLineEdit(self.frame)
        self.InventarioLine.setObjectName(u"InventarioLine")
        self.InventarioLine.setGeometry(QRect(340, 310, 161, 22))
        self.InventarioLine.setStyleSheet(u"QLineEdit {\n"
"        background-color: #f0f0f0;  /* Color de fondo */\n"
"        color: #333333;              /* Color del texto */\n"
"\n"
"    }\n"
"    \n"
"    QLineEdit:focus {\n"
"        border: 1px solid #0069c0;   /* Borde cuando est\u00e1 enfocado */\n"
"        background-color: #ffffff;   /* Color de fondo cuando est\u00e1 enfocado */\n"
"    }")
        self.BotonAceptar = QPushButton(self.frame)
        self.BotonAceptar.setObjectName(u"BotonAceptar")
        self.BotonAceptar.setGeometry(QRect(350, 390, 161, 51))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush13 = QBrush(QColor(148, 193, 30, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush13)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonAceptar.setPalette(palette2)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.BotonAceptar.setFont(font)
        self.BotonAceptar.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        self.BotonPLanDay = QPushButton(self.frame)
        self.BotonPLanDay.setObjectName(u"BotonPLanDay")
        self.BotonPLanDay.setGeometry(QRect(790, 300, 41, 41))
        self.BotonPLanDay.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")    
        self.BotonPLanDay.setIcon(icon)
        self.BotonPLanDay.setIconSize(QSize(35, 35))
        self.BotonPLanDay.setFlat(True)
        self.PlanDayLine = QLineEdit(self.frame)
        self.PlanDayLine.setObjectName(u"PlanDayLine")
        self.PlanDayLine.setGeometry(QRect(620, 310, 161, 22))
        self.PlanDayLine.setStyleSheet(u"QLineEdit {\n"
"        background-color: #f0f0f0;  /* Color de fondo */\n"
"        color: #333333;              /* Color del texto */\n"
"\n"
"    }\n"
"    \n"
"    QLineEdit:focus {\n"
"        border: 1px solid #0069c0;   /* Borde cuando est\u00e1 enfocado */\n"
"        background-color: #ffffff;   /* Color de fondo cuando est\u00e1 enfocado */\n"
"    }")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(650, 170, 111, 121))
        self.label_6.setPixmap(QPixmap(u"./assets/ArchivoExcelSubida.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(590, 120, 251, 41))

        self.retranslateUi(CargarArchivo)

        QMetaObject.connectSlotsByName(CargarArchivo)
    # setupUi

    def retranslateUi(self, CargarArchivo):
        CargarArchivo.setWindowTitle(QCoreApplication.translate("CargarArchivo", u"Cargar Archivos", None))
        self.label.setText(QCoreApplication.translate("CargarArchivo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Carga Los Archivos De Compras Y Inventario</span></p></body></html>", None))
        self.BotonStatus.setText("")
        self.label_2.setText(QCoreApplication.translate("CargarArchivo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">ESTATUS DE PEDIDOS</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("CargarArchivo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">INVENTARIO</span></p></body></html>", None))
        self.label_5.setText("")
        self.BotonInventario.setText("")
        self.BotonAceptar.setText(QCoreApplication.translate("CargarArchivo", u"Siguiente", None))
        self.BotonPLanDay.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("CargarArchivo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">PLAN DEL DIA</span></p></body></html>", None))
    # retranslateUi

