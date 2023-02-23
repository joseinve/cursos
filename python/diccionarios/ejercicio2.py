jugadores = {
    1: "Casillas",
    15: "Ramos",
    3: "Pique",
    5: "Puyol",
    11: "Capdevila",
    14: "Xabi Alonso",
    16: "Busquets",
    8: "Xavi Hernandez",
    18: "Pedrito",
    6: "Iniesta",
    7: "Villa",
}
num=float(input("ingrese un numero: "))
for i in jugadores:
    if i == num:
        existe = 1
        break
    else:
        existe = 0
if (existe == 1):
    print(jugadores[num])
else:
    print("No hay un jugador con ese numero en la lista")