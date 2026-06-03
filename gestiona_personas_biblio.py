# gestiona_personas_biblioteca

class Persona(object):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni


class Socio(Persona):
    def __init__(self, nombre, dni, nro_socio):
        super().__init__(nombre, dni)
        self.nro_socio = nro_socio


class Bibliotecario(Persona):
    def __init__(self, nombre, dni, legajo):
        super().__init__(nombre, dni)
        self.legajo = legajo