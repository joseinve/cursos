class animales():
    def __init__(self,mensaje):
        self.mensaje = mensaje
    def hablar (self):
        print(self.mensaje)

class perro(animales):
    def hablar(self):
        print("Yo hago guau")

class pez(animales):
    def hablar(self):
        print("Yo hago gluglu")

perro = perro("guau")
perro.hablar()
animal = animales("miau")
animal.hablar()
pez = pez("nada")
pez.hablar()