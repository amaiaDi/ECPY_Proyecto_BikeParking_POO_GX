"""
registro.py - Clase Registro.

Representa un movimiento de entrada o salida del parking.
"""


class Registro:
    """
    Representa un registro de movimiento (entrada/salida) del parking.
    
    Atributos:
        id: Identificador único del registro.
        id_bici: ID de la bicicleta.
        tipo: Tipo de movimiento ('entrada' o 'salida').
        fecha_hora: Fecha y hora del movimiento.
    """
    
    def __init__(self, id, id_bici, tipo, fecha_hora):
        """
        Crea un nuevo registro de movimiento.
        
        Args:
            id: Identificador único del registro.
            id_bici: ID de la bicicleta.
            tipo: 'entrada' o 'salida'.
            fecha_hora: Fecha y hora del movimiento.
        """
        self.id = id
        self.id_bici = id_bici
        self.tipo = tipo
        self.fecha_hora = fecha_hora
    
    def __str__(self):
        """Devuelve una representación legible del registro."""
        return f"{self.tipo.upper()} - Bici {self.id_bici} ({self.fecha_hora})"
    
    def es_entrada(self):
        """Devuelve True si es un registro de entrada."""
        return self.tipo.lower() == 'entrada'
    
    def es_salida(self):
        """Devuelve True si es un registro de salida."""
        return self.tipo.lower() == 'salida'
