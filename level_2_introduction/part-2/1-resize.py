import cv2

image = cv2.imread("pixels_llaves.jpg")
image_translated = cv2.resize(image, (300, 300))  # Cambiar tamaño de la imagen
alto, ancho, canales = image.shape  # Dimensiones

# * Mostrar imagen
cv2.imshow("Imagen", image)
cv2.imwrite("imagen_resized.jpg", image)  # Guardar imagen
