"""
Paquete vista - Contiene la interfaz de usuario.

Módulos:
    - menu: Funciones de menú y entrada/salida por consola.
    - validators: Funciones de validación de entrada de usuario.
"""

from src.vista.menu import (
    mostrar_menu_principal,
    pedir_datos_usuario,
    pedir_datos_bici,
    pedir_serie_bici,
    mostrar_mensaje,
    mostrar_error,
    mostrar_errores,
    mostrar_lista_usuarios,
    mostrar_lista_bicis,
    mostrar_lista_registros,
    mostrar_bicis_parking,
)
from src.vista.validators import (
    validar_dni,
    validar_email,
    validar_nombre,
    validar_serie_cuadro,
    validar_datos_usuario,
    validar_datos_bici,
)
