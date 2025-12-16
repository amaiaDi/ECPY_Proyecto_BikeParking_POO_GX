"""
Repositorio de usuarios: acceso a datos (CSV ahora, BD en el futuro)
"""
from src.datos import csv_manager
from src.modelo.usuario import Usuario


def obtener_usuario_por_dni(dni):
    """Devuelve un Usuario por DNI o None si no existe."""
    usuarios = csv_manager.leer_usuarios()
    for u in usuarios:
        if u['dni'] == dni:
            return Usuario(**u)
    return None


def guardar_usuario(usuario):
    """Guarda un usuario (objeto Usuario) en el CSV."""
    csv_manager.guardar_usuario(usuario)


def listar_usuarios():
    """Devuelve una lista de objetos Usuario."""
    usuarios = csv_manager.leer_usuarios()
    return [Usuario(**u) for u in usuarios]
