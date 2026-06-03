# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    # 1. Instanciar la biblioteca central
    biblioteca_central = Biblioteca("DSOO Internacional")

    # 2. Registrar materiales en el inventario (Composición)
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

    # 3. Crear un socio
    usuario = Socio("Yutzura Marcano", 95999888, "Socio-01")

    print(f"=== BIENVENIDO A LA BIBLIOTECA {biblioteca_central.nombre.upper()} ===\n")

    # 4. Operar los préstamos (Simulación de transacciones reales)
    print("--- Intentando transacciones de prueba ---")
    biblioteca_central.emitir_prestamo(usuario, l1, 7)  # Préstamo 1 (Libro)
    biblioteca_central.emitir_prestamo(usuario, r1, 5)  # Préstamo 2 (Revista - Polimorfismo)
    biblioteca_central.emitir_prestamo(usuario, l2, 14) # Préstamo 3 (Libro)

    print("\n--- Intentando violar la Regla de Negocio (4to préstamo) ---")
    biblioteca_central.emitir_prestamo(usuario, l3, 7)  # Debería ser RECHAZADO por límite de 3

    print("\n--- Imprimiendo Tickets del Historial de Auditoría ---")
    for ticket in biblioteca_central.history_prestamos if hasattr(biblioteca_central, 'history_prestamos') else biblioteca_central.historial_prestamos:
        print("-" * 60)
        print(ticket)