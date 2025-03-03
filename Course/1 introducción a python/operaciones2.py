# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:18:37 2021

@author: Jesus-Mtz
"""


def promedio(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    promedio = suma / len(lista)
    return promedio, suma



            
def moda(listado):
    listaConteo = []
    for elemento in listado:
        cuenta = 0
        for elemento2 in listado:
            if elemento == elemento2:
                cuenta = cuenta + 1
            
        listaConteo.append(cuenta)
        
    mayor = listaConteo[0]
    for elemento in listaConteo:
        if elemento > mayor:
            mayor = elemento
            
    for index in range(len(listaConteo)):
        if listaConteo[index] == mayor:
            moda = listado[index]
            break

    return moda   
    