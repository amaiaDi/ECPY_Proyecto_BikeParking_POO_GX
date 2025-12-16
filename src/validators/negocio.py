"""
Validaciones de negocio: dependen de los datos existentes (unicidad, existencia, coherencia).
"""
from src.repositories.usuarios_repository import obtener_usuario_por_dni
from src.repositories.bicis_repository import obtener_bici_por_serie


def dni_unico(dni):
    """Devuelve True si el DNI no existe ya en el sistema."""
    return obtener_usuario_por_dni(dni) is None


def bici_unica(serie_cuadro):
    """Devuelve True si la bici no existe ya en el sistema."""
    return obtener_bici_por_serie(serie_cuadro) is None
