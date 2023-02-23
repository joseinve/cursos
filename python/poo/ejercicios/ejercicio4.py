# Crear una clase llamada Marino(), con un metodo que sea hablar,
# en donde muestre un mensaje que diga "Hola...".
# Luego, crear una clase Pulpo() que herede Marino,
# pero modificar el mensaje de hablar por "Soy un Pulpo".
# Por ultimo, crear una clase Foca(), heredada de Marino,
# pero que tenga un atributo nuevo llamado mensaje,
# que muestre ese mesaje como parametro
class marino:
    def hablar(self):
        print("Hola soy un marino")


class pulpo(marino):
    def hablar(self):
        print("Soy un pulpo")


class foca(marino):
    _mensaje = "Soy una foca"
    def __init__(self):
        self._mensaje
    @property
    def mensaje(self):
        return self._mensaje

marino=marino()
pulpo=pulpo()
foca=foca()
marino.hablar()
pulpo.hablar()
print(foca.mensaje)