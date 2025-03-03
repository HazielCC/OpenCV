# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:23:56 2021

@author: Jesus-Mtz
"""

##importar la libreria de numpy

# import numpy as np

##Crear un vector apartir de una lista

# listado = [1,2,3,4,5,6]
# vector = np.array(listado)
# print(type(vector), vector)
# print("\n")

##Operaciones con vectores

# print("vector: ",vector)
# print("\n")

# print("Sumando 1 a cada elemento del vector:")
# print(vector+1)
# print("\n")

# print("Multiplicar por 2 cada elementro del vector")
# print(vector*2)
# print("\n")

# print("Sumar los elementos del vector: ")
# print(np.sum(vector))
# print("\n")

# print("promedio (media) de los elementos: ")
# print(np.mean(vector)) 
# print("\n")

# print("Sumando dos vectores del mismo tamaño: ")
# vector2=np.array([11,55,1.2,-8,3,5])
# print(vector+vector2)
# print("\n")

##Acceder a un elemento de un vector:
    
# elemento = vector[1]
# print(elemento)

# elemento = vector[5]
# print(elemento)

# print(vector[:]) #imprimir todos los elementos del vector

# print(vector[1:]) #imprimir todos los elementos del vector despues del 1er elemento

# print(vector[-1]) #imprimir el ultimo elemento del vector

# print(vector[::-1]) #imprimir el vector en orden invertido

##Remplazar elemento de un vector

# vector[4] = 0
# print(vector)

# vector[:] = 0
# print(vector)

##Recorrer un vector

# for elemento in vector:
#     print(elemento)

# for elemento in vector[::-1]:
#     print(elemento)


##Creación de una matriz apartir de una lista de listas

# listado = [[1,2,3,4,5], [45, 6, 7, 2, 3], [9, 7, 15, 52, 0], [15, 20, 1, 3, 8]]
# matriz = np.array(listado)
# print(type(matriz))
# print(matriz)
# print("\n")

# ##Crear matríz con solo ceros
# dimensiones=(3,3)
# matrizSoloCeros = np.zeros(dimensiones)
# print(matrizSoloCeros)
# print("\n")

# ##Crear matriz con solo unos
# dimensiones=(3,3)
# matrizSoloCeros = np.ones(dimensiones)
# print(matrizSoloCeros)
# print("\n")


##Accediendo a los elementos de una matriz

# print(matriz[0,0]) #Elemento 0 con 0 de la matriz

# print(matriz[2,1]) #Elemento 2 con 1 de la matriz

# print(matriz[1,:]) #elementos de la fila 1 

# print(matriz[:,2]) #elementos de la columna 2


##Modificando elementos de una matriz

# matriz[0,1] =5 #modificar elemento de la fila 0 columna 1
# print(matriz)

# matriz[:,-1] =200 #modificar todos los elementos de la ultima co1umna
# print(matriz)

# matriz[-1,:] =100 #modificar todos los elementos de la ultima fila
# print(matriz)


##Recorrer matriz con ciclo for

# filas, columnas = matriz.shape

# for i in range(filas):
#     for j in range(columnas):
#         print(matriz[i,j])