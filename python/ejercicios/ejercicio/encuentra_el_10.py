c = input("Ingrese las notas de las tareas: ")
notas = c.split(",")
suma = 0
for i in range(len(notas)):
    suma += int(notas[i])
prom = suma/len(notas)
x = 0
while (True):
    if (prom < 9.5):
        x += 1
        suma += 10
        prom = suma/(len(notas)+x)
    else:
        print("Necesitas ", x, " tareas")
        break
# 8,9
# 9,10,10,9
