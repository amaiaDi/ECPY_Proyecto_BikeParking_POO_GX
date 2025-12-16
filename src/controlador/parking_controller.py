"""
parking_controller.py - Controlador principal del sistema.

Clase que agrupa todas las operaciones del parking.
Internamente delega a los módulos especializados.
"""

from src.validators.formato import validar_dni, validar_email
from src.controlador import usuarios_controller
from src.controlador import bicis_controller
from src.controlador import movimientos_controller


class ParkingController:
    """
    Controlador principal del sistema de parking de bicicletas.
    
    Agrupa todas las operaciones en una única clase para facilitar su uso.
    Internamente delega en módulos especializados.
    """
    
    def __init__(self):
        """Inicializa el controlador."""
        pass
    
    # =========================================================================
    # VALIDACIONES
    # =========================================================================
    
    def validar_dni(self, dni):
        """Valida el formato y letra del DNI."""
        return validar_dni(dni)
    
    def validar_email(self, email):
        """Valida el formato del email."""
        return validar_email(email)
    
    # =========================================================================
    # USUARIOS
    # =========================================================================
    
    def registrar_usuario(self, dni, nombre, email):
        """Registra un nuevo usuario."""
        return usuarios_controller.registrar_usuario(dni, nombre, email)
    
    def obtener_usuarios(self):
        """Obtiene la lista de usuarios."""
        return usuarios_controller.obtener_usuarios()
    
    # =========================================================================
    # BICICLETAS
    # =========================================================================
    
    def registrar_bici(self, serie_cuadro, dni_usuario, marca, modelo):
        """Registra una nueva bicicleta."""
        return bicis_controller.registrar_bici(serie_cuadro, dni_usuario, marca, modelo)
    
    def obtener_bicis(self):
        """Obtiene la lista de bicicletas."""
        return bicis_controller.obtener_bicis()
    
    # =========================================================================
    # MOVIMIENTOS
    # =========================================================================
    
    def registrar_entrada(self, serie_cuadro):
        """Registra la entrada de una bicicleta."""
        return movimientos_controller.registrar_entrada(serie_cuadro)
    
    def registrar_salida(self, serie_cuadro):
        """Registra la salida de una bicicleta."""
        return movimientos_controller.registrar_salida(serie_cuadro)
    
    def obtener_registros(self):
        """Obtiene la lista de registros."""
        return movimientos_controller.obtener_registros()
    
    def obtener_bicis_en_parking(self):
        """Obtiene las bicis que están en el parking."""
        return movimientos_controller.obtener_bicis_en_parking()
