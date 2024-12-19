# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetallesPedido.ui'
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

class Ui_Pedido(object):
    def setupUi(self, Pedido):
        if not Pedido.objectName():
            Pedido.setObjectName(u"Pedido")
        Pedido.resize(1289, 1039)
        palette = QPalette()
        brush = QBrush(QColor(28, 60, 107, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Pedido.setPalette(palette)
        self.frame = QFrame(Pedido)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 20, 1301, 1031))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.TablaDetalles = QTableWidget(self.frame)
        self.TablaDetalles.setObjectName(u"TablaDetalles")
        self.TablaDetalles.setGeometry(QRect(10, 50, 1101, 481))
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.TablaDetalles.setPalette(palette1)
        self.TablaDetalles.setStyleSheet(u"QTableWidget {\n"
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
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 0, 251, 61))
        palette2 = QPalette()
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(127, 127, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush7)
        brush8 = QBrush(QColor(170, 170, 170, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush10 = QBrush(QColor(0, 0, 0, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
        brush11 = QBrush(QColor(127, 127, 127, 127))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_5.setPalette(palette2)
        self.label_5.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 550, 211, 61))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_6.setPalette(palette3)
        self.label_6.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.Planificador = QLineEdit(self.frame)
        self.Planificador.setObjectName(u"Planificador")
        self.Planificador.setEnabled(False)
        self.Planificador.setGeometry(QRect(10, 610, 171, 31))
        self.Planificador.setStyleSheet(u"QLineEdit {\n"
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
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 550, 151, 61))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_7.setPalette(palette4)
        self.label_7.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(530, 550, 191, 61))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_8.setPalette(palette5)
        self.label_8.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.Chofer = QLineEdit(self.frame)
        self.Chofer.setObjectName(u"Chofer")
        self.Chofer.setGeometry(QRect(10, 710, 171, 31))
        self.Chofer.setStyleSheet(u"QLineEdit {\n"
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
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 660, 111, 41))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_9.setPalette(palette6)
        self.label_9.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.Cedula = QLineEdit(self.frame)
        self.Cedula.setObjectName(u"Cedula")
        self.Cedula.setGeometry(QRect(260, 710, 171, 31))
        self.Cedula.setStyleSheet(u"QLineEdit {\n"
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
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(295, 660, 111, 41))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_10.setPalette(palette7)
        self.label_10.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.Placa = QLineEdit(self.frame)
        self.Placa.setObjectName(u"Placa")
        self.Placa.setGeometry(QRect(510, 710, 171, 31))
        self.Placa.setStyleSheet(u"QLineEdit {\n"
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
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(545, 660, 111, 41))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette8.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_11.setPalette(palette8)
        self.label_11.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_11.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(810, 660, 221, 41))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette9.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_12.setPalette(palette9)
        self.label_12.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_12.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.Observaciones = QLineEdit(self.frame)
        self.Observaciones.setObjectName(u"Observaciones")
        self.Observaciones.setGeometry(QRect(760, 710, 331, 31))
        self.Observaciones.setStyleSheet(u"QLineEdit {\n"
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
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(910, 770, 161, 41))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette10.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_13.setPalette(palette10)
        self.label_13.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.TMtotales = QLineEdit(self.frame)
        self.TMtotales.setObjectName(u"TMtotales")
        self.TMtotales.setEnabled(False)
        self.TMtotales.setGeometry(QRect(910, 820, 161, 31))
        self.TMtotales.setStyleSheet(u"QLineEdit {\n"
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
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 770, 201, 41))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette11.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_14.setPalette(palette11)
        self.label_14.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.ZonaApagar = QLineEdit(self.frame)
        self.ZonaApagar.setObjectName(u"ZonaApagar")
        self.ZonaApagar.setGeometry(QRect(0, 820, 201, 31))
        self.ZonaApagar.setStyleSheet(u"QLineEdit {\n"
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
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(250, 770, 201, 41))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette12.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_15.setPalette(palette12)
        self.label_15.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_15.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(500, 770, 191, 41))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette13.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_17.setPalette(palette13)
        self.label_17.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(730, 770, 141, 41))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette14.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_18.setPalette(palette14)
        self.label_18.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.TotalPaletas = QLineEdit(self.frame)
        self.TotalPaletas.setObjectName(u"TotalPaletas")
        self.TotalPaletas.setGeometry(QRect(250, 820, 201, 31))
        self.TotalPaletas.setStyleSheet(u"QLineEdit {\n"
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
        self.PesoSistema = QLineEdit(self.frame)
        self.PesoSistema.setObjectName(u"PesoSistema")
        self.PesoSistema.setGeometry(QRect(530, 820, 121, 31))
        self.PesoSistema.setStyleSheet(u"QLineEdit {\n"
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
        self.PesoReal = QLineEdit(self.frame)
        self.PesoReal.setObjectName(u"PesoReal")
        self.PesoReal.setGeometry(QRect(730, 820, 141, 31))
        self.PesoReal.setStyleSheet(u"QLineEdit {\n"
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
        self.TipoVehi = QComboBox(self.frame)
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.addItem("")
        self.TipoVehi.setObjectName(u"TipoVehi")
        self.TipoVehi.setGeometry(QRect(200, 600, 301, 51))
        self.TipoVehi.setStyleSheet(u" QComboBox {\n"
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
        self.Provedor = QComboBox(self.frame)
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.addItem("")
        self.Provedor.setObjectName(u"Provedor")
        self.Provedor.setGeometry(QRect(510, 600, 241, 51))
        self.Provedor.setStyleSheet(u" QComboBox {\n"
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
        self.BotonMas = QPushButton(self.frame)
        self.BotonMas.setObjectName(u"BotonMas")
        self.BotonMas.setGeometry(QRect(1120, 180, 91, 81))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush12 = QBrush(QColor(148, 193, 30, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush13 = QBrush(QColor(85, 170, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush12)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonMas.setPalette(palette15)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.BotonMas.setFont(font)
        self.BotonMas.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/botonMas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonMas.setIcon(icon)
        self.BotonMas.setIconSize(QSize(75, 75))
        self.BotonMas.setFlat(True)
        self.BotonMenos = QPushButton(self.frame)
        self.BotonMenos.setObjectName(u"BotonMenos")
        self.BotonMenos.setGeometry(QRect(1120, 270, 91, 81))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonMenos.setPalette(palette16)
        self.BotonMenos.setFont(font)
        self.BotonMenos.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/BotonNegativo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonMenos.setIcon(icon1)
        self.BotonMenos.setIconSize(QSize(75, 75))
        self.BotonMenos.setFlat(True)
        self.BotonListo = QPushButton(self.frame)
        self.BotonListo.setObjectName(u"BotonListo")
        self.BotonListo.setGeometry(QRect(1120, 360, 91, 81))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonListo.setPalette(palette17)
        self.BotonListo.setFont(font)
        self.BotonListo.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assets/BotonListo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonListo.setIcon(icon2)
        self.BotonListo.setIconSize(QSize(110, 110))
        self.BotonListo.setFlat(True)
        self.Tarifa = QLineEdit(self.frame)
        self.Tarifa.setObjectName(u"Tarifa")
        self.Tarifa.setGeometry(QRect(780, 610, 141, 31))
        self.Tarifa.setStyleSheet(u"QLineEdit {\n"
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
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(800, 550, 101, 61))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette18.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.Accent, brush6)
        self.label_16.setPalette(palette18)
        self.label_16.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")

        self.retranslateUi(Pedido)

        QMetaObject.connectSlotsByName(Pedido)
    # setupUi

    def retranslateUi(self, Pedido):
        Pedido.setWindowTitle(QCoreApplication.translate("Pedido", u"Detalles Del Pedido", None))
        self.label_5.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Carga Del Camion</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">PLANIFICADOR</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">VEH\u00cdCULO</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">TRANSPORTE</span></p></body></html>", None))
        self.Chofer.setText("")
        self.label_9.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">CHOFER</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">CEDULA</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">PLACA</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">OBSERVACIONES</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">TM TOTALES </span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">ZONA A PAGAR</span></p></body></html>", None))
        self.ZonaApagar.setText("")
        self.label_15.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">TOTAL PALETAS</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">PESO SISTEMA</span></p><p><br/></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">PESO REAL</span></p><p><br/></p></body></html>", None))
        self.TotalPaletas.setText("")
        self.PesoSistema.setText("")
        self.PesoReal.setText("")
        self.TipoVehi.setItemText(0, QCoreApplication.translate("Pedido", u"CM PANEL CAP 500KG", None))
        self.TipoVehi.setItemText(1, QCoreApplication.translate("Pedido", u"CM PICKUP 150. CAP. 700 KG", None))
        self.TipoVehi.setItemText(2, QCoreApplication.translate("Pedido", u"CM PICKUP 250 CAP. 900 KG", None))
        self.TipoVehi.setItemText(3, QCoreApplication.translate("Pedido", u"CM PANEL 1100 CAP. 1100 KG", None))
        self.TipoVehi.setItemText(4, QCoreApplication.translate("Pedido", u"CM CAMION 350 CAP. 2800 KG", None))
        self.TipoVehi.setItemText(5, QCoreApplication.translate("Pedido", u"CM CAMION 350 A GASOLINA CAP. 2800 KG", None))
        self.TipoVehi.setItemText(6, QCoreApplication.translate("Pedido", u"CM MITSUBISHI FK 44 CAP. 3800 KG", None))
        self.TipoVehi.setItemText(7, QCoreApplication.translate("Pedido", u"CM DINA SUPER DUTTY CAP. 4200 KG", None))
        self.TipoVehi.setItemText(8, QCoreApplication.translate("Pedido", u"CM DINA FE CAP.5000 KG", None))
        self.TipoVehi.setItemText(9, QCoreApplication.translate("Pedido", u"CM DINA D9 CAP. 5900 KG", None))
        self.TipoVehi.setItemText(10, QCoreApplication.translate("Pedido", u"CM CAMION 600 CAP. 6000 KG", None))
        self.TipoVehi.setItemText(11, QCoreApplication.translate("Pedido", u"CM CAMION 750 CAP. 8000 KG", None))
        self.TipoVehi.setItemText(12, QCoreApplication.translate("Pedido", u"CM CAMION 7000 CAP. 8000 KG", None))
        self.TipoVehi.setItemText(13, QCoreApplication.translate("Pedido", u"CM KODIAK CAP. 9000 KG", None))
        self.TipoVehi.setItemText(14, QCoreApplication.translate("Pedido", u"CAMION 10000", None))
        self.TipoVehi.setItemText(15, QCoreApplication.translate("Pedido", u"CM CAMION 800 CAP. 12000 KG", None))
        self.TipoVehi.setItemText(16, QCoreApplication.translate("Pedido", u"TORONTO", None))
        self.TipoVehi.setItemText(17, QCoreApplication.translate("Pedido", u"GANDOLAS 4 EJES", None))
        self.TipoVehi.setItemText(18, QCoreApplication.translate("Pedido", u"GANDOLA 5 ejes", None))
        self.TipoVehi.setItemText(19, QCoreApplication.translate("Pedido", u"GANDOLA 6 ejes", None))
        self.TipoVehi.setItemText(20, QCoreApplication.translate("Pedido", u"TANQUE GRANEL", None))

        self.Provedor.setItemText(0, "")
        self.Provedor.setItemText(1, QCoreApplication.translate("Pedido", u"SERVICIOS P.G.M, C.A", None))
        self.Provedor.setItemText(2, QCoreApplication.translate("Pedido", u"MULTISERVICIOS JD-JR 2018, C.A", None))
        self.Provedor.setItemText(3, QCoreApplication.translate("Pedido", u"TRANSPORTE GAMA C.A", None))
        self.Provedor.setItemText(4, QCoreApplication.translate("Pedido", u"SOLUCIONES DE TRANSPORTE DINSA, C.A", None))
        self.Provedor.setItemText(5, QCoreApplication.translate("Pedido", u"TRANSERAL, C .A", None))
        self.Provedor.setItemText(6, QCoreApplication.translate("Pedido", u"TRANSPORTE 1DA, C.A.", None))
        self.Provedor.setItemText(7, QCoreApplication.translate("Pedido", u"SERVICIOS LOGISTICOS CENTROANDES,C.A", None))
        self.Provedor.setItemText(8, QCoreApplication.translate("Pedido", u"TRANSPORTE CATAURE, C.A.", None))
        self.Provedor.setItemText(9, QCoreApplication.translate("Pedido", u"MULTITRANSPORTE OCEANICA EXPORT1,C.A", None))
        self.Provedor.setItemText(10, QCoreApplication.translate("Pedido", u"TRANSPORTE TRAVEL TRUCK 2012, C.A", None))
        self.Provedor.setItemText(11, QCoreApplication.translate("Pedido", u"TRANSPORTE MANZANO 23-25-13,C.A.", None))
        self.Provedor.setItemText(12, QCoreApplication.translate("Pedido", u"TRANSPORTE S.T.I. C.A", None))
        self.Provedor.setItemText(13, QCoreApplication.translate("Pedido", u"GAMA FLETES, C.A.", None))
        self.Provedor.setItemText(14, QCoreApplication.translate("Pedido", u"SERVIENVIA, C.A", None))
        self.Provedor.setItemText(15, QCoreApplication.translate("Pedido", u"TRANSPORTE ENERGY 81, C.A.", None))
        self.Provedor.setItemText(16, QCoreApplication.translate("Pedido", u"TRANSPORTE LEOAR, C.A", None))
        self.Provedor.setItemText(17, QCoreApplication.translate("Pedido", u"CLONE SERVICES, C.A.", None))
        self.Provedor.setItemText(18, QCoreApplication.translate("Pedido", u"TRANSPORTE FREYMAR, C.A.", None))
        self.Provedor.setItemText(19, QCoreApplication.translate("Pedido", u"TRANSPORTE TRANSFAMILIA 2023, C.A.", None))
        self.Provedor.setItemText(20, QCoreApplication.translate("Pedido", u"ANTONIO VILLALOBOS", None))
        self.Provedor.setItemText(21, QCoreApplication.translate("Pedido", u"SERVILONG, C.A.", None))

        self.BotonMas.setText("")
        self.BotonMenos.setText("")
        self.BotonListo.setText("")
        self.Tarifa.setText("")
        self.label_16.setText(QCoreApplication.translate("Pedido", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">TARIFA</span></p></body></html>", None))
    # retranslateUi

