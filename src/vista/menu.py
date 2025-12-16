"""
menu.py - Interfaz de usuario por consola.

Funciones para mostrar menús, pedir datos y mostrar resultados.
"""


def mostrar_menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n" + "=" * 50)
    print("       SISTEMA DE PARKING DE BICICLETAS")
    print("=" * 50)
    print("1. Registrar usuario")
    print("2. Registrar bicicleta")
    print("3. Registrar entrada")
    print("4. Registrar salida")
    print("5. Ver usuarios")
    print("6. Ver bicicletas")
    print("7. Ver registros")
    print("8. Ver bicis en el parking")
    print("0. Salir")
    print("-" * 50)
    
    opcion = input("Seleccione una opción: ").strip()
    return opcion


def pedir_datos_usuario():
    """Pide al usuario los datos para registrar un nuevo usuario."""
    print("\n--- REGISTRO DE USUARIO ---")
    dni = input("DNI: ").strip().upper()
    nombre = input("Nombre completo: ").strip().title()
    email = input("Email: ").strip().lower()
    
    return dni, nombre, email


def pedir_datos_bici():
    """Pide al usuario los datos para registrar una bicicleta."""
    print("\n--- REGISTRO DE BICICLETA ---")
    serie_cuadro = input("Número de serie del cuadro: ").strip().upper()
    dni_usuario = input("DNI del propietario: ").strip().upper()
    marca = input("Marca: ").strip().title()
    modelo = input("Modelo: ").strip()
    
    return serie_cuadro, dni_usuario, marca, modelo


def pedir_serie_bici(accion):
    """
    Pide el número de serie de una bicicleta.
    
    Args:
        accion: Texto descriptivo ('entrada' o 'salida').
    """
    print(f"\n--- REGISTRAR {accion.upper()} ---")
    serie_cuadro = input("Número de serie del cuadro: ").strip().upper()
    return serie_cuadro


def mostrar_mensaje(mensaje):
    """Muestra un mensaje al usuario."""
    print(f"\n>>> {mensaje}")


def mostrar_error(mensaje):
    """Muestra un mensaje de error al usuario."""
    print(f"\n[ERROR] {mensaje}")


def mostrar_errores(errores):
    """
    Muestra una lista de errores al usuario.
    
    Args:
        errores: Lista de mensajes de error.
    """
    print("\n[ERRORES]")
    for error in errores:
        print(f"  - {error}")


def mostrar_lista_usuarios(usuarios):
    """
    Muestra una lista de usuarios.
    
    Args:
        usuarios: Lista de objetos Usuario.
    """
    print("\n--- LISTA DE USUARIOS ---")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    print(f"{'DNI':<12} {'Nombre':<20} {'Email':<25}")
    print("-" * 60)
    for u in usuarios:
        print(f"{u.dni:<12} {u.nombre_completo():<20} {u.email:<25}")
    print(f"\nTotal: {len(usuarios)} usuario(s)")


def mostrar_lista_bicis(bicis):
    """
    Muestra una lista de bicicletas.
    
    Args:
        bicis: Lista de objetos Bici.
    """
    print("\n--- LISTA DE BICICLETAS ---")
    if not bicis:
        print("No hay bicicletas registradas.")
        return
    
    print(f"{'Serie':<15} {'Propietario':<12} {'Marca':<15} {'Modelo':<15}")
    print("-" * 60)
    for b in bicis:
        print(f"{b.serie_cuadro:<15} {b.dni_usuario:<12} {b.marca:<15} {b.modelo:<15}")
    print(f"\nTotal: {len(bicis)} bicicleta(s)")


def mostrar_lista_registros(registros):
    """
    Muestra una lista de registros de movimiento.
    
    Args:
        registros: Lista de objetos Registro.
    """
    print("\n--- HISTORIAL DE MOVIMIENTOS ---")
    if not registros:
        print("No hay registros de movimientos.")
        return
    
    print(f"{'Fecha/Hora':<22} {'Acción':<8} {'Serie':<15} {'Usuario':<12}")
    print("-" * 60)
    for r in registros:
        print(f"{r.timestamp:<22} {r.accion:<8} {r.serie_cuadro:<15} {r.dni_usuario:<12}")
    print(f"\nTotal: {len(registros)} registro(s)")


def mostrar_bicis_parking(bicis):
    """
    Muestra las bicicletas actualmente en el parking.
    
    Args:
        bicis: Lista de objetos Bici en el parking.
    """
    print("\n--- BICICLETAS EN EL PARKING ---")
    if not bicis:
        print("No hay bicicletas en el parking.")
        return
    
    for b in bicis:
        print(f"  - {b}")
    print(f"\nTotal: {len(bicis)} bicicleta(s) en el parking")
