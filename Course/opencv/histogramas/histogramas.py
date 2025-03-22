# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:30:59 2021

@author: Jesus-Mtz
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

# img = cv2.imread("lena.png",0) ## leemos la imagen en escala de grises
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# plt.hist(img.ravel(), 256, [0,255]) ## graficamos el histograma, .ravel nos devuelve la matriz en fpormato plano
# #continuo, el siguiente dato es en cuantas partes se divide el histograma, el ultimo dato es el rango de gama
# plt.show()

# img = cv2.imread("lena.png")

# color = ('b', 'g', 'r')

# for i, col in enumerate(color): ## recorremos la variable color usando un ciclo for y con la funcion enumerate
# #obtendriamos cada espacio de la tupla enumerado, se obtendria lo siguiente: 0 b 1 g 2 r
#     print(i,col)
#     hist = cv2.calcHist([img], [i], None, [256], [0,255]) ## calculamos el histograma para cada canal de la imagen
    
#     plt.plot(hist, color = col) ##graficamos el histograma por color
#     plt.xlim([0,256])

# plt.show()

img = cv2.imread("lena.png",0)

mask = np.zeros(img.shape[:2], np.uint8)

mask[0:300, 0:300] = 255

masked_img = cv2.bitwise_and(img, img, mask= mask) ## aplicamos una compuerta and bit a bit entre img e img, pero 
##solo en la parte de la mascara con pixeles blancos

histCompleto = cv2.calcHist([img], [0], None, [256], [0, 255])
histMask = cv2.calcHist([img], [0], mask, [256], [0,255])

plt.subplot(221), plt.imshow(img, "gray")
plt.subplot(222), plt.imshow(mask, "gray")
plt.subplot(223), plt.imshow(masked_img, "gray")
plt.subplot(224), plt.plot(histCompleto), plt.plot(histMask)
plt.xlim([0,256])
plt.show()








