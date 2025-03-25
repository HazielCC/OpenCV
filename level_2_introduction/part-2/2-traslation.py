import cv2
import numpy as np

imagen = cv2.imread("pixels_llaves.jpg")
imagen_traslalada = cv2.resize(imagen, (300, 300))  # Cambiar tamaño de la imagen
alto, ancho, canales = imagen.shape  # Dimensiones

# * Mostrar imagen
cv2.imshow("Imagen", imagen)
cv2.imwrite("imagen_resized.jpg", imagen)  # Guardar imagen

# * Traslada la imagen
"""
Utilizando una matriz de traslación, se puede mover la imagen en el eje x y y.
La matriz de traslación es una matriz de 2x3, donde la primera fila es [1, 0, tx]
y la segunda fila es [0, 1, ty], donde tx y ty son los valores de traslación en x y y respectivamente.

Para trasladar la imagen en x = 100 y y = 50, se puede crear la siguiente matriz:
1 0 100
0 1 50
0 0 1
"""
tx = 100  # Traslación en x
ty = 50  # Traslación en y
# Matriz de traslación
translation = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8)
imagen_translated = np.zeros((alto + ty, ancho + tx, canales), np.uint8)

for i in range(alto):
    for j in range(ancho):
        px = np.array(([j, i, 1]), np.uint8)
        dot = np.dot(translation, px)
        x = dot[0]
        y = dot[1]
        imagen_translated[i, j] =

cv2.waitKey(0)
