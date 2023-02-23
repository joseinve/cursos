meses = (
    "Enero",
    "Febreo",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Setiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)
mes=round(float(input("ingrese un numero entre 1 y 12:")))
if(mes<13 and mes > -0):
    print(meses[mes-1])
elif(mes>11):
    print("El numero no debe ser mayor a 12")
elif(mes<1):
    print("El numero no debe ser menor a 1")