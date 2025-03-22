# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:16:49 2021

@author: Jesus-Mtz
"""

import cv2 ## importamos la libreria opencv

# ##Utilizando el comando imread de opencv, leeremos la imagen 1.jpeg y la guardaremos en la variable img
# img = cv2.imread("1.jpeg")
# ## Utilizando el comando imshow de opencv, mostraremos la imagen en una ventana llamada ventana1
# cv2.imshow("ventana1", img)
# ##Controla el timepo de muestreo de la señal de entrada por teclado
# cv2.waitKey()
# ## destruye o cierra las ventanas creadas por opencv
# cv2.destroyAllWindows()
# ##Guardamos la imagen contenida en la variable img en el archivo imagenGuardada1.jpeg
# cv2.imwrite("imagenGuardada1.jpeg", img)

# ##mandamos llamar la imagen 1.jpeg en escala de grises y la guardamos en la variable img
# img = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE) #tambien se puede remplazar cv2.IMREAD_GRAYSCALE por un 0 zero
# cv2.imshow("imagen en escala de grises", img)
# ##Controla el timepo de muestreo de la señal de entrada por teclado
# cv2.waitKey()
# ## destruye o cierra las ventanas creadas por opencv
# cv2.destroyAllWindows()
# ##Guardamos la imagen contenida en la variable img en el archivo imagenGuardada1.jpeg
# cv2.imwrite("imagenGuardada2.jpeg", img)

##Jugando con waitKey()

# img = cv2.imread("1.jpeg")
# img2 = cv2.imread("1.jpeg", 0)

# while True:
#     cv2.imshow("color", img)
#     cv2.imshow("grises", img2)
    
#     key = cv2.waitKey()
    
#     if key == ord("g"):
#         cv2.imwrite("imagenGuardada.png", img2)
        
#     elif key == ord("c"):
#         cv2.imwrite("imagenGuardada.png", img)    
        
#     else:
#         break
    
# cv2.destroyAllWindows()


img = cv2.imread("1.jpeg")
img2 = cv2.imread("1.jpeg",0)

# cv2.imshow("ventana", img) ## Mostramos la imagen en la ventana "ventana", es redimensionable pero no cambia su escala

# cv2.namedWindow("ventana", cv2.WND_PROP_FULLSCREEN) ## Aplicamos la propiedad full screen a la ventana

##Activamos la propiedad full screen
# cv2.setWindowProperty("ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) 
# cv2.setWindowProperty("ventana", 0, 1)

# cv2.namedWindow("ventana", cv2.WINDOW_NORMAL)## Esta propiedad nos permite redimensionar la ventana

# cv2.namedWindow("ventana", cv2.WINDOW_AUTOSIZE)

while True:
    
    key = cv2.waitKey()
    
    if key == ord("4"):
        cv2.imshow("ventana", img)
    elif key == ord("6"):
        cv2.imshow("ventana", img2)
    else:
        break
    
cv2.destroyAllWindows()




















