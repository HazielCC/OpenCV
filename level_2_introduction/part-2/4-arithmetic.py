import cv2

img_1 = cv2.imread("../../assets/happy_face.png")
img_2 = cv2.imread("../../assets/hola.png")

img_1 = cv2.resize(img_1, (300, 300))
img_2 = cv2.resize(img_2, (300, 300))

# * Sumar imágenes
img_sum = cv2.add(img_1, img_2)  # Sumar imágenes
# * Restar imágenes
img_sub = cv2.subtract(img_1, img_2)  # Restar imágenes
# * Multiplicar imágenes
img_mul = cv2.multiply(img_1, img_2)  # Multiplicar imágenes
# * Dividir imágenes
img_div = cv2.divide(img_1, img_2)  # Dividir imágenes

cv2.imshow("Suma", img_sum)  # Mostrar imagen
cv2.imshow("Resta", img_sub)  # Mostrar imagen
cv2.imshow("Multiplicación", img_mul)  # Mostrar imagen
cv2.imshow("División", img_div)  # Mostrar imagen
cv2.waitKey(0)  # Esperar a que se presione una tecla
