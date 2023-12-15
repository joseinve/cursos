n = int(input("Número de lomos queso a preparar: "))
tiempo_coccion = 20 * 4
print("Luís tardará {} segundos en preparar lomos queso.".format(
    (((n + 3) // 4) * tiempo_coccion)))
