# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:20:38 2021

@author: Jesus-Mtz
"""

"""Funciones: Es un bloque de codigo al cual se le asigna un nombre, puede recibir varios argumentos como entrada o ninguno, 
    esta función ejecuta una secuencia de sentencias y pueden retornar o no un valor, ademas pueden ser llamados cuando se les necesite 
"""

""" Permiten modular el codigo o estructurarlo en segmentos mas simples, facilitando así la programación y depuración, ademas
    permite la reutilización de codigo en distintos programas 
"""

## para definir una función utilizaremos la sentencia def, ejemplo:
    
# def miPrimerFuncion():
#     print("Hola mundo")
    
# miPrimerFuncion()

## enviar argumentos a una función:
    
# def suma(x, y):
#     resultado = x + y
#     print(resultado)
    
# suma(5, 8)


## Retornar valores desde una función:
    
# def suma(x, y):
#     resultado = x + y
#     return resultado

# resultadoSuma = suma(1, 9)
# print(resultadoSuma)


## argumentos por nombre:
    
# def resta(x, y):
#     resultado = x - y
#     return resultado

# resultadoResta = resta(y = 1, x = 9)
# print(resultadoResta)