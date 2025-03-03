# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:36:57 2021

@author: Jesus-Mtz
"""

import numpy as np
import cv2

# imagen = cv2.imread("1.jpg") ## leemos la imagen a trasladar
# imagen2 =cv2.resize(imagen,(100,50)) #redimensionamos la imagen solo para efectos practicos
# alto, ancho, canales = imagen2.shape ## obtenemos las dimensiones de la imagen

# tx = 1 ## definimos la  traslación en x de 10 px
# ty= 1 ## definimos la traslación en y de 2 px

# mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8)

# imgT = np.zeros((alto + ty, ancho + tx, canales), np.uint8)

# for i in range(alto): ## recorremos las filas de la matriz de la imagen
#     for j in range(ancho): ## recorremos las columnas de la matriz de la imagen
#         px = np.array(([j, i, 1]), np.uint8) ## formamos nuestro vector posición
#         dot = np.dot(mT, px) ## realizamos el producto punto entre la matriz de tranformación y el vector posicion
#         x = dot[0] ## extraemos el valor para x
#         y = dot[1]## extraemos el valor para y
#         imgT[y, x] = imagen2[i, j] ##remplazamos los valores de los pixeles
        
# cv2.namedWindow("org", cv2.WINDOW_NORMAL)
# cv2.namedWindow("T", cv2.WINDOW_NORMAL)

# cv2.imshow("org", imagen2)
# cv2.imshow("T", imgT)

# cv2.waitKey()
# cv2.destroyAllWindows()


imagen = cv2.imread("1.jpg") ## leemos la imagen a trasladar
imagen2 =cv2.resize(imagen,(100,50)) #redimensionamos la imagen solo para efectos practicos
alto, ancho, canales = imagen2.shape ## obtenemos las dimensiones de la imagen

tx = 1 ## definimos la  traslación en x de 10 px
ty= 1 ## definimos la traslación en y de 2 px

mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8)

imgT = np.zeros((alto + ty, ancho + tx, canales), np.uint8)

for i in range(alto):
    for j in range(ancho):
        x = j + tx
        y = i + ty
        imgT[y, x] = imagen2[i, j]

cv2.namedWindow("org", cv2.WINDOW_NORMAL)
cv2.namedWindow("T", cv2.WINDOW_NORMAL)

cv2.imshow("org", imagen2)
cv2.imshow("T", imgT)

cv2.waitKey()
cv2.destroyAllWindows()


imagen = cv2.imread("1.jpg") ## leemos la imagen a trasladar
imagen =cv2.resize(imagen,(100,50)) #redimensionamos la imagen solo para efectos practicos
alto, ancho, canales = imagen.shape ## obtenemos las dimensiones de la imagen

mt = np.float32([[1, 0, 25], [0, 1, 30]]) ## generamos nuestra matriz de transformación

imgT = cv2.warpAffine(imagen, mt, (ancho, alto))


cv2.namedWindow("org", cv2.WINDOW_NORMAL)
cv2.namedWindow("T", cv2.WINDOW_NORMAL)

cv2.imshow("org", imagen)
cv2.imshow("T", imgT)

cv2.waitKey()
cv2.destroyAllWindows()




