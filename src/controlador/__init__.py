"""
Paquete controlador - Contiene la lógica de negocio.

Módulos:
    - parking_controller: Controlador principal (clase fachada).
    - validaciones: Funciones de validación de DNI, email, etc.
    - usuarios_controller: Gestión de usuarios.
    - bicis_controller: Gestión de bicicletas.
    - movimientos_controller: Gestión de entradas y salidas.
"""

from src.controlador.parking_controller import ParkingController
from src.validators.formato import validar_dni, validar_email
