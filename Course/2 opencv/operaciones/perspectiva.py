# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:12:29 2021

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# tMatrix = np.array([[1,1,0], [0,1,0], [0,1,1]]) ## construimos la matríz de transformación
# mResultante = np.zeros((500,500,3), np.uint8) ## contruimos la matriz resultante

# imagen = cv2.imread("1.png") ## cargamos la imagen a transformar

# h, w, c = imagen.shape ## obtenemos las dimensiones de la imagen a transformar

# for i in range(h):
#     for j in range(w):
#         pixel = imagen[i,j]
#         vector = np.array([j,i,1]) ## construimos el vector posición
#         result = np.dot(tMatrix, vector) ## calculamos el producto punto, resultado de aplicar la transformación
#         x = result[0]
#         y = result[1]
#         mResultante[y,x] = pixel

# cv2.imshow("org", imagen)
# cv2.imshow("t", mResultante)

# cv2.waitKey()
# cv2.destroyAllWindows()

## bloque 1
img = cv2.imread("mural.jpg") ## leemos la imagen a trabajar
h, w, ch = img.shape ## obtenemos sus dimensiones

cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL) ## generamos una ventana con la que trabajaremos
########################################################################################################

## bloque 4 generamos la variable global listaPuntos para poderla utilizar tanto fuera como dentro de la funcion
global listaPuntos
listaPuntos=[] ## inicializamos listaPuntos vacia
##############################################################################

#bloque 3  event, x,y, flags, params van por default
def obtenerPuntos(event, x, y, flags, params): ## construimos la función para trabajar con cv2.setMouseCallback

    if event == cv2.EVENT_LBUTTONDBLCLK: ##leemos el evento del mouse, registrado por setMouseCallback
    ## si event == doble click izq
        # print('ddd')
        listaPuntos.append([x,y]) ## agregamos las posiciones de x, y a una lista y esa lista la agregamos
        # a listaPuntos
###############################################################################################################


######### bloque 2
cv2.setMouseCallback("imagen1", obtenerPuntos) ## utilizamos la función setMouseCallback
#####################################################################################################


## bloque 5
cv2.imshow("imagen1", img) ## mostramos la imagen con la que trabajaremos en la ventana "imagen1"

while True: ## generamos un ciclo While "infinito"

    if cv2.waitKey(0) == 13: #si la tecla presionada es "enter" ejecuta el bloque identado (13 en ascii es enter)
        print(listaPuntos) ## imprimimos la lista de puntos
        ## puntos seleccionados de la imagen a transformar
        pts1 = np.float32(listaPuntos) ## convertimos la lista en un vector con tipo de dato float32

        pts2 = np.float32([[0,0], [w, 0], [0, h], [w,h]]) ## definimos los puntos donde debe quedar la imagen
        #transformada

        M = cv2.getPerspectiveTransform(pts1, pts2)
        resultadoImagen = cv2.warpPerspective(img, M, (w,h))
        cv2.imshow("imagen1", resultadoImagen)

    if cv2.waitKey(0) == 27: ## esc en ascii es 27
        break

cv2.destroyAllWindows()


