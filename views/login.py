# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_InicioSesion(object):
    def setupUi(self, InicioSesion):
        if not InicioSesion.objectName():
            InicioSesion.setObjectName(u"InicioSesion")
        InicioSesion.setEnabled(True)
        InicioSesion.resize(562, 458)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(28, 60, 107, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(42, 90, 160, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(35, 75, 133, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(14, 30, 53, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(19, 40, 71, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(14, 30, 53, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        brush10 = QBrush(QColor(20, 42, 75, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush10)
        InicioSesion.setPalette(palette)
        self.Login = QFrame(InicioSesion)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(10, 0, 561, 461))
        self.Login.setFrameShape(QFrame.Shape.StyledPanel)
        self.Login.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 230, 291, 61))
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"")
        self.comboBox = QComboBox(self.Login)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 320, 161, 22))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush11 = QBrush(QColor(148, 193, 30, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        brush12 = QBrush(QColor(0, 255, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush12)
        brush13 = QBrush(QColor(0, 85, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush13)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush13)
        brush14 = QBrush(QColor(255, 85, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush14)
        brush15 = QBrush(QColor(255, 85, 255, 127))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        brush16 = QBrush(QColor(0, 170, 0, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush16)
        brush17 = QBrush(QColor(255, 85, 127, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush17)
        brush18 = QBrush(QColor(170, 170, 0, 127))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush16)
        brush19 = QBrush(QColor(85, 170, 255, 127))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.comboBox.setPalette(palette1)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"  	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #94c11e;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox.setPlaceholderText(u"")
        self.comboBox.setDuplicatesEnabled(False)
        self.aceptar = QPushButton(self.Login)
        self.aceptar.setObjectName(u"aceptar")
        self.aceptar.setGeometry(QRect(220, 360, 75, 24))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        brush20 = QBrush(QColor(85, 170, 0, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush20)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush11)
        brush21 = QBrush(QColor(255, 255, 255, 128))
        brush21.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush21)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush20)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush21)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.aceptar.setPalette(palette2)
        self.aceptar.setStyleSheet(u"QPushButton {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #94c11e;\n"
"    color: white;\n"
"}\n"
"")
        self.label_2 = QLabel(self.Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 100, 141, 121))
        self.label_2.setPixmap(QPixmap(u"./assets/IconIniciarSesion.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(InicioSesion)

        QMetaObject.connectSlotsByName(InicioSesion)
    # setupUi

    def retranslateUi(self, InicioSesion):
        InicioSesion.setWindowTitle(QCoreApplication.translate("InicioSesion", u"Iniciar Sesion", None))
        self.label.setText(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p><span style=\" font-weight:700;\">Inicie Sesion</span></p></body></html>", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("InicioSesion", u"Ysmeira Floiran", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("InicioSesion", u"Gregory Sevilla", None))

        self.aceptar.setText(QCoreApplication.translate("InicioSesion", u"Aceptar", None))
        self.label_2.setText("")
    # retranslateUi

