# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:20:15 2021

@author: Jesus-Mtz
"""
#
##operadores logicos: Son utilizados para formar expresiones que pueden ser resueltas y expresadas como True o False.

##Operador logico or

# x = False or False
# print(x)
# x = False or True
# print(x)
# x = True or False
# print(x)
# x = True or True
# print(x)

# ##Operador logico and
# x = False and False
# print(x)
# x = False and True
# print(x)
# x = True and False
# print(x)
# x = True and True
# print(x)

# ##Operador logico not
# x = not False
# print(x)
# x = not True
# print(x)


##Operadores relacionales: Son utilizados para comparar dos o mas valores, el resultado puede ser True o False

# ## Mayor que
# x = 2 > 1
# print(x)

# ## Menor que
# x = 2 < 1
# print(x)

# ## Mayor o igual que
# x = 2 >= 2
# print(x)
# x = 1 >= 2
# print(x)

# ## Menor o igual que
# x = 2 <= 2
# print(x)
# x = 3 <= 2
# print(x)

# ## igual que
# x = 2 == 2
# print(x)
# x = 3 == 2
# print(x)

# ## Diferente que
# x = 2 != 2
# print(x)
# x = 3 != 2
# print(x)

##Sentencia if: Es utilizada para ejecutar un bloque de codigo si, y solo si, se cumple determinada condición.
##Usado para la toma de decisiones

# x = 1
# if x == 1:
#     print("el valor de x es 1")
# else: # se ejecuta cuando la condición de la sentencia if da como resultado False
#     print("el valor de x no es 1")

# if x == 1:
#     print("el valor de x es 1")
# if x == 1:
#     print("el valor de x es 1")
    
# if x == 1:
#     print("el valor de x es 1")
# elif x == 1:
#     print("el valor de x es 1")




##Ciclos: Es una secuencia de instrucciones de codigo que se ejecuta repetidas veces, hasta que la condición asignada a dicho bucle deje de cumplirse

#Ciclo for: Se utiliza para recorrer los elementos de un objeto iterable, ejemplo una lista, tupla, conjunto o diccionario
#O para ejecutar un fragmento de codigo un numero finito de veces
#En cada iteración se utiliza solo un elemento del objeto iterable

# listadoDeEdades = [16, 20, 18, 5, 9, 23, 29]

# for edad in listadoDeEdades:
#     print(edad)
    
# for indice in range(len(listadoDeEdades)):
#     print(listadoDeEdades[indice])


# sumaDeEdades = 0
# for edad in listadoDeEdades:
#     sumaDeEdades = sumaDeEdades + edad
#     print(sumaDeEdades)

# for elemento in range(1,5):
#     print(elemento)
    
# for elemento in range(10):
#     print(elemento)
    
# for elemento in range(0, 100, 2):
#     print(elemento)
    
# listado = [2, 4, 5, 7, 8, 9, 3, 4]
# for elemento in listado:
#     if elemento == 3:
#         print("se ha encontrado un",elemento)
#         break
#     print(elemento)
    
# listado = [2, 4, 5, 7, 8, 9, 3, 4]
# for elemento in listado:
#     if elemento == 3:
#         print("se ha encontrado un",elemento)
#         break
#     print(elemento)
    
# listado = [2, 4, 5, 7, 8, 9, 4]
# elementoAEncontrar = 3
# for elemento in listado:
#     if elemento == elementoAEncontrar:
#         print("se ha encontrado un",elemento)
#         break
#     print(elemento)
# else:
#     print("No se encontró el numero", elementoAEncontrar)

##Ciclo while: Se utiliza para realizar multiples iteraciones de un fragmento de codigo
##esto basandonos en el resultado de una expresión lógica que puede tener como resultado un valor True o False

##Ciclo while controlado por conteo

# cuenta = 0
# while cuenta < 10:
#     cuenta = cuenta + 1
#     print (cuenta)


##Ciclo while controlado por evento

# numero = int(input("introdusca un numero, para salir introdusca un 0: "))
# while numero != 0:
#     print(numero)
#     numero = int(input("introdusca un numero, para salir introdusca un 0: "))


##Sentencia break en el ciclo while

# cuenta = 10
# while cuenta < 11:
#     cuenta = cuenta - 1
#     print (cuenta)
#     if cuenta == 3:
#         break
    

##Sentencia continue en el ciclo while

# cuenta = 10
# while cuenta < 11 :
#     cuenta = cuenta - 1
#     if cuenta == 3:
#         continue
#     if cuenta == 0:
#         break
#     print (cuenta)









