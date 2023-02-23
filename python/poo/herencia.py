class animales():
    def __init__(self,nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre
class perro(animales):
    def __init__(self,nombre,sonido):
        super().__init__(nombre)
        self._sonido = sonido
    @property
    def sonido(self):
        return self._sonido
perro = perro("firulais","guau")
print(perro.nombre)
print(perro.sonido)