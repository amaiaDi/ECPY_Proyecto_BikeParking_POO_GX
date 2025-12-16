"""
usuario.py - Clase Usuario.

Representa a un usuario registrado en el sistema de parking.
"""


class Usuario:
    """
    Representa un usuario del sistema de parking de bicicletas.
    
    Atributos:
        dni: DNI del usuario (identificador único).
        nombre: Nombre del usuario.
        apellidos: Apellidos del usuario.
        email: Correo electrónico.
        movil: Número de teléfono móvil.
        password: Contraseña del usuario.
    """
    
    def __init__(self, dni, nombre, apellidos, email, movil, password):
        """
        Crea un nuevo usuario.
        
        Args:
            dni: DNI del usuario.
            nombre: Nombre del usuario.
            apellidos: Apellidos del usuario.
            email: Correo electrónico.
            movil: Teléfono móvil.
            password: Contraseña.
        """
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.movil = movil
        self.password = password
    
    def __str__(self):
        """Devuelve una representación legible del usuario."""
        return f"{self.nombre} {self.apellidos} (DNI: {self.dni})"
    
    def nombre_completo(self):
        """Devuelve el nombre completo del usuario."""
        return f"{self.nombre} {self.apellidos}"
