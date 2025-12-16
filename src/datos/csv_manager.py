"""
csv_manager.py - Gestor de archivos CSV.

Clase simple para leer y escribir datos en archivos CSV.
Usa la configuración centralizada de config.py.
"""

import csv
import os

from src.modelo import Usuario, Bici, Registro
from config import config


class CsvManager:
    """
    Gestiona la lectura y escritura de datos en archivos CSV.
    
    Atributos:
        ruta_usuarios: Ruta al archivo de usuarios.
        ruta_bicis: Ruta al archivo de bicicletas.
        ruta_registros: Ruta al archivo de registros.
    """
    
    def __init__(self, carpeta_datos=None):
        """
        Inicializa el gestor de CSV.
        
        Args:
            carpeta_datos: Carpeta donde se guardan los archivos CSV.
                          Si es None, usa la configuración.
        """
        self.carpeta_datos = carpeta_datos or config.DATA_FOLDER
        self.delimiter = config.CSV_DELIMITER
        self.encoding = config.CSV_ENCODING
        
        self.ruta_usuarios = os.path.join(self.carpeta_datos, config.USUARIOS_FILE)
        self.ruta_bicis = os.path.join(self.carpeta_datos, config.BICIS_FILE)
        self.ruta_registros = os.path.join(self.carpeta_datos, config.REGISTROS_FILE)
        
        # Crear carpeta y archivos si no existen
        self._inicializar_archivos()
    
    def _inicializar_archivos(self):
        """Crea la carpeta y archivos CSV si no existen."""
        # Crear carpeta si no existe
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)
        
        # Crear archivo de usuarios si no existe
        if not os.path.exists(self.ruta_usuarios):
            self._crear_csv(self.ruta_usuarios, config.HEADERS_USUARIOS)
        
        # Crear archivo de bicis si no existe
        if not os.path.exists(self.ruta_bicis):
            self._crear_csv(self.ruta_bicis, config.HEADERS_BICIS)
        
        # Crear archivo de registros si no existe
        if not os.path.exists(self.ruta_registros):
            self._crear_csv(self.ruta_registros, config.HEADERS_REGISTROS)
    
    def _crear_csv(self, ruta, cabeceras):
        """
        Crea un archivo CSV vacío con las cabeceras especificadas.
        
        Args:
            ruta: Ruta del archivo a crear.
            cabeceras: Lista de nombres de columnas.
        """
        with open(ruta, mode='w', encoding=self.encoding, newline='') as archivo:
            writer = csv.writer(archivo, delimiter=self.delimiter)
            writer.writerow(cabeceras)
    
    # =========================================================================
    # USUARIOS
    # =========================================================================
    
    def leer_usuarios(self):
        """
        Lee todos los usuarios del archivo CSV.
        
        Returns:
            Lista de objetos Usuario.
        """
        usuarios = []
        
        with open(self.ruta_usuarios, mode='r', encoding=self.encoding, newline='') as archivo:
            reader = csv.DictReader(archivo, delimiter=self.delimiter)
            for fila in reader:
                usuario = Usuario(
                    dni=fila['dni'],
                    nombre=fila['nombre'],
                    email=fila['email']
                )
                usuarios.append(usuario)
        
        return usuarios
    
    def guardar_usuario(self, usuario):
        """
        Añade un usuario al archivo CSV.
        
        Args:
            usuario: Objeto Usuario a guardar.
        """
        with open(self.ruta_usuarios, mode='a', encoding=self.encoding, newline='') as archivo:
            writer = csv.writer(archivo, delimiter=self.delimiter)
            writer.writerow([
                usuario.dni,
                usuario.nombre,
                usuario.email
            ])
    
    # =========================================================================
    # BICICLETAS
    # =========================================================================
    
    def leer_bicis(self):
        """
        Lee todas las bicicletas del archivo CSV.
        
        Returns:
            Lista de objetos Bici.
        """
        bicis = []
        
        with open(self.ruta_bicis, mode='r', encoding=self.encoding, newline='') as archivo:
            reader = csv.DictReader(archivo, delimiter=self.delimiter)
            for fila in reader:
                bici = Bici(
                    serie_cuadro=fila['serie_cuadro'],
                    dni_usuario=fila['dni_usuario'],
                    marca=fila['marca'],
                    modelo=fila['modelo']
                )
                bicis.append(bici)
        
        return bicis
    
    def guardar_bici(self, bici):
        """
        Añade una bicicleta al archivo CSV.
        
        Args:
            bici: Objeto Bici a guardar.
        """
        with open(self.ruta_bicis, mode='a', encoding=self.encoding, newline='') as archivo:
            writer = csv.writer(archivo, delimiter=self.delimiter)
            writer.writerow([
                bici.serie_cuadro,
                bici.dni_usuario,
                bici.marca,
                bici.modelo
            ])
    
    # =========================================================================
    # REGISTROS DE MOVIMIENTO
    # =========================================================================
    
    def leer_registros(self):
        """
        Lee todos los registros del archivo CSV.
        
        Returns:
            Lista de objetos Registro.
        """
        registros = []
        
        with open(self.ruta_registros, mode='r', encoding=self.encoding, newline='') as archivo:
            reader = csv.DictReader(archivo, delimiter=self.delimiter)
            for fila in reader:
                registro = Registro(
                    timestamp=fila['timestamp'],
                    accion=fila['accion'],
                    serie_cuadro=fila['serie_cuadro'],
                    dni_usuario=fila['dni_usuario']
                )
                registros.append(registro)
        
        return registros
    
    def guardar_registro(self, registro):
        """
        Añade un registro al archivo CSV.
        
        Args:
            registro: Objeto Registro a guardar.
        """
        with open(self.ruta_registros, mode='a', encoding=self.encoding, newline='') as archivo:
            writer = csv.writer(archivo, delimiter=self.delimiter)
            writer.writerow([
                registro.timestamp,
                registro.accion,
                registro.serie_cuadro,
                registro.dni_usuario
            ])
