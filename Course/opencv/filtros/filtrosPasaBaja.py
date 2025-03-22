# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:26:27 2021

@author: Jesus-Mtz
"""

#filtros pasa baja
import cv2

#filtro de promediado

# img = cv2.imread("images.jpg", 0)
# imgBlurred = cv2.blur(img,(8,8)) #aplicamos un filtro de promediado con un kernel de 8 x 8 a la imagen original
# # y la guardamos en imgBlurred
# cv2.imshow("original", img)
# cv2.imshow("modif", imgBlurred)
# cv2.waitKey()
# cv2.destroyAllWindows()

#filtro de desenfoque gaussiano

# img = cv2.imread("images.jpg", 0)
# filtrada = cv2.GaussianBlur(img,(9,9), 3)

# cv2.imshow("original", img)
# cv2.imshow("modif", filtrada)
# cv2.waitKey()
# cv2.destroyAllWindows()

#filtro de desenfoque medio

# img = cv2.imread("salypimienta.jpg", 0)
# filtrada = cv2.medianBlur(img, 9)
# cv2.imshow("original", img)
# cv2.imshow("modif", filtrada)
# cv2.waitKey()
# cv2.destroyAllWindows()

#filtrado bilateral

# img = cv2.imread("images.jpg", 0)
# filtrada = cv2.bilateralFilter(img,9, 80, 80)

# cv2.imshow("original", img)
# cv2.imshow("modif", filtrada)
# cv2.waitKey()
# cv2.destroyAllWindows()

import numpy as np

img = cv2.imread("a.jpg",0) # LEEMOS LA IMAGEN A PROCESAR
equ = cv2.equalizeHist(img) #EQUALIZAMOS EL HISTOGRAMA DE LA IMAGEN
blur = cv2.blur(equ, (8,8)) # APLICAMOS UN FILTRO DE PROMEDIADO
blur = cv2.medianBlur(blur, 3) #APLICAMOS UN MEDIANBLUR A LA IMAGEN
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) #CREAMOS UN KERNEL PARA AFILAR LA IMAGEN
afilada = cv2.filter2D(blur, -1, sharpen_kernel) #APLICAMOS EL FILTRO DE AFILAMIENTO A LA IMAGEN
result = np.hstack((img, equ, blur, afilada)) # CONCATENAMOS LAS IMAGENES RESULTANTES
cv2.namedWindow("resultadoGral", cv2.WINDOW_NORMAL) #CREAMOS UNA VENTANA CON AUTO AJUSTE
cv2.imshow("resultadoGral", result) #MOSTRAMOS LA IMAGEN CONCATENADA
cv2.waitKey(0) #DEFINIMOS UN TIEMPO DE MUESTREO Y ESPERAMOS UNA TECLA
cv2.destroyAllWindows() #DESTRUIMOS LAS VENTANAS DE OPENCV