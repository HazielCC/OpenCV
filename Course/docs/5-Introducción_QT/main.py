# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainIntroPyQT.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(260, 40, 181, 51))
        self.button.setObjectName("button")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 180, 101, 21))
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 221, 51))
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 221, 31))
        self.comboBox.setObjectName("comboBox")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(430, 210, 181, 161))
        self.imagen.setFrameShape(QtWidgets.QFrame.Box)
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(20, 200, 221, 51))
        self.line2.setReadOnly(True)
        self.line2.setObjectName("line2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Agregar al cbox"))
        self.checkBox.setText(_translate("MainWindow", "Mostrar imagen"))
        self.imagen.setText(_translate("MainWindow", "NO IMAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

