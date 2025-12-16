"""
bici.py - Clase Bici.

Representa una bicicleta registrada en el sistema de parking.
"""


class Bici:
    """
    Representa una bicicleta registrada en el sistema.
    
    Atributos:
        id: Identificador único (número de serie).
        marca: Marca de la bicicleta.
        modelo: Modelo de la bicicleta.
        dni_propietario: DNI del usuario propietario.
    """
    
    def __init__(self, id, marca, modelo, dni_propietario):
        """
        Crea una nueva bicicleta.
        
        Args:
            id: Número de serie (identificador único).
            marca: Marca de la bicicleta.
            modelo: Modelo de la bicicleta.
            dni_propietario: DNI del propietario.
        """
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.dni_propietario = dni_propietario
    
    def __str__(self):
        """Devuelve una representación legible de la bici."""
        return f"{self.marca} {self.modelo} (ID: {self.id})"
