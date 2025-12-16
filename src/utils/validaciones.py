"""
validaciones.py - Funciones de validación de datos.

Contiene las validaciones de DNI, email y otros campos.
"""

import re


# Letras para validar DNI español
LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"


def validar_dni(dni):
    """
    Valida el formato y letra del DNI español.
    
    Args:
        dni: DNI a validar.
        
    Returns:
        True si el DNI es válido, False en caso contrario.
    """
    if not dni or len(dni) != 9:
        return False
    
    numeros = dni[:-1]
    letra = dni[-1].upper()
    
    if not numeros.isdigit():
        return False
    
    letra_correcta = LETRAS_DNI[int(numeros) % 23]
    return letra == letra_correcta


def validar_email(email):
    """
    Valida el formato del email.
    
    Args:
        email: Email a validar.
        
    Returns:
        True si el formato es válido, False en caso contrario.
    """
    if not email:
        return False
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))
