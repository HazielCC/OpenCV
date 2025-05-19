import cv2
import numpy as np

t_matrix = np.array(([1, 1, 0], [0, 1, 0], [0, 1, 1]), np.int32) # Matriz de traslación
image = cv2.imread("../../assets/pixels_llaves.jpg")  # Cargar imagen

height, width, channels = image.shape # Obtener dimensiones de la imagen
# Crear imagen vacía para almacenar la trasladada
translated_image = np.zeros((height, width, channels), np.uint8)
# Aplicar la matriz de traslación a cada píxel de la imagen original
for i in range(height): # Iterar sobre las filas
    for j in range(width): # Iterar sobre las columnas
        px = np.array(([j, i, 1]), np.int32) # Píxel actual en coordenadas homogéneas
        dot = np.dot(t_matrix, px) # Multiplicar por la matriz de traslación
        x, y = dot[0], dot[1] # Coordenadas del píxel trasladado

        # Asignar el valor del píxel original a la nueva posición
        if y < translated_image.shape[0] and x < translated_image.shape[1]:
            translated_image[y, x] = image[i, j]

# Mostrar imagen original y trasladada
cv2.namedWindow("org", cv2.WINDOW_NORMAL) # Crear ventana para la imagen original
cv2.imshow("org", image) # Mostrar imagen original
cv2.namedWindow("t", cv2.WINDOW_NORMAL) # Crear ventana para la imagen trasladada
cv2.imshow("t", translated_image) # Mostrar imagen trasladada
cv2.waitKey(0) # Esperar a que el usuario presione una tecla