"""
validators.py - Funciones de validación de entrada de usuario.

Contiene funciones para validar los datos introducidos por el usuario
antes de pasarlos al controlador.
"""

import re
from config import config


def validar_dni(dni):
    """
    Valida el formato de un DNI español.
    
    El DNI debe tener 8 dígitos seguidos de una letra.
    
    Args:
        dni: DNI a validar.
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not dni:
        return False, "El DNI no puede estar vacío"
    
    dni = dni.upper().strip()
    
    if len(dni) != config.DNI_LENGTH:
        return False, f"El DNI debe tener {config.DNI_LENGTH} caracteres"
    
    # Patrón: 8 dígitos + 1 letra
    patron = r'^[0-9]{8}[A-Z]$'
    if not re.match(patron, dni):
        return False, "El DNI debe tener 8 dígitos seguidos de una letra"
    
    # Validar letra del DNI
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(dni[:-1])
    letra_correcta = letras_dni[numero % 23]
    
    if dni[-1] != letra_correcta:
        return False, f"La letra del DNI no es correcta (debería ser {letra_correcta})"
    
    return True, ""


def validar_email(email):
    """
    Valida el formato de un email.
    
    Args:
        email: Email a validar.
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not email:
        return False, "El email no puede estar vacío"
    
    email = email.strip().lower()
    
    # Patrón básico de email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        return False, "El formato del email no es válido"
    
    return True, ""


def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío y tenga formato correcto.
    
    Args:
        nombre: Nombre a validar.
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not nombre:
        return False, "El nombre no puede estar vacío"
    
    nombre = nombre.strip()
    
    if len(nombre) < 2:
        return False, "El nombre debe tener al menos 2 caracteres"
    
    # Solo letras y espacios
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', nombre):
        return False, "El nombre solo puede contener letras"
    
    return True, ""


def validar_serie_cuadro(serie_cuadro):
    """
    Valida el número de serie del cuadro de una bicicleta.
    
    Args:
        serie_cuadro: Número de serie del cuadro a validar.
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not serie_cuadro:
        return False, "El número de serie no puede estar vacío"
    
    serie_cuadro = serie_cuadro.strip()
    
    if len(serie_cuadro) < 1:
        return False, "El número de serie debe tener al menos 1 carácter"
    
    return True, ""


def validar_datos_usuario(dni, nombre, email):
    """
    Valida todos los datos de un usuario.
    
    Args:
        dni: DNI del usuario.
        nombre: Nombre completo del usuario.
        email: Email del usuario.
        
    Returns:
        tuple: (es_valido, lista_errores)
    """
    errores = []
    
    valido, error = validar_dni(dni)
    if not valido:
        errores.append(f"DNI: {error}")
    
    valido, error = validar_nombre(nombre)
    if not valido:
        errores.append(f"Nombre: {error}")
    
    if email:  # Email es opcional
        valido, error = validar_email(email)
        if not valido:
            errores.append(f"Email: {error}")
    
    return len(errores) == 0, errores


def validar_datos_bici(serie_cuadro, dni_usuario, marca, modelo):
    """
    Valida todos los datos de una bicicleta.
    
    Args:
        serie_cuadro: Número de serie del cuadro.
        dni_usuario: DNI del propietario.
        marca: Marca de la bicicleta.
        modelo: Modelo de la bicicleta.
        
    Returns:
        tuple: (es_valido, lista_errores)
    """
    errores = []
    
    valido, error = validar_serie_cuadro(serie_cuadro)
    if not valido:
        errores.append(f"Serie: {error}")
    
    valido, error = validar_dni(dni_usuario)
    if not valido:
        errores.append(f"DNI propietario: {error}")
    
    if not marca or len(marca.strip()) < 1:
        errores.append("Marca: La marca no puede estar vacía")
    
    if not modelo or len(modelo.strip()) < 1:
        errores.append("Modelo: El modelo no puede estar vacío")
    
    return len(errores) == 0, errores
