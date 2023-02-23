"""Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota 
y si ha aprobado o no."""


class estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
        if nota > 1:
            self._aprobado = "Está aprobado"
        else:
            self._aprobado = "No está aprobado"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    @property
    def aprobado(self):
        return self._aprobado


alumno1 = estudiante("Jose", 2)
print(alumno1.nombre)
print(alumno1.nota)
print(alumno1.aprobado)
