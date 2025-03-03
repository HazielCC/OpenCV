# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:35:01 2021

@author: Jesus-Mtz
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

# img = cv2.imread("aaa.png", 0) ## leemos la imagen de entrada y la guardamos en la variable img
# equ = cv2.equalizeHist(img)## realizamos la equialización del histograma

# res = np.hstack((img,equ)) ##concatenamos la imagen de entrada con la imagen equializada
# cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)#construimos nuestra ventana donde se mostrara la imagen
# cv2.imshow("resultado", res) ##mostramos la imagen concatenada
# cv2.waitKey()
# cv2.destroyAllWindows()

# hist, bins = np.histogram(img.flatten(), 256, [0,256])
# plt.hist(img.flatten(), 256, [0,256], color = 'b')
# plt.xlim([0,256])
# plt.legend('H', loc = 'upper left')
# plt.show()

# hist, bins = np.histogram(equ.flatten(), 256, [0,256])
# plt.hist(equ.flatten(), 256, [0,256], color = 'b')
# plt.xlim([0,256])
# plt.legend('H', loc = 'upper left')
# plt.show()



img = cv2.imread("aaa.png", 0) ## leemos la imagen de entrada y la guardamos en la variable img
clahe = cv2.createCLAHE(clipLimit = 5.0 , tileGridSize = (8,8)) ##creamos la configuración  para el algoritmo
##CLAHE con un humbral de 1.0 y un kernel de 8 x 8

cl1 = clahe.apply(img) ## aplicamos el metodo a la imagen de entrada
res = np.hstack((img,cl1)) ##concatenamos la imagen de entrada con la imagen equializada

cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)#construimos nuestra ventana donde se mostrara la imagen
cv2.imshow("resultado", res) ##mostramos la imagen concatenada
cv2.waitKey()
cv2.destroyAllWindows()

hist, bins = np.histogram(img.flatten(), 256, [0,256])
plt.hist(img.flatten(), 256, [0,256], color = 'b')
plt.xlim([0,256])
plt.legend('H', loc = 'upper left')
plt.show()

hist, bins = np.histogram(cl1.flatten(), 256, [0,256])
plt.hist(cl1.flatten(), 256, [0,256], color = 'b')
plt.xlim([0,256])
plt.legend('H', loc = 'upper left')
plt.show()