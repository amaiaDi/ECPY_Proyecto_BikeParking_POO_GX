"""
Repositorio de registros de movimientos: acceso a datos (CSV ahora, BD en el futuro)
"""
from src.datos import csv_manager
from src.modelo.registro import Registro


def guardar_registro(registro):
    """Guarda un registro (objeto Registro) en el CSV."""
    csv_manager.guardar_registro(registro)


def listar_registros():
    """Devuelve una lista de objetos Registro."""
    registros = csv_manager.leer_registros()
    return [Registro(**r) for r in registros]
