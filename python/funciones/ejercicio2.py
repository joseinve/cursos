def factoriales(numpar):
    factorial = 1
    for i in range(1,numpar+1):
        factorial = factorial * i
    print(factorial)


numpar = int(input("Ingrese un numero par: "))
if numpar % 2 != 0:
    print("El numero debe ser par")
else:
    factoriales(numpar)
