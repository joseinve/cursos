"""Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas"""
lista = []


def ingresoDatos(lista):
    print("ingrese la cantidad de datos que llevara la lista")
    tamano = int(input())
    print("Ingrese los datos de la lista")
    for i in range(tamano):
        num = int(input())
        lista.append(num)


ingresoDatos(lista)


def ordenamiento(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print("Los numeros pares son")
    print(pares)
    print("Los numeros impares son")
    print(impares)


ordenamiento(lista)
