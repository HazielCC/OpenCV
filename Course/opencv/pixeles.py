# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:42:25 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# imagenObscura = np.zeros((100,100,3), np.uint8) ##Creamos una matríz de 3 dimenciones y la llenamos con ceros

# pixel = imagenObscura[97,97] ##obtenemos el valor del pixel en la posición 97, 97 de la matríz en general,
# # nos devuelve un vector de 3 elementos

# print(pixel) ## imprimimos el valor del pixel
# # print(type(pixel))

# imagenObscura[30, 60] = [255, 255, 255] ## remplazamos le valor del pixel en la posición 97, 97, lo hacemos color blanco [B, G, R]

# pixel = imagenObscura[30,60]
# print(pixel)

# # obtener las dimensiones de la imagen generada, utilizaremos ña función shape

# alto, largo, canales = imagenObscura.shape()

# print(alto, largo, canales)

# ##Recorremos la imagen imprimiendo los valores de cada pixel
# for i in range(largo):
#     for j in range(alto):
#         print(imagenObscura[i,j])
        
# ##Modificar los valores de cada pixel

# for i in range(largo):
#     for j in range(alto):
#         pixel = imagenObscura[i,j]
#         if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#             imagenObscura[i,j] = [0, 255, 230]
            
# cv2.namedWindow("black", cv2.WINDOW_NORMAL)
# cv2.imshow("black", imagenObscura)

# cv2.waitKey()
# cv2.destroyAllWindows()



# lista = [1,2,8,9,5,1,6,56,4,8]

# for elemento in lista:
#     print(elemento)

# print(lista[:])
# # print(lista[0:])
# # print(lista[5:])
# # print(lista[::-1])

# # lista[5:] = [1,1,1,1,1,1]
# # print(lista) 

# # lista[:]=[1,1,1,1,1,1]

# # print(lista) 

# print(lista[5:9])



# img = cv2.imread("candados.jpg") ## leemos la imagen de entrada y la guardamos en la variable img

# alto, largo, canales = img.shape ##obtenemos las dimensiones de la imagen

# print(alto, largo)

# candado1 = img[0:alto, 0:int(largo/2)] ## obtenemos los pixeles comprendidos desde 0 al total del alto de la imagen
# # y a su vez hasta la mitad del largo de la misma

# candado2 = img[0:alto, int(largo/2):] ##obtenemos los pixeles compresndidos desde 0 al total del alto de la imagen
# # y a su vez desde la mitad del largo de la misma hasta el final del largo.


# imagenCompuesta = np.zeros((alto, largo, canales), np.uint8) ## generamos una imagen de las mismas dimensiones
# #que la original y la rellenamos con ceros

# imagenCompuesta[0:alto, 0:int(largo/2)] = candado2 #remplazamos los pixeles de la primer mitad con la imagen
# #del candado 2
# imagenCompuesta[0:alto, int(largo/2):] = candado1## remplazamos los pixeles de la segunda mitad con la imagen del
# #candado 1

# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("candado1", cv2.WINDOW_NORMAL)
# cv2.namedWindow("candado2", cv2.WINDOW_NORMAL)
# cv2.namedWindow("imgCompuesta", cv2.WINDOW_NORMAL)

# cv2.imshow("original", img)
# cv2.imshow("candado1", candado1)
# cv2.imshow("candado2", candado2)
# cv2.imshow("imgCompuesta", imagenCompuesta)

# cv2.waitKey()
# cv2.destroyAllWindows()



img = cv2.imread("candados.jpg")

imgCopy = img.copy()

alto, largo, canales = img.shape

cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)

roi1 = cv2.selectROI("ROI", img)
print(roi1)

candado1 = img[int(roi1[1]) : int(roi1[1]+roi1[3]), int(roi1[0]) : int(roi1[0]+roi1[2])]
alto1, largo1, _ = candado1.shape
roi2 = cv2.selectROI("ROI", img)
print(roi2)

candado2 = img[int(roi2[1]) : int(roi2[1]+roi2[3]), int(roi2[0]) : int(roi2[0]+roi2[2])]
alto2, largo2, _ = candado2.shape

newCandado1 = cv2.resize(candado1, (largo2, alto2))
newCandado2 = cv2.resize(candado2, (largo1, alto1))

imgCopy[int(roi1[1]) : int(roi1[1]+ roi1[3]), int(roi1[0]) : int(roi1[0]+ roi1[2])] = newCandado2
imgCopy[int(roi2[1]) : int(roi2[1]+ roi2[3]), int(roi2[0]) : int(roi2[0]+ roi2[2])] = newCandado1                                                                
        

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado1", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado2", cv2.WINDOW_NORMAL)
cv2.namedWindow("imgCompuesta", cv2.WINDOW_NORMAL)

cv2.imshow("original", img)
cv2.imshow("candado1", candado1)
cv2.imshow("candado2", candado2)
cv2.imshow("imgCompuesta", imgCopy)

cv2.waitKey()
cv2.destroyAllWindows()
