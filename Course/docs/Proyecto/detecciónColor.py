# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:33:27 2021

@author: A.Martinez
"""

import cv2
import numpy as np
frame = cv2.imread(r"C:/Users/Jesus-Mtz/Documents/Python Scripts/IVSLite/IMAGENES/terminal.JPG")

frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

r = cv2.selectROI(frameHSV)

print(r)
imagenNueva = frameHSV[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
altura, ancho = imagenNueva.shape[:2]
H=[]
S=[]
V=[]

for i in range(altura):
    for j in range(ancho):
        # print(imagenNueva[i,j])
        pixel = imagenNueva[i,j]
        H.append(pixel[0])
        S.append(pixel[1])
        V.append(pixel[2])
        
hMin = min(H)
hMax = max(H)
sMin = min(S)
sMax = max(S)
vMin = min(V)
vMax = max(V)

bajo = np.array([hMin,sMin,vMin], np.uint8)
alto = np.array([hMax,sMax,vMax], np.uint8)

mask = cv2.inRange(frameHSV, bajo, alto)

total = 0

altura, ancho = mask.shape[:2]
for i in range(altura):
    for j in range(ancho):
        pixel = mask[i,j]
        if pixel == 255:
            total = total +1
            frame[i,j]= (0,255,0)

multi = total * 100
porcentaje = multi / 18588 ## los 18000 son el valor base con el que se guardó la primer muestra

if porcentaje > 100:
    porcentaje = 100

if porcentaje < 80:
    print("error", porcentaje)
else:
    print("pass", porcentaje)
    
    
cv2.imshow('maskAzul', mask)
cv2.imshow('frame', frame)
cv2.waitKey()

cv2.destroyAllWindows()