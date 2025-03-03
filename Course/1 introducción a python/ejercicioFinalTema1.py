# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:16:41 2021

@author: Jesus-Mtz
"""

import operaciones2

lista = []
cuenta = 0

while cuenta < 10:
    cuenta = cuenta + 1
    numero = int(input("ingresa un numero: "))
    lista.append(numero)
    
print(lista)

promedio, suma = operaciones2.promedio(lista)
moda = operaciones2.moda(lista)

print(promedio, suma, moda)
