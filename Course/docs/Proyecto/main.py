# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:41:59 2021

@author: A.Martinez
"""

## importamos las librerias a utilizar
import sys
from visionCurso import Ui_MainWindow ##importamos la interfaz grafica
import visionLib ##importamos la libreria visionLib
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from labels import MyLabel ##Importamos la clase Qlabel modificada
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from mTK import selectFile


class aplicacionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dialogo = Ui_MainWindow()
        self.dialogo.setupUi(self)

        ##Creación de los labels que mostraran las imagenes
        self.ancho=550
        self.alto=522
        self.imagenTest = 0


        self.inicializar()

        self.dialogo.simuladorChB.clicked.connect(self.simuladorClicked)
        self.dialogo.activarColorChB.clicked.connect(self.colorClicked)
        self.dialogo.activarPresenciaChB.clicked.connect(self.presenciaClicked)
        self.dialogo.SelectImageButton.clicked.connect(self.simuladorImagen)
        self.dialogo.cargarImagenTest.clicked.connect(self.cargarImagenTestSim)
        self.dialogo.guardarRoiColorButton.clicked.connect(self.guardarROIColor)

        self.dialogo.activarColorChB.clicked.connect(self.habilitarTest)
        self.dialogo.activarPresenciaChB.clicked.connect(self.habilitarTest)
        self.dialogo.capturarImagenButton.clicked.connect(self.capturarImagen)
        self.dialogo.guardarElementoPresencia.clicked.connect(self.guardarROIPresencia)
        self.dialogo.realizarTestButton.clicked.connect(self.testFunc)

        self.camarasDisponibles = visionLib.leerCamarasDisponibles()
        self.dialogo.camarasCBox.clear()
        self.dialogo.camarasCBox.addItems(self.camarasDisponibles)

    def inicializar(self):
        self.dialogo.tabWidget.setTabEnabled(1, False)
        self.dialogo.tabWidget.setTabEnabled(2, False)
        self.dialogo.tabWidget.setTabEnabled(3, False)
        self.dialogo.SelectImageButton.setEnabled(False)


    def simuladorClicked(self):
        x = self.dialogo.simuladorChB.isChecked()
        if x == True:
            self.dialogo.SelectImageButton.setEnabled(True)
            self.dialogo.capturarImagenButton.setEnabled(False)
            self.dialogo.camarasCBox.setEnabled(False)
            self.dialogo.camarasCBox.clear()
            self.dialogo.cargarImagenTest.setDisabled(False)
            self.dialogo.realizarTestButton.setDisabled(True)
        else:
            self.dialogo.SelectImageButton.setEnabled(False)
            self.dialogo.capturarImagenButton.setEnabled(True)
            self.dialogo.camarasCBox.setEnabled(True)
            self.camarasDisponibles = visionLib.leerCamarasDisponibles()
            self.dialogo.camarasCBox.clear()
            self.dialogo.camarasCBox.addItems(self.camarasDisponibles)
            self.dialogo.cargarImagenTest.setDisabled(True)
            self.dialogo.realizarTestButton.setDisabled(False)

    def colorClicked(self):
        x = self.dialogo.activarColorChB.isChecked()
        if x == True:
            self.dialogo.tabWidget.setTabEnabled(1, True)
        else:
            self.dialogo.tabWidget.setTabEnabled(1, False)

    def presenciaClicked(self):
        x = self.dialogo.activarPresenciaChB.isChecked()
        if x == True:
            self.dialogo.tabWidget.setTabEnabled(2, True)
        else:
            self.dialogo.tabWidget.setTabEnabled(2, False)

    def habilitarTest(self):
        if (self.dialogo.activarColorChB.isChecked() == True or
            self.dialogo.activarPresenciaChB.isChecked() == True):

            self.dialogo.tabWidget.setTabEnabled(3, True)
        else:
            self.dialogo.tabWidget.setTabEnabled(3, False)

    def capturarImagen(self):
        camara = self.dialogo.camarasCBox.currentText()
        self.img, height, width, bytesPerLine = visionLib.capturarImagenShow(camara)
        self.mostrarImagenes(self.img, height, width, bytesPerLine)

    def simuladorImagen(self):
        ruta = selectFile()
        self.img, height, width, bytesPerLine = visionLib.capturarImagenSim(ruta)
        self.mostrarImagenes(self.img, height, width, bytesPerLine)

    def mostrarImagenes(self,img, height, width, bytesPerLine):

        QImg = QImage(img.data, width, height, bytesPerLine,QImage.Format_RGB888)

        self.pixmap = QPixmap.fromImage(QImg)
        self.dialogo.imagenCapturadaLabel.setPixmap(self.pixmap)
        self.dialogo.imagenCapturadaLabel.setCursor(Qt.CrossCursor)
        self.dialogo.imagenCapturadaLabel.setFixedWidth(self.ancho)
        self.dialogo.imagenCapturadaLabel.setFixedHeight(self.alto)

        self.dialogo.imagenColorLabel.modifDimImage(width, height)
        self.pixmap2 = QPixmap.fromImage(QImg)
        self.dialogo.imagenColorLabel.setPixmap(self.pixmap2)
        self.dialogo.imagenColorLabel.setCursor(Qt.CrossCursor)
        self.dialogo.imagenColorLabel.setFixedWidth(self.ancho)
        self.dialogo.imagenColorLabel.setFixedHeight(self.alto)

        self.dialogo.imagenPresenciaLabel.modifDimImage(width, height)
        self.pixmap3 = QPixmap.fromImage(QImg)
        self.dialogo.imagenPresenciaLabel.setPixmap(self.pixmap3)
        self.dialogo.imagenPresenciaLabel.setCursor(Qt.CrossCursor)
        self.dialogo.imagenPresenciaLabel.setFixedWidth(self.ancho)
        self.dialogo.imagenPresenciaLabel.setFixedHeight(self.alto)

    def mostrarImagenesTest(self,img, height, width, bytesPerLine):

        QImg = QImage(img.data, width, height, bytesPerLine,QImage.Format_RGB888)

        self.pixmap4 = QPixmap.fromImage(QImg)
        self.dialogo.imagenTestLabel.setPixmap(self.pixmap4)
        self.dialogo.imagenTestLabel.setCursor(Qt.CrossCursor)
        self.dialogo.imagenTestLabel.setFixedWidth(self.ancho)
        self.dialogo.imagenTestLabel.setFixedHeight(self.alto)


    def guardarROIColor(self):
        self.rectanguloColor = self.dialogo.imagenColorLabel.obtenerRectangulo()
        self.porcentajeColor = int(self.dialogo.pAceptacionColorSpin.value())
        print(self.rectanguloColor,self.porcentajeColor)
        self.bajoX, self.altoX, self.total = visionLib.extractColor(self.img, self.rectanguloColor)
        print(self.bajoX, self.altoX, self.total)

    def guardarROIPresencia(self):
        self.rectanguloPresencia = self.dialogo.imagenPresenciaLabel.obtenerRectangulo()
        self.porcentajePresencia = int(self.dialogo.pAceptacionPresenciaSpin.value())
        print(self.rectanguloPresencia,self.porcentajePresencia)


    def cargarImagenTestSim(self):
        rutaTest = selectFile()
        self.imgTest, height, width, bytesPerLine = visionLib.capturarImagenSim(rutaTest)
        self.mostrarImagenesTest(self.imgTest, height, width, bytesPerLine)
        self.dialogo.realizarTestButton.setDisabled(False)
        self.imgTestShow = self.imgTest


    def takePhoto(self):
        camara = self.dialogo.camarasCBox.currentText()
        self.imgTest, height, width, bytesPerLine = visionLib.capturarImagenShow(camara)
        self.mostrarImagenesTest(self.imgTest, height, width, bytesPerLine)
        self.imgTestShow = self.imgTest


    def testFunc(self):
        x = self.dialogo.simuladorChB.isChecked()
        if x == False:
            self.takePhoto()
        else:
            self.dialogo.realizarTestButton.setDisabled(True)

        testColor = self.dialogo.activarColorChB.isChecked()
        if testColor == True:
            resultColor, imageReturnedColor = visionLib.testColor(self.porcentajeColor, self.imgTest,
                                                                  self.bajoX, self.altoX, self.total)
            print(resultColor)
            self.imgTestShow, height, width, bytesPerLine =visionLib.convertImage(imageReturnedColor)
            self.mostrarImagenesTest(self.imgTestShow, height, width, bytesPerLine)
        else:
            resultColor = ("OK", 100)

        testPresencia = self.dialogo.activarPresenciaChB.isChecked()
        if testPresencia == True:
            resultPresencia, imageReturnedPresencia  = visionLib.testPlantilla(self.imgTest,
                                self.rectanguloPresencia, self.porcentajePresencia, self.imgTestShow, self.img)
            self.imgTestShow, height, width, bytesPerLine =visionLib.convertImage(imageReturnedPresencia)
            self.mostrarImagenesTest(self.imgTestShow, height, width, bytesPerLine)
        else:
            resultPresencia = ("OK", 100)



        self.dialogo.resultadoColorLabel.setText(resultColor[0])
        self.dialogo.porcentajeColorRes.setText(str(round(resultColor[1], 2)))
        self.dialogo.resultadoPresenciaLabel.setText(resultPresencia[0])
        self.dialogo.porcentajePresenciaRes.setText(str(resultPresencia[1]))

        if resultColor[0] == "OK" and resultPresencia[0] == "OK":
            self.dialogo.resultadoGeneralLabel.setText("PASS")
            self.dialogo.resultadoGeneralLabel.setStyleSheet("background-color: green; border: 1px solid black;")
            print("PASS")
        else:
            self.dialogo.resultadoGeneralLabel.setText("FAIL")
            self.dialogo.resultadoGeneralLabel.setStyleSheet("background-color: red; border: 1px solid black;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = aplicacionWindow()
    dialogo.show()
    sys.exit(app.exec_())