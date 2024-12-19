# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PruebaTabla.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_TodosPedidos(object):
    def setupUi(self, TodosPedidos):
        if not TodosPedidos.objectName():
            TodosPedidos.setObjectName(u"TodosPedidos")
        TodosPedidos.setEnabled(True)
        TodosPedidos.resize(1694, 981)
        TodosPedidos.setMinimumSize(QSize(1279, 981))
        TodosPedidos.setBaseSize(QSize(1279, 981))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(28, 60, 107, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        TodosPedidos.setPalette(palette)
        self.frame = QFrame(TodosPedidos)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(-10, 10, 1621, 971))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(0, 85, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
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
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
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
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
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
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
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
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(30, 90, 1231, 361))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    margin: 10px;\n"
"    font-family: 'Arial';  \n"
"    font-size: 10pt;  \n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #1c3c6b; \n"
"    color: #ffffff;\n"
"    padding: 4px;\n"
"    border: 1px solid #aaa;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #f0f0f0;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #04943b;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"\n"
"   QScrollBar:horizontal {\n"
"        height: 12px;\n"
"        background: #04943b ;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"        background: #04943b ;\n"
"        border-radius: 6px;\n"
"    }\n"
"    QScrollBar::add-line:horizontal,\n"
" QScrollBar::sub-line:horizontal {\n"
"        background: none;\n"
"    }\n"
"\n"
"")
        self.tableWidget.setGridStyle(Qt.PenStyle.DashLine)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(800, 20, 151, 61))
        palette2 = QPalette()
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush14 = QBrush(QColor(127, 127, 127, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(170, 170, 170, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
        brush16 = QBrush(QColor(0, 0, 0, 127))
        brush16.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
        brush17 = QBrush(QColor(127, 127, 127, 127))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label.setPalette(palette2)
        self.label.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(950, 30, 161, 51))
        self.comboBox.setStyleSheet(u" QComboBox {\n"
"                background-color: #94cc1c  ;\n"
"                border: 1px solid #ccc;\n"
"                padding: 5px;\n"
"                margin: 10px;\n"
"				color: white; \n"
"                font-family: Arial; /* Fuente */\n"
"                font-size: 14px; /* Tama\u00f1o de la fuente */\n"
"				\n"
"\n"
"            }\n"
"            QComboBox QAbstractItemView {\n"
"                background-color: #1c3c6b ;\n"
"                border: 1px solid #ccc;\n"
"                padding: 5px;\n"
"				color: white; \n"
"                font-family: Arial; /* Fuente */\n"
"                font-size: 14px; /* Tama\u00f1o de la fuente */\n"
"            }\n"
"            QComboBox::drop-down {\n"
"                border: 1px solid #1c3c6b  ;\n"
"                background-color: #1c3c6b  ;\n"
"            }")
        self.TablaPlanificado = QTableWidget(self.frame)
        self.TablaPlanificado.setObjectName(u"TablaPlanificado")
        self.TablaPlanificado.setEnabled(True)
        self.TablaPlanificado.setGeometry(QRect(30, 500, 1231, 361))
        self.TablaPlanificado.setFont(font)
        self.TablaPlanificado.setStyleSheet(u"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    margin: 10px;\n"
"    font-family: 'Arial';  \n"
"    font-size: 10pt;  \n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #1c3c6b; \n"
"    color: #ffffff;\n"
"    padding: 4px;\n"
"    border: 1px solid #aaa;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #f0f0f0;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #04943b;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"\n"
"   QScrollBar:horizontal {\n"
"        height: 12px;\n"
"        background: #04943b ;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"        background: #04943b ;\n"
"        border-radius: 6px;\n"
"    }\n"
"    QScrollBar::add-line:horizontal,\n"
" QScrollBar::sub-line:horizontal {\n"
"        background: none;\n"
"    }\n"
"\n"
"")
        self.TablaPlanificado.setGridStyle(Qt.PenStyle.DashLine)
        self.Enrutar = QPushButton(self.frame)
        self.Enrutar.setObjectName(u"Enrutar")
        self.Enrutar.setGeometry(QRect(1100, 860, 151, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.Enrutar.setFont(font1)
        self.Enrutar.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 860, 381, 61))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label_2.setPalette(palette3)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.AgregarCargamento = QPushButton(self.frame)
        self.AgregarCargamento.setObjectName(u"AgregarCargamento")
        self.AgregarCargamento.setGeometry(QRect(490, 450, 61, 51))
        self.AgregarCargamento.setFont(font1)
        self.AgregarCargamento.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/flecha pa abajo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AgregarCargamento.setIcon(icon)
        self.AgregarCargamento.setIconSize(QSize(55, 55))
        self.AgregarCargamento.setFlat(True)
        self.SacarCargamento = QPushButton(self.frame)
        self.SacarCargamento.setObjectName(u"SacarCargamento")
        self.SacarCargamento.setGeometry(QRect(690, 450, 61, 51))
        self.SacarCargamento.setFont(font1)
        self.SacarCargamento.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/flecha pa arriba.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SacarCargamento.setIcon(icon1)
        self.SacarCargamento.setIconSize(QSize(55, 55))
        self.SacarCargamento.setFlat(True)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 450, 241, 61))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label_3.setPalette(palette4)
        self.label_3.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 191, 61))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette5.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label_5.setPalette(palette5)
        self.label_5.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.plainTextEdit = QLineEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(1120, 40, 113, 31))
        self.plainTextEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0; /* Color de fondo */\n"
"    border: 2px solid #4CAF50; /* Borde */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    color: #333; /* Color del texto */\n"
"    font-size: 14px; /* Tama\u00f1o de la fuente */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FF5722; /* Borde al tener foco */\n"
"    background-color: #ffffff; /* Cambiar color de fondo al tener foco */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #999; /* Color del texto del placeholder */\n"
"    font-style: italic; /* Estilo del texto del placeholder */\n"
"}\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 860, 161, 61))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette6.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.label_4.setPalette(palette6)
        font3 = QFont()
        font3.setPointSize(18)
        self.label_4.setFont(font3)
        self.label_4.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.botontodo = QPushButton(self.frame)
        self.botontodo.setObjectName(u"botontodo")
        self.botontodo.setGeometry(QRect(1170, 450, 75, 51))
        icon2 = QIcon()
        icon2.addFile(u"./assets/botonBajarTodo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botontodo.setIcon(icon2)
        self.botontodo.setIconSize(QSize(45, 45))
        self.botontodo.setFlat(True)
        self.BotonPorcentaje = QPushButton(self.frame)
        self.BotonPorcentaje.setObjectName(u"BotonPorcentaje")
        self.BotonPorcentaje.setGeometry(QRect(560, 450, 111, 51))
        icon3 = QIcon()
        icon3.addFile(u"./assets/ojoTabla.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonPorcentaje.setIcon(icon3)
        self.BotonPorcentaje.setIconSize(QSize(45, 45))
        self.BotonPorcentaje.setFlat(True)
        self.TablaPorcentaje = QTableWidget(self.frame)
        if (self.TablaPorcentaje.columnCount() < 5):
            self.TablaPorcentaje.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TablaPorcentaje.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TablaPorcentaje.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TablaPorcentaje.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TablaPorcentaje.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TablaPorcentaje.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.TablaPorcentaje.setObjectName(u"TablaPorcentaje")
        self.TablaPorcentaje.setEnabled(True)
        self.TablaPorcentaje.setGeometry(QRect(220, 510, 811, 351))
#if QT_CONFIG(statustip)
        self.TablaPorcentaje.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.TablaPorcentaje.setAutoFillBackground(False)
        self.TablaPorcentaje.setStyleSheet(u"QTableWidget {\n"
"    background-color: transparent;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    margin: 10px;\n"
"    font-family: 'Arial';  \n"
"    font-size: 10pt;  \n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #1c3c6b; \n"
"    color: #ffffff;\n"
"    padding: 4px;\n"
"    border: 1px solid #aaa;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #f0f0f0;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #04943b;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"\n"
"   QScrollBar:horizontal {\n"
"        height: 12px;\n"
"        background: #04943b ;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"        background: #04943b ;\n"
"        border-radius: 6px;\n"
"    }\n"
"    QScrollBar::add-line:horizontal,\n"
" QScrollBar::sub-line:horizontal {\n"
"        background: none;\n"
"    }\n"
"\n"
"")
        self.TablaPorcentaje.setDragEnabled(False)
        self.TablaPorcentaje.setShowGrid(True)
        self.LabelPaletas = QLabel(self.frame)
        self.LabelPaletas.setObjectName(u"LabelPaletas")
        self.LabelPaletas.setGeometry(QRect(460, 860, 411, 61))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette7.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.LabelPaletas.setPalette(palette7)
        self.LabelPaletas.setFont(font2)
        self.LabelPaletas.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.LabelPaletas.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")

        self.retranslateUi(TodosPedidos)

        QMetaObject.connectSlotsByName(TodosPedidos)
    # setupUi

    def retranslateUi(self, TodosPedidos):
        TodosPedidos.setWindowTitle(QCoreApplication.translate("TodosPedidos", u"Todos Los Pedidos", None))
        self.label.setText(QCoreApplication.translate("TodosPedidos", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Filtrar Por: </span></p></body></html>", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("TodosPedidos", u"Fecha de la Cita", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("TodosPedidos", u"Codigo SKU", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("TodosPedidos", u"Status", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("TodosPedidos", u"Numero de Pedido", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("TodosPedidos", u"Nombre Cliente", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("TodosPedidos", u"Codigo Cliente", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("TodosPedidos", u"Zona de Entrega", None))

        self.Enrutar.setText(QCoreApplication.translate("TodosPedidos", u"EnRutar", None))
        self.label_2.setText(QCoreApplication.translate("TodosPedidos", u"<html><head/><body><p><br/></p></body></html>", None))
        self.AgregarCargamento.setText("")
        self.SacarCargamento.setText("")
        self.label_3.setText(QCoreApplication.translate("TodosPedidos", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Nuevo Despacho</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("TodosPedidos", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Carga Del Dia</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("TodosPedidos", u"<html><head/><body><p><br/></p></body></html>", None))
        self.botontodo.setText("")
        self.BotonPorcentaje.setText("")
        ___qtablewidgetitem = self.TablaPorcentaje.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TodosPedidos", u"Codigo SKU", None));
        ___qtablewidgetitem1 = self.TablaPorcentaje.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TodosPedidos", u"Descripcion SKU", None));
        ___qtablewidgetitem2 = self.TablaPorcentaje.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TodosPedidos", u"Cant. P", None));
        ___qtablewidgetitem3 = self.TablaPorcentaje.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TodosPedidos", u"TM Programadas", None));
        ___qtablewidgetitem4 = self.TablaPorcentaje.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TodosPedidos", u"%", None));
#if QT_CONFIG(whatsthis)
        self.TablaPorcentaje.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.LabelPaletas.setText(QCoreApplication.translate("TodosPedidos", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

