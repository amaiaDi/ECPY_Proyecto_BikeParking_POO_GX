"""
Servicio principal de BikeParking: lógica de negocio y validaciones de alto nivel.
Agrupa los casos de uso principales (usuarios, bicis, movimientos).
"""
from src.repositories.usuarios_repository import obtener_usuario_por_dni, guardar_usuario, listar_usuarios
from src.repositories.bicis_repository import obtener_bici_por_serie, guardar_bici, listar_bicis
from src.repositories.registros_repository import guardar_registro, listar_registros
from src.validators.formato import validar_dni, validar_email
from src.validators.negocio import dni_unico, bici_unica
from src.modelo.usuario import Usuario
from src.modelo.bici import Bici
from src.modelo.registro import Registro


def registrar_usuario(dni, nombre, email):
    """Registra un usuario si pasa validaciones de formato y negocio."""
    if not validar_dni(dni):
        return "ERROR: DNI no válido"
    if not validar_email(email):
        return "ERROR: Email no válido"
    if not dni_unico(dni):
        return "ERROR: El DNI ya existe"
    usuario = Usuario(dni, nombre, email)
    guardar_usuario(usuario)
    return "OK: Usuario registrado"


def obtener_usuarios():
    """Devuelve la lista de usuarios."""
    return listar_usuarios()

# Aquí se pueden añadir funciones para bicis y movimientos siguiendo el mismo patrón.
