'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''
cantidad=int(input("Ingrese la cantidad: "))
iva=input("Ingrese el iva: ")
def ivacalc(cantidad,iva):
    if (iva != ''):
        iva=int(iva)/100
        cantidadIva=float(cantidad*(iva+1))
    else:
        cantidadIva=float(cantidad*1.21)
    return cantidadIva
ivacalc(cantidad, iva)
print(ivacalc(cantidad, iva))