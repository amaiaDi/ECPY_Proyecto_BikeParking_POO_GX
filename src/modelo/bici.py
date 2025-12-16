"""
bici.py - Clase Bici.

Representa una bicicleta registrada en el sistema de parking.
"""


class Bici:
    """
    Representa una bicicleta registrada en el sistema.
    
    Atributos:
        serie_cuadro: Número de serie del cuadro (identificador único).
        dni_usuario: DNI del usuario propietario.
        marca: Marca de la bicicleta.
        modelo: Modelo de la bicicleta.
    """
    
    def __init__(self, serie_cuadro, dni_usuario, marca, modelo):
        """
        Crea una nueva bicicleta.
        
        Args:
            serie_cuadro: Número de serie del cuadro (identificador único).
            dni_usuario: DNI del propietario.
            marca: Marca de la bicicleta.
            modelo: Modelo de la bicicleta.
        """
        self.serie_cuadro = serie_cuadro
        self.dni_usuario = dni_usuario
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        """Devuelve una representación legible de la bici."""
        return f"{self.marca} {self.modelo} (Serie: {self.serie_cuadro})"
