import cv2
import numpy as np

candado_1 = cv2.imread("../candado.jpg")  # Se lee la imagen a color
candado_2 = cv2.imread("../candado-oxidado.jpg")  # Se lee la imagen a color
alto, largo, canales = candado_1.shape  # Se obtienen las dimensiones de la imagen

# Se recorre la imagen
candado1 = candado_1[0:alto, 0:int(largo/2)]
candado2 = candado_2[0:alto, int(largo/2):]


# Unir las dos imágenes
imagen_unida = np.zeros((int(alto), int(largo), int(canales)), np.uint8)
imagen_unida[0:alto, 0:int(largo/2)] = candado1
imagen_unida[0:alto, int(largo/2):] = candado2

cv2.namedWindow("candado", cv2.WINDOW_NORMAL)
cv2.imshow("Candado" ,imagen_unida)  # Se muestra la imagen
cv2.waitKey()  # Se espera a que se presione una tecla