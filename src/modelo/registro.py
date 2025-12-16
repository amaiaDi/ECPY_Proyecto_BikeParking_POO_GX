"""
registro.py - Clase Registro.

Representa un movimiento de entrada o salida del parking.
"""


class Registro:
    """
    Representa un registro de movimiento (entrada/salida) del parking.
    
    Atributos:
        timestamp: Fecha y hora del movimiento.
        accion: Tipo de movimiento ('IN' o 'OUT').
        serie_cuadro: Serie del cuadro de la bicicleta.
        dni_usuario: DNI del usuario.
    """
    
    def __init__(self, timestamp, accion, serie_cuadro, dni_usuario):
        """
        Crea un nuevo registro de movimiento.
        
        Args:
            timestamp: Fecha y hora del movimiento.
            accion: 'IN' (entrada) o 'OUT' (salida).
            serie_cuadro: Serie del cuadro de la bicicleta.
            dni_usuario: DNI del usuario.
        """
        self.timestamp = timestamp
        self.accion = accion
        self.serie_cuadro = serie_cuadro
        self.dni_usuario = dni_usuario
    
    def __str__(self):
        """Devuelve una representación legible del registro."""
        return f"{self.accion} - Bici {self.serie_cuadro} ({self.timestamp})"
    
    def es_entrada(self):
        """Devuelve True si es un registro de entrada."""
        return self.accion.upper() == 'IN'
    
    def es_salida(self):
        """Devuelve True si es un registro de salida."""
        return self.accion.upper() == 'OUT'
