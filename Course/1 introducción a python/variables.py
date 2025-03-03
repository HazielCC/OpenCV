# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:02:33 2021

@author: Jesus-Mtz
"""

##Variables y constantes:

#Los nombres de las variables pueden contener letras, numeros y guiones bajos
#El nombre de una variable puede comenzar con una letra o un guion bajo, pero no puede comenzar con un numero
#El software puede defierenciar entre minusculas y mayusculas: no es lo mismo escuela que Escuela, carro que CaRro
#Notación recomendada camelCase, ejemplo: nombreEscuelaPreparatoria, nombrePersona, llantasCarro

#Ejemplos:
    
# valor1 = 5
# valor2 = 8

# print(valor1)
# print(valor2)
# print(valor1, valor2)
# print(valor2, valor1)

# print("La suma de estas dos variables es: ", valor1 + valor2)
# print("La resta de estas dos variables es: ", valor2 - valor1)

# cadenaSuma = "La suma de estas dos variables es: "
# cadenaResta = "La resta de estas dos variables es: "

# suma = valor1 + valor2
# resta = valor2 - valor1

# print(cadenaSuma, suma)
# print(cadenaResta, resta)

#Utilización de cadenas:

# nombrePersona = "Jesús"
# apellidoPersona = "Martínez"

# print("Mi nombre es: ", nombrePersona )
# print("Mi apellido es: ", apellidoPersona)
# print("Mi nombre completo es: ", nombrePersona + " " + apellidoPersona ) ## concatenación de cadenas
# nombreCompleto = nombrePersona + " " + apellidoPersona ## concatenación de cadenas
# print("Mi nombre completo es: ", nombreCompleto)
# print("Mi nombre es {0} y mi apellido es {1}".format(nombrePersona, apellidoPersona))
# print("Mi nombre es {nombre} y mi apellido es {apellido}".format(nombre = nombrePersona, apellido = apellidoPersona))

#Función input: ## nos permite recoger datos ingresados por teclado
    
# nombreCompleto = input("ingresa tu nombre completo: ")

# print(nombreCompleto)

# numero1 = input("Ingresa el valor 1: ")
# numero2 = input("Ingresa el valor 2: ")

# suma = int(numero1) + int(numero2)

# print(suma)

# numero1 = int(input("Ingresa el valor 1: "))
# numero2 = int(input("Ingresa el valor 2: "))

# suma = numero1 + numero2

# print(suma)

# nombrePersona = input("Ingresa tu nombre: ")
# edadPersona = int(input("Ingresa tu edad: "))

# print("Tu nombre es: {0} y tienes {1} años".format(nombrePersona, edadPersona))


from modulos.x import *

print(pi)
print(contraseña)
print(direccion)

print(pi + pi)
print(direccion+contraseña)
print(pi+int(contraseña))

# escuela = "escuela 1"
# Escuela = "escuela 2"

# print(escuela, Escuela)

