class FabricaTelefonos:
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje
    def escucharMusica(self):
        print("Estás escuchando Música")


telefono = FabricaTelefonos()
telefono.color
telefono.memoriaRam
telefono.almacenamiento
print(telefono.marca)
print(telefono.llamar("Hola, ¿Con quien hablo?"))
telefono.escucharMusica()
