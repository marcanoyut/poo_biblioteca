# main.py
import os
from datetime import datetime

# 1. IMPORTACIONES 
# clases raíz
from gestiona_materiales import Autor, Editorial, Libro, Revista
from gestiona_personas_biblio import Socio
from gestiona_prestamo_biblio import Prestamo


# 2. DEFINICIÓN DE LA CLASE PRINCIPAL
class Biblioteca(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.historial_prestamos = []

    def registrar_material(self, material):
        self.inventario.append(material)

    def emitir_prestamo(self, socio, material, dias):
        # REGLA DE NEGOCIO 1: Máximo 3 préstamos activos
        activos = [p for p in self.historial_prestamos if p.socio == socio and p.estado == "Activo"]
        if len(activos) >= 3:
            print(f"❌ Rechazado: {socio.nombre} ya tiene el límite de 3 materiales prestados.")
            return

        # REGLA DE NEGOCIO 2: Verificar disponibilidad
        if not material.disponible:
            print(f"❌ Rechazado: '{material.titulo}' ya está prestado.")
            return

        # Si pasa las reglas, se crea el objeto Préstamo (usa la clase importada)
        nuevo_p = Prestamo(socio, material, dias)
        self.historial_prestamos.append(nuevo_p)
        print(f"🎫 Préstamo Emitido con Éxito. Ticket ID: {nuevo_p.id_prestamo}")


# 3. --- PRUEBA DEL SISTEMA (SIMULACIÓN) ---
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    # 1. Instanciar la biblioteca central
    biblioteca_central = Biblioteca("DSOO Internacional")

    # 2. Registrar materiales en el inventario
    gabo = Autor("Gabriel García Márquez")
    sudamericana = Editorial("Editorial Sudamericana")

    l1 = Libro("Cien años de soledad", gabo, sudamericana)
    l2 = Libro("El amor en los tiempos del cólera", gabo, sudamericana)
    l3 = Libro("Crónica de una muerte anunciada", gabo, sudamericana)
    l4 = Libro("El coronel no tiene quien le escriba", gabo, sudamericana)
    r1 = Revista("National Geographic", 105, Editorial("RBA"))

    biblioteca_central.registrar_material(l1)
    biblioteca_central.registrar_material(l2)
    biblioteca_central.registrar_material(l3)
    biblioteca_central.registrar_material(l4)
    biblioteca_central.registrar_material(r1)

    # 3. Crear el socio para la prueba
    usuario = Socio("Yutzura Marcano", 95999888, "Socio-01")

    print(f"=== BIENVENIDO A LA BIBLIOTECA {biblioteca_central.nombre.upper()} ===\n")

    # 4. Operar los préstamos
    print("--- Intentando transacciones de prueba ---")
    biblioteca_central.emitir_prestamo(usuario, l1, 7)  # Préstamo 1 (Libro)
    biblioteca_central.emitir_prestamo(usuario, r1, 5)  # Préstamo 2 (Revista)
    biblioteca_central.emitir_prestamo(usuario, l2, 14) # Préstamo 3 (Libro)

    print("\n--- Intentando violar la Regla de Negocio (4to préstamo) ---")
    biblioteca_central.emitir_prestamo(usuario, l3, 7)  # Debería ser RECHAZADO por límite de 3

    print("\n--- Imprimiendo Tickets del Historial de Auditoría ---")
    for ticket in biblioteca_central.historial_prestamos:
        print("-" * 60)
        print(ticket)  # Llama automáticamente al método __str__ de tu clase Prestamo