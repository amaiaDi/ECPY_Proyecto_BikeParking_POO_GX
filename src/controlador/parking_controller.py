"""
parking_controller.py - Controlador principal del sistema.

Contiene la lógica de negocio que conecta el modelo con la vista.
"""

import re
from datetime import datetime

from src.modelo import Usuario, Bici, Registro
from src.datos.csv_manager import CsvManager


class ParkingController:
    """
    Controlador principal del sistema de parking de bicicletas.
    
    Gestiona la lógica de negocio:
    - Validación de datos.
    - Operaciones CRUD sobre usuarios, bicis y registros.
    - Reglas de negocio (puede entrar/salir, unicidad, etc.).
    """
    
    # Letras para validar DNI español
    LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    def __init__(self):
        """Inicializa el controlador con los gestores de datos."""
        self.csv_manager = CsvManager()
    
    # =========================================================================
    # VALIDACIONES
    # =========================================================================
    
    def validar_dni(self, dni):
        """
        Valida el formato y letra del DNI.
        
        Args:
            dni: DNI a validar.
            
        Returns:
            True si el DNI es válido, False en caso contrario.
        """
        if not dni or len(dni) != 9:
            return False
        
        numeros = dni[:-1]
        letra = dni[-1].upper()
        
        if not numeros.isdigit():
            return False
        
        letra_correcta = self.LETRAS_DNI[int(numeros) % 23]
        return letra == letra_correcta
    
    def validar_email(self, email):
        """
        Valida el formato del email.
        
        Args:
            email: Email a validar.
            
        Returns:
            True si el formato es válido, False en caso contrario.
        """
        if not email:
            return False
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))
    
    # =========================================================================
    # GESTIÓN DE USUARIOS
    # =========================================================================
    
    def registrar_usuario(self, dni, nombre, email):
        """
        Registra un nuevo usuario en el sistema.
        
        Args:
            dni: DNI del usuario.
            nombre: Nombre completo del usuario.
            email: Correo electrónico.
            
        Returns:
            Mensaje indicando el resultado de la operación.
        """
        # Validar campos obligatorios
        if not dni or not nombre:
            return "ERROR: DNI y nombre son obligatorios."
        
        # Validar formato DNI
        if not self.validar_dni(dni):
            return "ERROR: El DNI no es válido."
        
        # Validar que el DNI no esté registrado
        usuarios = self.csv_manager.leer_usuarios()
        for u in usuarios:
            if u.dni == dni:
                return "ERROR: Ya existe un usuario con ese DNI."
        
        # Validar formato email
        if email and not self.validar_email(email):
            return "ERROR: El formato del email no es válido."
        
        # Validar que el email no esté registrado
        if email:
            for u in usuarios:
                if u.email == email:
                    return "ERROR: Ya existe un usuario con ese email."
        
        # Crear y guardar usuario
        usuario = Usuario(dni, nombre, email)
        self.csv_manager.guardar_usuario(usuario)
        
        return f"OK: Usuario {nombre} registrado correctamente."
    
    def obtener_usuarios(self):
        """
        Obtiene la lista de todos los usuarios.
        
        Returns:
            Lista de objetos Usuario.
        """
        return self.csv_manager.leer_usuarios()
    
    # =========================================================================
    # GESTIÓN DE BICICLETAS
    # =========================================================================
    
    def registrar_bici(self, serie_cuadro, dni_usuario, marca, modelo):
        """
        Registra una nueva bicicleta en el sistema.
        
        Args:
            serie_cuadro: Número de serie del cuadro.
            dni_usuario: DNI del propietario.
            marca: Marca de la bicicleta.
            modelo: Modelo de la bicicleta.
            
        Returns:
            Mensaje indicando el resultado de la operación.
        """
        # Validar campos obligatorios
        if not serie_cuadro or not marca or not dni_usuario:
            return "ERROR: Serie, marca y DNI del propietario son obligatorios."
        
        # Validar que el propietario exista
        usuarios = self.csv_manager.leer_usuarios()
        propietario_existe = False
        for u in usuarios:
            if u.dni == dni_usuario:
                propietario_existe = True
                break
        
        if not propietario_existe:
            return "ERROR: El propietario no está registrado."
        
        # Validar que el ID de bici no esté registrado
        bicis = self.csv_manager.leer_bicis()
        for b in bicis:
            if b.serie_cuadro == serie_cuadro:
                return "ERROR: Ya existe una bicicleta con ese número de serie."
        
        # Crear y guardar bici
        bici = Bici(serie_cuadro, dni_usuario, marca, modelo)
        self.csv_manager.guardar_bici(bici)
        
        return f"OK: Bicicleta {marca} {modelo} registrada correctamente."
    
    def obtener_bicis(self):
        """
        Obtiene la lista de todas las bicicletas.
        
        Returns:
            Lista de objetos Bici.
        """
        return self.csv_manager.leer_bicis()
    
    # =========================================================================
    # GESTIÓN DE MOVIMIENTOS (ENTRADAS/SALIDAS)
    # =========================================================================
    
    def registrar_entrada(self, serie_cuadro):
        """
        Registra la entrada de una bicicleta al parking.
        
        Args:
            serie_cuadro: Número de serie del cuadro de la bicicleta.
            
        Returns:
            Mensaje indicando el resultado de la operación.
        """
        if not serie_cuadro:
            return "ERROR: El número de serie de la bicicleta es obligatorio."
        
        # Verificar que la bici existe y obtener dni_usuario
        bicis = self.csv_manager.leer_bicis()
        bici_encontrada = None
        for b in bicis:
            if b.serie_cuadro == serie_cuadro:
                bici_encontrada = b
                break
        
        if not bici_encontrada:
            return "ERROR: La bicicleta no está registrada."
        
        # Verificar que la bici no está ya en el parking
        if self._bici_en_parking(serie_cuadro):
            return "ERROR: La bicicleta ya está en el parking."
        
        # Crear y guardar registro de entrada
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = Registro(timestamp, "IN", serie_cuadro, bici_encontrada.dni_usuario)
        self.csv_manager.guardar_registro(registro)
        
        return f"OK: Entrada registrada para bici {serie_cuadro}."
    
    def registrar_salida(self, serie_cuadro):
        """
        Registra la salida de una bicicleta del parking.
        
        Args:
            serie_cuadro: Número de serie del cuadro de la bicicleta.
            
        Returns:
            Mensaje indicando el resultado de la operación.
        """
        if not serie_cuadro:
            return "ERROR: El número de serie de la bicicleta es obligatorio."
        
        # Verificar que la bici existe y obtener dni_usuario
        bicis = self.csv_manager.leer_bicis()
        bici_encontrada = None
        for b in bicis:
            if b.serie_cuadro == serie_cuadro:
                bici_encontrada = b
                break
        
        if not bici_encontrada:
            return "ERROR: La bicicleta no está registrada."
        
        # Verificar que la bici está en el parking
        if not self._bici_en_parking(serie_cuadro):
            return "ERROR: La bicicleta no está en el parking."
        
        # Crear y guardar registro de salida
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = Registro(timestamp, "OUT", serie_cuadro, bici_encontrada.dni_usuario)
        self.csv_manager.guardar_registro(registro)
        
        return f"OK: Salida registrada para bici {serie_cuadro}."
    
    def obtener_registros(self):
        """
        Obtiene la lista de todos los registros.
        
        Returns:
            Lista de objetos Registro.
        """
        return self.csv_manager.leer_registros()
    
    def obtener_bicis_en_parking(self):
        """
        Obtiene las bicicletas que actualmente están en el parking.
        
        Returns:
            Lista de objetos Bici que están en el parking.
        """
        bicis = self.csv_manager.leer_bicis()
        bicis_en_parking = []
        
        for bici in bicis:
            if self._bici_en_parking(bici.serie_cuadro):
                bicis_en_parking.append(bici)
        
        return bicis_en_parking
    
    def _bici_en_parking(self, serie_cuadro):
        """
        Verifica si una bicicleta está actualmente en el parking.
        
        Una bici está en el parking si su último movimiento fue una entrada.
        
        Args:
            serie_cuadro: Número de serie del cuadro de la bicicleta.
            
        Returns:
            True si la bici está en el parking, False en caso contrario.
        """
        registros = self.csv_manager.leer_registros()
        
        # Buscar el último registro de esta bici
        ultimo_registro = None
        for r in registros:
            if r.serie_cuadro == serie_cuadro:
                ultimo_registro = r
        
        # Si no hay registros, no está en el parking
        if ultimo_registro is None:
            return False
        
        # Está en el parking si el último movimiento fue entrada
        return ultimo_registro.es_entrada()
