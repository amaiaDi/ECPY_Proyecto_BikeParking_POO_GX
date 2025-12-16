"""
movimientos_controller.py - Gestión de entradas y salidas.

Funciones para registrar movimientos de bicicletas en el parking.
"""

from datetime import datetime

from src.modelo import Registro
from src.datos import csv_manager
from src.controlador.bicis_controller import buscar_bici


def bici_en_parking(serie_cuadro):
    """
    Verifica si una bicicleta está actualmente en el parking.
    
    Una bici está en el parking si su último movimiento fue una entrada.
    
    Args:
        serie_cuadro: Número de serie del cuadro de la bicicleta.
        
    Returns:
        True si la bici está en el parking, False en caso contrario.
    """
    registros = csv_manager.leer_registros()
    
    # Buscar el último registro de esta bici
    ultimo_registro = None
    for r in registros:
        if r.serie_cuadro == serie_cuadro:
            ultimo_registro = r
    
    # Si no hay registros, no está en el parking
    if ultimo_registro is None:
        return False
    
    # Está en el parking si el último movimiento fue entrada
    return ultimo_registro.es_entrada()


def registrar_entrada(serie_cuadro):
    """
    Registra la entrada de una bicicleta al parking.
    
    Args:
        serie_cuadro: Número de serie del cuadro de la bicicleta.
        
    Returns:
        Mensaje indicando el resultado de la operación.
    """
    if not serie_cuadro:
        return "ERROR: El número de serie de la bicicleta es obligatorio."
    
    # Verificar que la bici existe
    bici = buscar_bici(serie_cuadro)
    if not bici:
        return "ERROR: La bicicleta no está registrada."
    
    # Verificar que la bici no está ya en el parking
    if bici_en_parking(serie_cuadro):
        return "ERROR: La bicicleta ya está en el parking."
    
    # Crear y guardar registro de entrada
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = Registro(timestamp, "IN", serie_cuadro, bici.dni_usuario)
    csv_manager.guardar_registro(registro)
    
    return f"OK: Entrada registrada para bici {serie_cuadro}."


def registrar_salida(serie_cuadro):
    """
    Registra la salida de una bicicleta del parking.
    
    Args:
        serie_cuadro: Número de serie del cuadro de la bicicleta.
        
    Returns:
        Mensaje indicando el resultado de la operación.
    """
    if not serie_cuadro:
        return "ERROR: El número de serie de la bicicleta es obligatorio."
    
    # Verificar que la bici existe
    bici = buscar_bici(serie_cuadro)
    if not bici:
        return "ERROR: La bicicleta no está registrada."
    
    # Verificar que la bici está en el parking
    if not bici_en_parking(serie_cuadro):
        return "ERROR: La bicicleta no está en el parking."
    
    # Crear y guardar registro de salida
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = Registro(timestamp, "OUT", serie_cuadro, bici.dni_usuario)
    csv_manager.guardar_registro(registro)
    
    return f"OK: Salida registrada para bici {serie_cuadro}."


def obtener_registros():
    """
    Obtiene la lista de todos los registros.
    
    Returns:
        Lista de objetos Registro.
    """
    return csv_manager.leer_registros()


def obtener_bicis_en_parking():
    """
    Obtiene las bicicletas que actualmente están en el parking.
    
    Returns:
        Lista de objetos Bici que están en el parking.
    """
    bicis = csv_manager.leer_bicis()
    bicis_en_parking = []
    
    for bici in bicis:
        if bici_en_parking(bici.serie_cuadro):
            bicis_en_parking.append(bici)
    
    return bicis_en_parking
