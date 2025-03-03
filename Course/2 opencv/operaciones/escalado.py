# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:19:26 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np

imagen = cv2.imread("1.jpg") ## leemos la imagen a transformar y la guardamos en la variable imagen
h, w, c = imagen.shape ## obtenemos las dimensiones de la imagen

escala = 2

tMatrix = np.array([[escala, 0, 0], [0, escala, 0], [0, 0, 1]]) ## generamos la matriz de transformación

imagen2 = np.zeros((h*escala, w*escala, 3), np.uint8)## generamos la matriz que recibe la imagen escalada

for i in range(h):
    for j in range(w):
        pixel = imagen[i,j] ## obtenemos el valor del pixel
        vectorPos = np.array([j,i,1]) ## generamos nuestro vector posición
        resultPP =np.dot(tMatrix, vectorPos) ## resolvemos el producto punto de la matriz de transformación con
        # el vector posición
        # print(resultPP)
        x = resultPP[0]
        y = resultPP[1]
        imagen2[y,x] = pixel
        
cv2.imshow("original1", imagen)
cv2.imshow("transformada", imagen2)

cv2.waitKey()
cv2.destroyAllWindows()


imagen = cv2.imread("1.jpg")

escalada = cv2.resize(imagen,(1024, 720), interpolation = cv2.INTER_LINEAR)

cv2.imshow("original2", imagen)
cv2.imshow("t", escalada)

cv2.waitKey()
cv2.destroyAllWindows()
