"""
bicis_controller.py - Gestión de bicicletas.

Funciones para registrar y consultar bicicletas.
"""

from src.modelo import Bici
from src.datos import csv_manager


def registrar_bici(serie_cuadro, dni_usuario, marca, modelo):
    """
    Registra una nueva bicicleta en el sistema.
    
    Args:
        serie_cuadro: Número de serie del cuadro.
        dni_usuario: DNI del propietario.
        marca: Marca de la bicicleta.
        modelo: Modelo de la bicicleta.
        
    Returns:
        Mensaje indicando el resultado de la operación.
    """
    # Validar campos obligatorios
    if not serie_cuadro or not marca or not dni_usuario:
        return "ERROR: Serie, marca y DNI del propietario son obligatorios."
    
    # Validar que el propietario exista
    usuarios = csv_manager.leer_usuarios()
    propietario_existe = False
    for u in usuarios:
        if u.dni == dni_usuario:
            propietario_existe = True
            break
    
    if not propietario_existe:
        return "ERROR: El propietario no está registrado."
    
    # Validar que el número de serie no esté registrado
    bicis = csv_manager.leer_bicis()
    for b in bicis:
        if b.serie_cuadro == serie_cuadro:
            return "ERROR: Ya existe una bicicleta con ese número de serie."
    
    # Crear y guardar bici
    bici = Bici(serie_cuadro, dni_usuario, marca, modelo)
    csv_manager.guardar_bici(bici)
    
    return f"OK: Bicicleta {marca} {modelo} registrada correctamente."


def obtener_bicis():
    """
    Obtiene la lista de todas las bicicletas.
    
    Returns:
        Lista de objetos Bici.
    """
    return csv_manager.leer_bicis()


def buscar_bici(serie_cuadro):
    """
    Busca una bicicleta por su número de serie.
    
    Args:
        serie_cuadro: Número de serie del cuadro.
        
    Returns:
        Objeto Bici si existe, None en caso contrario.
    """
    bicis = csv_manager.leer_bicis()
    for bici in bicis:
        if bici.serie_cuadro == serie_cuadro:
            return bici
    return None
