import cv2  # Importamos OpenCV para procesamiento de imágenes

# *** Carga y copia de la imagen ***
llaves = cv2.imread("pixels_llaves.jpg")  # Se lee la imagen original
llaves_copy = llaves.copy()  # Se crea una copia de la imagen
alto, largo, canales = llaves.shape  # Se obtienen las dimensiones de la imagen

# *** Selección de la región de interés (ROI) para la llave 1 ***
cv2.namedWindow("llaves_1", cv2.WINDOW_NORMAL)  # Se crea una ventana para la selección
roi_llaves = cv2.selectROI("llaves_1", llaves)  # Seleccionamos ROI en la ventana
print("ROI llave 1:", roi_llaves)  # Mostramos las coordenadas del ROI seleccionada

# Extraemos la región seleccionada para la llave 1
llave1 = llaves[
    roi_llaves[1] : roi_llaves[1] + roi_llaves[3],  # Alto
    roi_llaves[0] : roi_llaves[0] + roi_llaves[2],  # Ancho
]

# *** Selección de la región de interés (ROI) para la llave 2 ***
cv2.namedWindow("llaves_2", cv2.WINDOW_NORMAL)  # Se crea una ventana para la selección
roi_llave_2 = cv2.selectROI("llaves_2", llaves)  # Seleccionamos otro ROI en la ventana
print("ROI llave 2:", roi_llave_2)  # Mostramos las coordenadas del ROI seleccionada

# Extraemos la región seleccionada para la llave 2
llave2 = llaves[
    roi_llave_2[1] : roi_llave_2[1] + roi_llave_2[3],  # Alto
    roi_llave_2[0] : roi_llave_2[0] + roi_llave_2[2],  # Ancho
]

# *** Procesamiento: Ajustar dimensiones de las llaves ***
alto_llave1, largo_llave1, canales_llave1 = llave1.shape  # Dimensiones de llave 1
alto_llave2, largo_llave2, canales_llave2 = llave2.shape  # Dimensiones de llave 2

# Redimensionamos cada llave al tamaño de la otra región
nueva_llave_1 = cv2.resize(
    llave1, (largo_llave2, alto_llave2)
)  # Llave 1 al tamaño de llave 2
nueva_llave_2 = cv2.resize(
    llave2, (largo_llave1, alto_llave1)
)  # Llave 2 al tamaño de llave 1

# *** Intercambio de contenido en la imagen copiada ***
llaves_copy[
    roi_llaves[1] : roi_llaves[1] + nueva_llave_2.shape[0],  # Alto
    roi_llaves[0] : roi_llaves[0] + nueva_llave_2.shape[1],  # Ancho
] = nueva_llave_2  # Copiamos nueva llave 2 en la región de llave 1

llaves_copy[
    roi_llave_2[1] : roi_llave_2[1] + nueva_llave_1.shape[0],  # Alto
    roi_llave_2[0] : roi_llave_2[0] + nueva_llave_1.shape[1],  # Ancho
] = nueva_llave_1  # Copiamos nueva llave 1 en la región de llave 2

# *** Mostrar la imagen resultante ***
cv2.imshow("llaves_unidas", llaves_copy)  # Mostramos el resultado en una ventana
cv2.waitKey(0)  # Esperamos a que se pulse una tecla
cv2.destroyAllWindows()  # Cerramos todas las ventanas
