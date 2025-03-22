import cv2

# Se obtiene la ruta del archivo actual
llaves = cv2.imread("pixels_llaves.jpg")  # Se lee la imagen a color
llaves_copy = llaves.copy()  # Se crea una copia de la imagen
alto, largo, canales = llaves.shape  # Se obtienen las dimensiones de la imagen

""" Seleccionar la región de interés de la imagen "(llave_1)" """
cv2.namedWindow("llaves", cv2.WINDOW_NORMAL)  # Se crea una ventana
roi_llaves = cv2.selectROI("llaves", llaves)
print(roi_llaves)

# Se obtiene la región de interés de la imagen
llave1 = llaves[
    roi_llaves[1] : roi_llaves[1] + roi_llaves[3],
    roi_llaves[0] : roi_llaves[0] + roi_llaves[2],
]
# Se obtienen las dimensiones de la imagen
alto_llave1, largo_llave1, canales_llave1 = llave1.shape

""" Seleccionar la región de interés de la imagen "(llave_2)" """
roi_llave_2 = cv2.selectROI("llave_2", llaves)
print(roi_llave_2)

# Se obtiene la región de interés de la imagen
llave2 = llaves[
    roi_llave_2[1] : roi_llave_2[1] + roi_llave_2[3],
    roi_llave_2[0] : roi_llave_2[0] + roi_llave_2[2],
]
# Se obtienen las dimensiones de la imagen
alto_llave2, largo_llave2, canales_llave2 = llave2.shape

""" Mostrar la imagen con la región de interés seleccionada """
nueva_llave_1 = cv2.resize(llave1, (largo_llave2, alto_llave2))
nueva_llave_2 = cv2.resize(llave2, (largo_llave1, alto_llave1))

# Se copian las nuevas llaves en la imagen original
llaves_copy[
    roi_llaves[1] : roi_llaves[1] + roi_llaves[3],
    roi_llaves[0] : roi_llaves[0] + roi_llaves[2],
] = nueva_llave_1

llaves_copy[
    roi_llave_2[1] : roi_llave_2[1] + roi_llave_2[3],
    roi_llave_2[0] : roi_llave_2[0] + roi_llave_2[2],
] = nueva_llave_2

cv2.imshow("llaves", llaves_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
