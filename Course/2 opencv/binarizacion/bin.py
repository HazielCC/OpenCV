# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:13:33 2021

@author: Jesus-Mtz
"""

import cv2 

# img = cv2.imread("coins.png",0)


## umbralEstablecido, imagenBinarizada=cv2.threshold(imagen, valor de umbral, valor de umbral maximo, tipo de algoritmo)
# _, th = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow("original", img)
# cv2.imshow("bin", th)

# cv2.waitKey()
# cv2.destroyAllWindows()


# def umbral(valor):
#     _, th = cv2.threshold(img, valor, 255, cv2.THRESH_BINARY)
#     cv2.imshow("Binarizando", th)

# cv2.namedWindow("Binarizando")
# img = cv2.imread("coins.png",0)

# cv2.createTrackbar("Umbral", "Binarizando", 0, 255, umbral)

# cv2.waitKey()
# cv2.destroyAllWindows()


# def umbral(valor):
#     _, th = cv2.threshold(img, valor, 255, cv2.THRESH_TOZERO_INV)
#     cv2.imshow("Binarizando", th)

# cv2.namedWindow("Binarizando")
# img = cv2.imread("coins.png",0)

# cv2.createTrackbar("Umbral", "Binarizando", 0, 255, umbral)

# cv2.waitKey()
# cv2.destroyAllWindows()

# from matplotlib import pyplot as plt

# img = cv2.imread("monedas.jpg", 0)
# hist = cv2.calcHist([img], [0], None, [256], [0,255])
# plt.hist(img.ravel(), 256, [0,255])
# plt.show()

# umbral, th = cv2.threshold(img, 0,255, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
# print(umbral)

# cv2.imshow("original", img)
# cv2.imshow("bin", th)

# cv2.waitKey()
# cv2.destroyAllWindows()


kernel = 3
constante = 0

def updateKernel(krn):
    global kernel
    kernel = krn
    
    if kernel < 3:
        kernel = 3
    elif kernel %2 == 0:
        kernel +=1
    
    umbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizada", umbralizada)
    print(kernel)

def updateConstante(cte):
    global constante
    constante = cte
    umbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizada", umbralizada)
    print(constante)
    
cv2.namedWindow("Binarizada")
img = cv2.imread("sudoku.png",0)

cv2.createTrackbar("kernel", "Binarizada", kernel, 255, updateKernel)
cv2.createTrackbar("constante", "Binarizada", constante, 255, updateConstante)

cv2.waitKey()
cv2.destroyAllWindows()



