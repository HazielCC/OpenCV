# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:24:14 2022

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# img = cv2.imread("coins.png")
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# kernel = np.ones((3,3), np.uint8)
# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
# bordes = cv2.Canny(closing, 135, 255)

# contours, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, 
#                                        cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img2, contours, -1, (0,150,200), 2)
# cantidadMonedas = len(contours)

# img2 = cv2.putText(img2, "son "+ str(cantidadMonedas)+ " monedas", (10,50),
#                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print("Son " + str(cantidadMonedas)+ " monedas")
# cv2.imshow("original", img)
# cv2.imshow("closing", closing)
# cv2.imshow("bordes", bordes)
# cv2.imshow("Resultados", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread("coins.png")
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# kernel = np.ones((3,3), np.uint8)
# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
# # bordes = cv2.Canny(closing, 135, 255)

# contours, jerarquia = cv2.findContours(closing, cv2.RETR_EXTERNAL, 
#                                        cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img2, contours, -1, (0,150,200), 2)
# cantidadMonedas = len(contours)

# img2 = cv2.putText(img2, "son "+ str(cantidadMonedas)+ " monedas", (10,50),
#                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print("Son " + str(cantidadMonedas)+ " monedas")
# cv2.imshow("original", img)
# cv2.imshow("closing", closing)
# # cv2.imshow("bordes", bordes)
# cv2.imshow("Resultados", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread("tornillos.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((15,15), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
# bordes = cv2.Canny(closing, 135, 255)

contours, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, 
                                        cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2, contours, -1, (0,150,200), 20)
cantidadTornillos = len(contours)

img2 = cv2.putText(img2, "son "+ str(cantidadTornillos)+ " tornillos", (10,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 10, cv2.LINE_AA)

print("Son " + str(cantidadTornillos)+ " tornillos")

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("closing", cv2.WINDOW_NORMAL)
cv2.namedWindow("Resultados", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.imshow("closing", closing)
# cv2.imshow("bordes", bordes)
cv2.imshow("Resultados", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
























