# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PedidosHuerfano.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(876, 687)
        palette = QPalette()
        brush = QBrush(QColor(28, 60, 107, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Form.setPalette(palette)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 881, 681))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame.setPalette(palette1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(290, 20, 341, 61))
        palette2 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(127, 127, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(170, 170, 170, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush5 = QBrush(QColor(255, 255, 220, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush5)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 127))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush7 = QBrush(QColor(127, 127, 127, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        self.label_16.setPalette(palette2)
        self.label_16.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    color: white; /* Cambia 'blue' por el color que prefieras */\n"
"}")
        self.PedidosHuerfanos = QTableWidget(self.frame)
        self.PedidosHuerfanos.setObjectName(u"PedidosHuerfanos")
        self.PedidosHuerfanos.setGeometry(QRect(10, 80, 861, 501))
        palette3 = QPalette()
        brush8 = QBrush(QColor(0, 0, 0, 0))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush8)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.PedidosHuerfanos.setPalette(palette3)
        self.PedidosHuerfanos.setStyleSheet(u"QTableWidget {\n"
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
        self.BotonMas_2 = QPushButton(self.frame)
        self.BotonMas_2.setObjectName(u"BotonMas_2")
        self.BotonMas_2.setGeometry(QRect(320, 580, 91, 81))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush12 = QBrush(QColor(148, 193, 30, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush13 = QBrush(QColor(85, 170, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush12)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonMas_2.setPalette(palette4)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.BotonMas_2.setFont(font)
        self.BotonMas_2.setStyleSheet(u"QPushButton {\n"
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
        self.BotonMas_2.setIcon(icon)
        self.BotonMas_2.setIconSize(QSize(75, 75))
        self.BotonMas_2.setFlat(True)
        self.BotonListo_2 = QPushButton(self.frame)
        self.BotonListo_2.setObjectName(u"BotonListo_2")
        self.BotonListo_2.setGeometry(QRect(440, 580, 91, 81))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonListo_2.setPalette(palette5)
        self.BotonListo_2.setFont(font)
        self.BotonListo_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/BotonListo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonListo_2.setIcon(icon1)
        self.BotonListo_2.setIconSize(QSize(110, 110))
        self.BotonListo_2.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">PEDIDOS SIN AGREGAR</span></p></body></html>", None))
        self.BotonMas_2.setText("")
        self.BotonListo_2.setText("")
    # retranslateUi

