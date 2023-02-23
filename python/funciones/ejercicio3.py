"""Crear una funcion que pida dos numeros. 
Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
si el segundo es mayor al primero, debe retornar -1; 
si ambos son iguales, debe retornar 0"""


def condicion(num1,num2):
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0


num1 = input("Ingrese el primer valor: ")
num2 = input("Ingrese el segundo valor: ")
print(condicion(num1, num2))