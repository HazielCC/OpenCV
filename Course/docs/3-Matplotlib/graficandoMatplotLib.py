# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:25:01 2021

@author: Jesus-Mtz
"""

##Importamos la libreria matplotlib con el modulo pyplot
import matplotlib.pyplot as plt

#Creamos la figura y los ejes 
fig, ax = plt.subplots()

#Dibujamos puntos en el plano(diagrama de disperción)
ax.scatter([1, 2, 3, 4], [1, 2, 0, 0.5])

#Mostramos el grafico
plt.show()

#Diagrama de lineas

#Creamos la figura y los ejes 
fig, ax = plt.subplots()

#Dibujamos el diagrama de lineas
ax.plot([20, 25, 40, 50], [20, 55, 33, 30])

#Mostramos el grafico
plt.show()

#Creación de un diagrama de barras verticales

#Creamos la figura y los ejes 
fig, ax = plt.subplots()

#Dibujamos el diagrama de barras
ax.bar([1, 2, 3], [500, 150, 45])

#Mostramos el grafico
plt.show()

