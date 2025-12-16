"""
Repositorio de bicicletas: acceso a datos (CSV ahora, BD en el futuro)
"""
from src.datos import csv_manager
from src.modelo.bici import Bici


def obtener_bici_por_serie(serie_cuadro):
    """Devuelve una Bici por número de serie o None si no existe."""
    bicis = csv_manager.leer_bicis()
    for b in bicis:
        if b['serie_cuadro'] == serie_cuadro:
            return Bici(**b)
    return None


def guardar_bici(bici):
    """Guarda una bici (objeto Bici) en el CSV."""
    csv_manager.guardar_bici(bici)


def listar_bicis():
    """Devuelve una lista de objetos Bici."""
    bicis = csv_manager.leer_bicis()
    return [Bici(**b) for b in bicis]
