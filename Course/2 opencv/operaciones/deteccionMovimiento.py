# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:01:57 2021

@author: Jesus-Mtz
"""

import cv2 ## importamos la libreria opencv

cap = cv2.VideoCapture(1) ## mandamos llamar la camara 1 y guardamos sus configuraciones en cap

conteo = 0 ##inicializamos un conteo en 0

while True: ## definimos un ciclo "infinito"
    ret, frame = cap.read() ## leemos u obtenemos las capturas de la camara
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## convertimos la captura a escala de grises
    
    if conteo == 10:  ## si el conteo es 10 guarda la imagen como fondo
        fondo = gris ## fondo es igual a la imagen en escala de grises
        
    if conteo > 10: ## si el conteo es mayor a 10 realiza lo siguiente
        dif = cv2.absdiff(gris, fondo) ## realizamos la resta de el fondo a la imagen actual tomada
        
        _, imagenBinarizada = cv2.threshold(dif, 15, 255, cv2.THRESH_BINARY) ## REALIZAMOS LA BINARIZACIÓN DE 
        #LA IMAGEN
        
        ## ADQUIRIMOS LOS CONTORNOS DE LA IMAGEN
        contornos, _ = cv2.findContours(imagenBinarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contorno in contornos:
            area = cv2.contourArea(contorno) ## calculamos el area del contorno
            
            if area > 900:
                x, y, w ,h = cv2.boundingRect(contorno)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
                
    
    cv2.imshow("frame", frame)
        
    conteo = conteo +1
    
    if cv2.waitKey(1) == 13:
        break
    
cap.release()
cv2.destroyAllWindows()