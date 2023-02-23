"""
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
"""


class fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    @property
    def llantas(self):
        return self._llantas

    @property
    def color(self):
        return self._color

    @property
    def precio(self):
        return self._precio


class moto(fabrica):
    pass


class auto(fabrica):
    pass


moto = moto(2, "negro", 17000000)
auto = auto(4, "gris", 60000000)

print(moto.llantas)
print(moto.color)
print(moto.precio)

print(auto.llantas)
print(auto.color)
print(auto.precio)
