import cv2

imagen = cv2.imread("pixels_llaves.jpg")
imagen_traslalada = cv2.resize(imagen, (300, 300))  # Cambiar tamaño de la imagen
alto, ancho, canales = imagen.shape  # Dimensiones

# * Mostrar imagen
cv2.imshow("Imagen", imagen)
cv2.imwrite("imagen_resized.jpg", imagen)  # Guardar imagen
