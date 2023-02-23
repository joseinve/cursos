"""Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio"""

import math
def areaCuadrado(lado):
    areacua = lado**2
    return areacua

def areaCirculo(radio):
    areacir = math.pi* radio**2
    return areacir
lado=float(input("Ingrese el lado del cuadrado"))
print(areaCuadrado(lado))
radio=float(input("Ingrese el radio del circulo"))
print(areaCirculo(radio))