from distutils.command import clean
from os import system
# Escribe un programa que pida dos palabras y diga si riman o no.
# Si coinciden las tres últimas letras tiene que decir que riman.
# Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
system("cls")
palabra1=input("ingrese una palabra:")
palabra2=input("ingrese una palabra:")
tamano1=palabra1.count
tamano2=palabra2.count
if palabra1[len(palabra1)-3: ] == palabra2[len(palabra2)-3: ]:
    print("Las palabras riman")
elif palabra1[len(palabra1)-2: ] == palabra2[len(palabra2)-2: ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")