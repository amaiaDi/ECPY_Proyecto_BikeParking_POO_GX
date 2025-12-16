"""
Validaciones de formato: solo comprueban sintaxis, no acceden a datos.
"""
import re


def validar_dni(dni):
    """Valida el formato y la letra de control del DNI español (8 dígitos + letra)."""
    dni = str(dni).upper()
    if not re.match(r'^[0-9]{8}[A-Z]$', dni):
        return False
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(dni[:8])
    letra_correcta = letras[numero % 23]
    return dni[-1] == letra_correcta


def validar_email(email):
    """Valida el formato básico de un email."""
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', str(email)))


def campo_no_vacio(valor):
    """Comprueba que un campo no está vacío."""
    return bool(valor and str(valor).strip())
