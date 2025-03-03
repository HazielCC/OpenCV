# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:47:49 2022

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# img = cv2.imread('engranaje.jpg', 0)
# img2 = img.copy()
# template = cv2.imread('template.jpg',0)
# w, h = template.shape[::-1]

# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# for metodoX in methods:
#     img = img2.copy()
#     metodo = eval(metodoX)

#     res = cv2.matchTemplate(img, template, metodo)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

#     if metodo in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc

#     inf_der = (top_left[0] + w, top_left[1] + h)
#     cv2.rectangle(img,top_left, inf_der, 255, 2)

#     cv2.imwrite(metodoX+".jpg", img)

# imgRgb = cv2.imread('waldo.jpg')
# imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('BOLSO.jpg',0)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
# umbral = 0.8
# rectangulos = np.where(res >= umbral)

# for punto in zip(*rectangulos[::-1]):
#     print(punto)
#     cv2.rectangle(imgRgb, punto, (punto[0] + w, punto[1] + h), (0,255,0), 2)
# cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)
# cv2.imshow("resultado", imgRgb)

# cv2.waitKey()
# cv2.destroyAllWindows()



# def umbral(valor):
#     img2 = imgRgb.copy()
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
#     umbralX = valor/100
#     rectangulos = np.where(res >= umbralX)

#     for puntos in zip(*rectangulos[::-1]):
#         print(puntos)
#         cv2.rectangle(img2, puntos, (puntos[0] + w, puntos[1] + h), (0,255,0), 1)
#     cv2.imshow('match', img2)


# cv2.namedWindow('match', cv2.WINDOW_NORMAL)

# imgRgb = cv2.imread('engranaje.jpg')
# imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('template.jpg', 0)
# cv2.imshow('match', imgRgb)

# cv2.createTrackbar('Umbral', 'match', 0, 100, umbral)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



def umbral(valor):
    img2 = imgRgb.copy()
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
    umbralX = valor/100
    rectangulos = np.where(res >= umbralX)

    for puntos in zip(*rectangulos[::-1]):
        print(puntos)
        cv2.rectangle(img2, puntos, (puntos[0] + w, puntos[1] + h), (0,255,0), 1)
    cv2.imshow('match', img2)


cv2.namedWindow('match', cv2.WINDOW_NORMAL)


imgRgb = cv2.imread('engranaje.jpg')

roi = cv2.selectROI('match', imgRgb, True)
x = roi[0]
y = roi[1]
w = roi[2]
h = roi[3]

template = imgRgb[y:y+h, x:x+w]

imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow('match', imgRgb)

cv2.createTrackbar('Umbral', 'match', 0, 100, umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()










