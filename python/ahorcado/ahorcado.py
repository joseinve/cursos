# juego de ahorcados
from distutils.command import clean
from os import system
from figurita import figurita
while True:
    system("cls")
    letrasErroneas = ""
    vidas = 6
    palabra = input("Ingrese la palabra:")
    tamano = len(palabra)
    restante = tamano
    incognita = "_" * tamano
    system("cls")

    while vidas > 0 and restante > 0:
        acierto = False
        figurita(vidas)

        print(f"vida:{vidas}")
        print(incognita)
        print(f"Letras erroneas ingresadas: {letrasErroneas}")
        letra = input("Ingrese una letra:")
        for i in range(0, tamano):
            if letra.lower() == palabra[i].lower() and incognita[i] == "_":
                incognita = incognita[:i] + letra + incognita[i + 1 :]
                acierto = True
                restante -= 1

        if not acierto:
            vidas -= 1
            if vidas ==5:
                letrasErroneas = letrasErroneas + letra
            else:
                    letrasErroneas = letrasErroneas + ", " + letra

            print(incognita)
        system("cls")

    if vidas == 0:
        print(f"La palabra era {palabra}")
        figurita(vidas)
    
        input("Usted ha perdido, presione cualquier tecla para reintentar")
    if restante == 0:
        input("Has ganado, presione cualquier tecla para continuar")
