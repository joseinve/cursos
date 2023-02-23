# Crear un programa con tres clases Universidad,
# con atributos nombre (Donde se almacena el nombre de la Universidad).
# Otra llamada Carerra, con los atributos especialidad .
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad.
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
class universidad:
    def __init__(self,nombre):
        self.nombreUni=nombre


class carrera():
    def carrera(self,especialidad):
        self.especialidad= especialidad

class estudiante(universidad,carrera):
    def datos(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        print("mi nombre es {} y tengo {} años, soy de la especialidad de {} de la universidad {}".format(self.nombre,self.edad,self.especialidad,self.nombreUni)) 

persona = estudiante("UNA")
persona.carrera("Informatica")
persona.datos("José", 18)