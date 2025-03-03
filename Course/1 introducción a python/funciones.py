# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:53:11 2021

@author: Jesus-Mtz
"""

#Funciones

""" Es un bloque de codigo al cual se le asigna un nombre, puede o no recibir varios argumentos como entrada,
    la función ejecuta una secuencia de sentencias y púede retornar o no un valor, ademas puede ser utilizada o
    mandada a llamar en cualquier parte del codigo
    
    permite modular el codigo o estructurarlo en segmentos mas simples y faciles de entender.
    Facilita la depuración y la reutilización de codigo en distintos programas

"""

## para definir una función vamos a utilizar la sentencia def, ejemplo:
    
# def miPrimerFuncion():
#     print("hola mundo")

# for x in range(100):
#     miPrimerFuncion()


##Enviar argumentos a una función

# def suma(x, y):
#     sumatoria = x + y
#     print(sumatoria)


# for x in range(10):    
#     suma(x, x)

## enviar y recibir argumentos de una función


def suma(x, y):
    sumatoria = x + y
    return sumatoria


for x in range(10):    
    resultado = suma(x, x)
    print(resultado)