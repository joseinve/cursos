from distutils.command import clean
from os import system
# Crear un programa que permita al usuario elegir un candidato por el cual votar. 
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
# Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”.
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
system("cls")
print("Los candidatos son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.")
candidato=input("Eliga un candidato:")
if candidato.upper() == "A":
    print("Usted ha votado por el partido Rojo")
elif candidato.upper() == "B":
    print("Usted ha votado por el partido Verde")
elif candidato.upper() == "C":
    print("Usted ha votado por el partido Azul")
else:
    print("Opcion erronea")