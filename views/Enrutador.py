# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Enrutador.ui'
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

class Ui_EnRutador(object):
    def setupUi(self, EnRutador):
        if not EnRutador.objectName():
            EnRutador.setObjectName(u"EnRutador")
        EnRutador.setEnabled(True)
        EnRutador.resize(1289, 1039)
        palette = QPalette()
        brush = QBrush(QColor(28, 60, 107, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        EnRutador.setPalette(palette)
        EnRutador.setStyleSheet(u"QPlainTextEdit {\n"
"\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    margin: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1c3c6b; \n"
"    color: #ffffff;\n"
"    padding: 4px;\n"
"    border: 1px solid #aaa;\n"
"    font-weight: bold;\n"
"}\n"
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
"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"    background: #04943b;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #04943b;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.Enrutar = QFrame(EnRutador)
        self.Enrutar.setObjectName(u"Enrutar")
        self.Enrutar.setGeometry(QRect(-20, 0, 1781, 1011))
        self.Enrutar.setFrameShape(QFrame.Shape.StyledPanel)
        self.Enrutar.setFrameShadow(QFrame.Shadow.Raised)
        self.TablaPlanificacion = QTableWidget(self.Enrutar)
        if (self.TablaPlanificacion.columnCount() < 1):
            self.TablaPlanificacion.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.TablaPlanificacion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.TablaPlanificacion.rowCount() < 1):
            self.TablaPlanificacion.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TablaPlanificacion.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TablaPlanificacion.setItem(0, 0, __qtablewidgetitem2)
        self.TablaPlanificacion.setObjectName(u"TablaPlanificacion")
        self.TablaPlanificacion.setGeometry(QRect(70, 80, 971, 481))
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
        self.TablaPlanificacion.setPalette(palette1)
        self.TablaPlanificacion.setStyleSheet(u"QTableWidget {\n"
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
        self.label_5 = QLabel(self.Enrutar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 40, 171, 41))
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
        self.BotonSugerir = QPushButton(self.Enrutar)
        self.BotonSugerir.setObjectName(u"BotonSugerir")
        self.BotonSugerir.setGeometry(QRect(1060, 220, 161, 51))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush12 = QBrush(QColor(148, 193, 30, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush13 = QBrush(QColor(85, 170, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonSugerir.setPalette(palette3)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.BotonSugerir.setFont(font)
        self.BotonSugerir.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        self.TablaFacturar = QTableWidget(self.Enrutar)
        self.TablaFacturar.setObjectName(u"TablaFacturar")
        self.TablaFacturar.setGeometry(QRect(60, 600, 1201, 361))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.TablaFacturar.setPalette(palette4)
        self.TablaFacturar.setStyleSheet(u"QTableWidget {\n"
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
        self.label_8 = QLabel(self.Enrutar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 560, 141, 41))
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
        self.BotonMapa = QPushButton(self.Enrutar)
        self.BotonMapa.setObjectName(u"BotonMapa")
        self.BotonMapa.setGeometry(QRect(1060, 280, 161, 51))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonMapa.setPalette(palette6)
        self.BotonMapa.setFont(font)
        self.BotonMapa.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        self.BotonMapa_2 = QPushButton(self.Enrutar)
        self.BotonMapa_2.setObjectName(u"BotonMapa_2")
        self.BotonMapa_2.setGeometry(QRect(1060, 340, 161, 51))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.BotonMapa_2.setPalette(palette7)
        self.BotonMapa_2.setFont(font)
        self.BotonMapa_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        self.Reiniciar = QPushButton(self.Enrutar)
        self.Reiniciar.setObjectName(u"Reiniciar")
        self.Reiniciar.setGeometry(QRect(1060, 160, 161, 51))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Reiniciar.setPalette(palette8)
        self.Reiniciar.setFont(font)
        self.Reiniciar.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")

        self.retranslateUi(EnRutador)

        QMetaObject.connectSlotsByName(EnRutador)
    # setupUi

    def retranslateUi(self, EnRutador):
        EnRutador.setWindowTitle(QCoreApplication.translate("EnRutador", u"Proceso de Distribuci\u00f3n", None))
        ___qtablewidgetitem = self.TablaPlanificacion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EnRutador", u"x", None));
        ___qtablewidgetitem1 = self.TablaPlanificacion.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EnRutador", u"y", None));

        __sortingEnabled = self.TablaPlanificacion.isSortingEnabled()
        self.TablaPlanificacion.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.TablaPlanificacion.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EnRutador", u"s", None));
        self.TablaPlanificacion.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("EnRutador", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Planificado</span></p></body></html>", None))
        self.BotonSugerir.setText(QCoreApplication.translate("EnRutador", u"Sugerencia", None))
        self.label_8.setText(QCoreApplication.translate("EnRutador", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">A Facturar</span></p></body></html>", None))
        self.BotonMapa.setText(QCoreApplication.translate("EnRutador", u"Mapa", None))
        self.BotonMapa_2.setText(QCoreApplication.translate("EnRutador", u"Facturar", None))
        self.Reiniciar.setText(QCoreApplication.translate("EnRutador", u"Reiniciar", None))
    # retranslateUi

