capitales = {
    "Guatemala": "Ciudad de Guatemala",
    "El Salvador": "San Salvador",
    "Honduras": "Honduras",
    "Nicaragua": "Managua",
    "Costa Rica": "San Jose",
    "Panama": "Panama",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Venezuela": "Caracas",
    "España": "Madrid",
}
pais = input("Ingrese un pais: ")
pais = pais[0].upper() + pais[1:]
tamano = len(capitales)
for i in capitales:
    if i == pais:
        existe = 1
        break
    else:
        existe = 0
if existe == 1:
    print(capitales[pais])
else:
    print("El país ingresado no existe en la lista")
