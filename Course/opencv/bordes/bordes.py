# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 10:15:09 2022

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# img = cv2.imread("coins.png", 0) ##leemos la imagen de entrada en escala de grises

# x = cv2.Sobel(img, cv2.CV_16S, 1,0, ksize = 3) ##aplicamos el filtro sobel con una derivada
# ##de grado 1  en X y con un kernel de 3x3, se convierte en una imagen de 16 bits
# y = cv2.Sobel(img, cv2.CV_16S, 0,1, ksize = 3)##aplicamos el filtro sobel con una derivada
# ##de grado 1  en Y y con un kernel de 3x3, se convierte en una imagen de 16 bits

# absX = cv2.convertScaleAbs(x) ##convertimos los valores obtenidos en valores absolutos y la 
# ##salida de esta función nos retorna la imagen a 8 bits
# absY = cv2.convertScaleAbs(y) ##convertimos los valores obtenidos en valores absolutos y la 
# ##salida de esta función nos retorna la imagen a 8 bits

# destino = cv2.addWeighted(absX, 0.5, absY, 0.5, 0) ##combinamos las dos imagenes, definiendo
# ##0.5 el peso de trasparencia de los elementos de la primer imagen y 0.5 los pesos de la segunda
# ## el tercer elemento es un elemento agregado

# cv2.imshow("original", img) ## mostrar la imagen original
# cv2.imshow("absX", absX) ## mostramos la imagen filtrada en X
# cv2.imshow("absY", absY) ##mostramos la imagen filtrada en Y

# cv2.imshow("resultado", destino) ## mostramos el resultado de combinar las dos imagenes

# cv2.waitKey(0) ## definimos un timepo de muestreo para la imagen y esperamos que se presione
# ## cualquier tecla
# cv2.destroyAllWindows() ## cerramos cualquier ventana perteneciente a opencv.



##Filtro Canny

# img = cv2.imread("coins.png", 0) 
# bordes = cv2.Canny(img,135,255) ## aplicamos el filtro canny para la deteccion de bordes,
# ##seleccionamos un umbral minimo de 135 y un maximo de 255
# cv2.imshow("Result", bordes)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread("coins.png", 0)

# gaussiana = cv2.GaussianBlur(img, (9,9), 0)

# _, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY)

# bordes = cv2.Canny(th, 135, 255)
# cv2.imshow("Result", bordes)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


imgC = cv2.imread("coins.png")
imgD = imgC.copy()
img = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)

gaussiana = cv2.GaussianBlur(img, (9,9), 0)

_, th = cv2.threshold(gaussiana, 100,255, cv2.THRESH_BINARY)

bordes = cv2.Canny(th, 135,255)

alto, largo = img.shape

for i in range(largo):
    for j in range(alto):
        if bordes[j,i] == 255:
            imgD[j,i] = (0,255,0)
            
cv2.imshow("Original", imgC)
cv2.imshow("Bordes", bordes)
cv2.imshow("resultado", imgD)

cv2.waitKey(0)
cv2.destroyAllWindows()























