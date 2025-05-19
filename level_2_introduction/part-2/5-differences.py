import cv2

img_1 = cv2.imread("happy_face.png")
img_2 = cv2.imread("happy_face_no.png")

img_1 = cv2.resize(img_1, (300, 300))
img_2 = cv2.resize(img_2, (300, 300))

# * Diferencia entre imágenes
img_diff = cv2.absdiff(img_1, img_2)  # Diferencia entre imágenes
# * Diferencia entre imágenes en escala de grises
img_diff_gray = cv2.absdiff(cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY),
                            cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY))  # Diferencia entre imágenes en escala de grises
# * Diferencia entre imágenes en escala de grises con umbral
_, img_diff_gray = cv2.threshold(img_diff_gray, 50, 255,
                                 cv2.THRESH_BINARY)  # Diferencia entre imágenes en escala de grises con umbral
# * Diferencia entre imágenes en escala de grises con umbral y dilatación
img_diff_gray = cv2.dilate(img_diff_gray, None,
                           iterations=2)  # Diferencia entre imágenes en escala de grises con umbral y dilatación

cv2.imshow("Diferencia", img_diff)  # Mostrar imagen
cv2.imshow("Diferencia en escala de grises", img_diff_gray)  # Mostrar imagen
cv2.imshow("Diferencia en escala de grises con umbral", img_diff_gray)  # Mostrar imagen
cv2.imshow("Diferencia en escala de grises con umbral y dilatación", img_diff_gray)  # Mostrar imagen

cv2.waitKey(0)  # Esperar a que se presione una tecla
