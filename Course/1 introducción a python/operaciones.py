# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:04:52 2021

@author: Jesus-Mtz
"""

# def suma(x, y):
#     suma = x + y
#     return suma


# def resta(x, y):
#     resta = x - y
#     return resta


# def division(x, y):
#     division = x /y
#     return division


# def contador(limite):
#     cuenta = 0
#     while cuenta < limite:
#         cuenta = cuenta + 1
#         print(cuenta)
        
def promedio(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    
    promedio = suma / len(lista)
    return promedio, suma



def moda(lista):
    listaConteo = []
    
    for elemento in lista:
        cuenta = 0
        for index in lista:
            if elemento == index:
                cuenta = cuenta +1
                
        listaConteo.append(cuenta)
    mayor = lista[0]    
    for elemento in listaConteo:
        if elemento > mayor:
            mayor = elemento
            
    for x in range(len(listaConteo)):
        if listaConteo[x] == mayor:
            moda = lista[x]
            break
            
    return moda
            