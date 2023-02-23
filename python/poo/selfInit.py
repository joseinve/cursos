# class FabricaTelefonos:
#     marca = "Samsung"

#     def ElaborarHuawei(self):
#         self.marca = "Huawei"


# telefono = FabricaTelefonos()
# telefono.ElaborarHuawei()
# print(telefono.marca)


class FabricaTelefonos:
    def __init__(self, marca, color,almacenamiento):
        self.marca = marca
        self.color = color
        self.almacenamiento=almacenamiento


telefono = FabricaTelefonos("Huawei", "Negro","125Gb")
print(telefono.marca)
print(telefono.color)
print(telefono.almacenamiento)
