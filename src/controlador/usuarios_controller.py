"""
usuarios_controller.py - Gestión de usuarios.

Funciones para registrar y consultar usuarios.
"""

from src.modelo import Usuario
from src.datos import csv_manager
from src.utils.validaciones import validar_dni, validar_email


def registrar_usuario(dni, nombre, email):
    """
    Registra un nuevo usuario en el sistema.
    
    Args:
        dni: DNI del usuario.
        nombre: Nombre completo del usuario.
        email: Correo electrónico.
        
    Returns:
        Mensaje indicando el resultado de la operación.
    """
    # Validar campos obligatorios
    if not dni or not nombre:
        return "ERROR: DNI y nombre son obligatorios."
    
    # Validar formato DNI
    if not validar_dni(dni):
        return "ERROR: El DNI no es válido."
    
    # Validar que el DNI no esté registrado
    usuarios = csv_manager.leer_usuarios()
    for u in usuarios:
        if u.dni == dni:
            return "ERROR: Ya existe un usuario con ese DNI."
    
    # Validar formato email
    if email and not validar_email(email):
        return "ERROR: El formato del email no es válido."
    
    # Validar que el email no esté registrado
    if email:
        for u in usuarios:
            if u.email == email:
                return "ERROR: Ya existe un usuario con ese email."
    
    # Crear y guardar usuario
    usuario = Usuario(dni, nombre, email)
    csv_manager.guardar_usuario(usuario)
    
    return f"OK: Usuario {nombre} registrado correctamente."


def obtener_usuarios():
    """
    Obtiene la lista de todos los usuarios.
    
    Returns:
        Lista de objetos Usuario.
    """
    return csv_manager.leer_usuarios()
