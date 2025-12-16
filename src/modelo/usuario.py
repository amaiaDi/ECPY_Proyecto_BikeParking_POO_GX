"""
usuario.py - Clase Usuario.

Representa a un usuario registrado en el sistema de parking.
"""


class Usuario:
    """
    Representa un usuario del sistema de parking de bicicletas.
    
    Atributos:
        dni: DNI del usuario (identificador único).
        nombre: Nombre completo del usuario.
        email: Correo electrónico.
    """
    
    def __init__(self, dni, nombre, email):
        """
        Crea un nuevo usuario.
        
        Args:
            dni: DNI del usuario.
            nombre: Nombre completo del usuario.
            email: Correo electrónico.
        """
        self.dni = dni
        self.nombre = nombre
        self.email = email
    
    def __str__(self):
        """Devuelve una representación legible del usuario."""
        return f"{self.nombre} (DNI: {self.dni})"
    
    def nombre_completo(self):
        """Devuelve el nombre completo del usuario."""
        return self.nombre
