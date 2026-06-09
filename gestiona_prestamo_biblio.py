# prestamos.py
from datetime import datetime, timedelta

class Prestamo(object):
    _next_id = 1

    def __init__(self, socio, material, dias_prestamo=14):
        self.id_prestamo = Prestamo._next_id
        self.socio = socio          # Recibe un objeto Socio
        self.material = material    # Recibe un objeto Libro o Revista (Polimorfismo)
        self.dias_prestamo = dias_prestamo
        self.fecha_salida = datetime.now()
        self.estado = "Activo"

        # Al nacer el préstamo, el material se bloquea automáticamente
        self.material.disponible = False
        Prestamo._next_id += 1

    def obtener_fecha_vencimiento(self):
        return self.fecha_salida + timedelta(days=self.dias_prestamo)

    def esta_vencido(self):
        if self.estado == "Devuelto":
            return False
        return datetime.now() > self.obtener_fecha_vencimiento()

    def registrar_devolucion(self):
        self.estado = "Devuelto"
        self.material.disponible = True  # Libera el material

    def __str__(self):
        f_salida = self.fecha_salida.strftime('%d/%m/%Y')
        f_vence = self.obtener_fecha_vencimiento().strftime('%d/%m/%Y')
        status = "🔴 VENCIDO" if self.esta_vencido() else f"🟢 {self.estado}"

        return (f"Ticket N°: {self.id_prestamo} | Socio: {self.socio.nombre}\n"
                f"  Material: {self.material.obtener_detalles()}\n"
                f"  Retiro: {f_salida} | Vence: {f_vence} | Estado: {status}")