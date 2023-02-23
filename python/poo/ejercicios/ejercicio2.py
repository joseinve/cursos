"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
"""


class calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        sumar = self.valor1 + self.valor2
        print(sumar)

    def resta(self):
        rest = self.valor1 - self.valor2
        print(rest)

    def multiplicación(self):
        mult = self.valor1 * self.valor2
        print(mult)

    def divición(self):
        div = self.valor1 / self.valor2
        print(div)


operaciones = calculadora()
operaciones.suma()
operaciones.resta()
operaciones.multiplicación()
operaciones.divición()
