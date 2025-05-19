import cv2  # Importamos OpenCV para manipular imágenes
import numpy as np  # Importamos NumPy para operaciones con matrices

# *** Carga y redimensionamiento de la imagen ***
image = cv2.imread("../../assets/pixels_llaves.jpg")  # Se lee la imagen original desde un archivo
new_image = cv2.resize(image, (300, 300))  # Se redimensiona la imagen a 300x300 píxeles
height, width, channels = (
    image.shape
)  # Se obtienen las dimensiones originales de la imagen

# *** Configuración de traslación de la imagen ***
# Se define el desplazamiento en ejes x e y
tx = 100  # Cantidad de desplazamiento en el eje x
ty = 50  # Cantidad de desplazamiento en el eje y

# Creamos la matriz de traslación de 3x3
translation = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.int32)

# Creamos una imagen vacía para almacenar la trasladada
imagen_translated = np.zeros((height + ty, width + tx, channels), np.uint8)

# *** Aplicación de la matriz de traslación a cada píxel de la imagen original ***
for i in range(height):  # Iteramos sobre las filas
    for j in range(width):  # Iteramos sobre las columnas
        px = np.array(([j, i, 1]), np.int32)  # Píxel actual en coordenadas homogéneas
        dot = np.dot(translation, px)  # Multiplicamos por la matriz de traslación
        x, y = dot[0], dot[1]  # Coordenadas del píxel trasladado

        # Asignamos el valor del píxel original a la nueva posición
        if y < imagen_translated.shape[0] and x < imagen_translated.shape[1]:
            imagen_translated[y, x] = image[i, j]

# *** Visualización de los resultados ***
cv2.namedWindow("org", cv2.WINDOW_NORMAL)  # Creamos una ventana para la imagen original
cv2.namedWindow("t", cv2.WINDOW_NORMAL)  # Creamos una ventana para la imagen trasladada

cv2.imshow("org", new_image)  # Mostramos la imagen redimensionada
cv2.imshow("t", imagen_translated)  # Mostramos la imagen trasladada

cv2.waitKey(0)  # Esperamos a que el usuario presione una tecla
cv2.destroyAllWindows()  # Cerramos las ventanas abiertas
