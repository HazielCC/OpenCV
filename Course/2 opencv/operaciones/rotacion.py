# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:11:00 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# imagen = cv2.imread("2.png")
# imagen2 = cv2.resize(imagen,(200,200)) ## la redimensionamos solo para efectos practicos
# alto, ancho, canales = imagen2.shape

# angle = 80
# center = (ancho // 2, alto // 2)
# scale = 1

# M = cv2.getRotationMatrix2D(center, angle, scale)
# print(M)

# imgT = np.zeros((alto+50, ancho+50,canales),np.uint8)

# for i in range(alto):
#     for j in range(ancho):
#         px = np.array(([j, i, 1]), np.uint8)
#         dot = np.dot(M, px)
#         x = int((dot[0]))
#         y = int((dot[1]))
#         imgT[y,x] = imagen2[i,j]
        
# cv2.namedWindow("org", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("org", imagen2)
# cv2.imshow("t", imgT)

# cv2.waitKey()
# cv2.destroyAllWindows()


# imagen = cv2.imread("2.png")
# imagen2 = cv2.resize(imagen,(200,200)) ## la redimensionamos solo para efectos practicos
# alto, ancho, canales = imagen2.shape

# angle = 80
# center = (ancho // 2, alto // 2)
# scale = 1

# M = cv2.getRotationMatrix2D(center, angle, scale)
# print(M)

# imgT = cv2.warpAffine(imagen2, M, (ancho, alto))

# cv2.namedWindow("org", cv2.WINDOW_NORMAL)
# cv2.namedWindow("t", cv2.WINDOW_NORMAL)

# cv2.imshow("org", imagen2)
# cv2.imshow("t", imgT)

# cv2.waitKey()
# cv2.destroyAllWindows()

import imutils

imagen = cv2.imread("2.png")
imagen2 = cv2.resize(imagen,(200,200)) ## la redimensionamos solo para efectos practicos
alto, ancho, canales = imagen2.shape

angle = 90
# center = (ancho // 2, alto // 2)

imgT = imutils.rotate_bound(imagen2, angle)

cv2.namedWindow("org", cv2.WINDOW_NORMAL)
cv2.namedWindow("t", cv2.WINDOW_NORMAL)

cv2.imshow("org", imagen2)
cv2.imshow("t", imgT)

cv2.waitKey()
cv2.destroyAllWindows()