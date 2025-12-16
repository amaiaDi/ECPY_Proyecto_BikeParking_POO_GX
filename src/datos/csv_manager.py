"""
csv_manager.py - Gestor de archivos CSV.

Funciones simples para leer y escribir datos en archivos CSV.
"""

import csv
import os

import config
from src.modelo import Usuario, Bici, Registro


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def _asegurar_carpeta_existe():
    """Crea la carpeta de datos si no existe."""
    if not os.path.exists(config.DATA_FOLDER):
        os.makedirs(config.DATA_FOLDER)


def _ruta_archivo(nombre_archivo):
    """Devuelve la ruta completa a un archivo de datos."""
    return os.path.join(config.DATA_FOLDER, nombre_archivo)


def _leer_csv(nombre_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.
    
    Args:
        nombre_archivo: Nombre del archivo CSV.
        
    Returns:
        Lista de diccionarios con los datos.
    """
    ruta = _ruta_archivo(nombre_archivo)
    
    if not os.path.exists(ruta):
        return []
    
    with open(ruta, mode='r', encoding=config.CSV_ENCODING, newline='') as archivo:
        reader = csv.DictReader(archivo, delimiter=config.CSV_DELIMITER)
        return list(reader)


def _escribir_csv(nombre_archivo, cabeceras, fila):
    """
    Añade una fila a un archivo CSV. Crea el archivo si no existe.
    
    Args:
        nombre_archivo: Nombre del archivo CSV.
        cabeceras: Lista con los nombres de columnas.
        fila: Lista con los valores a escribir.
    """
    _asegurar_carpeta_existe()
    ruta = _ruta_archivo(nombre_archivo)
    
    # Si el archivo no existe, crear con cabeceras
    archivo_nuevo = not os.path.exists(ruta)
    
    with open(ruta, mode='a', encoding=config.CSV_ENCODING, newline='') as archivo:
        writer = csv.writer(archivo, delimiter=config.CSV_DELIMITER)
        if archivo_nuevo:
            writer.writerow(cabeceras)
        writer.writerow(fila)


# =============================================================================
# USUARIOS
# =============================================================================

def leer_usuarios():
    """
    Lee todos los usuarios del archivo CSV.
    
    Returns:
        Lista de objetos Usuario.
    """
    filas = _leer_csv(config.USUARIOS_FILE)
    usuarios = []
    
    for fila in filas:
        usuario = Usuario(
            dni=fila['dni'],
            nombre=fila['nombre'],
            email=fila['email']
        )
        usuarios.append(usuario)
    
    return usuarios


def guardar_usuario(usuario):
    """
    Añade un usuario al archivo CSV.
    
    Args:
        usuario: Objeto Usuario a guardar.
    """
    _escribir_csv(
        config.USUARIOS_FILE,
        config.HEADERS_USUARIOS,
        [usuario.dni, usuario.nombre, usuario.email]
    )


# =============================================================================
# BICICLETAS
# =============================================================================

def leer_bicis():
    """
    Lee todas las bicicletas del archivo CSV.
    
    Returns:
        Lista de objetos Bici.
    """
    filas = _leer_csv(config.BICIS_FILE)
    bicis = []
    
    for fila in filas:
        bici = Bici(
            serie_cuadro=fila['serie_cuadro'],
            dni_usuario=fila['dni_usuario'],
            marca=fila['marca'],
            modelo=fila['modelo']
        )
        bicis.append(bici)
    
    return bicis


def guardar_bici(bici):
    """
    Añade una bicicleta al archivo CSV.
    
    Args:
        bici: Objeto Bici a guardar.
    """
    _escribir_csv(
        config.BICIS_FILE,
        config.HEADERS_BICIS,
        [bici.serie_cuadro, bici.dni_usuario, bici.marca, bici.modelo]
    )


# =============================================================================
# REGISTROS
# =============================================================================

def leer_registros():
    """
    Lee todos los registros del archivo CSV.
    
    Returns:
        Lista de objetos Registro.
    """
    filas = _leer_csv(config.REGISTROS_FILE)
    registros = []
    
    for fila in filas:
        registro = Registro(
            timestamp=fila['timestamp'],
            accion=fila['accion'],
            serie_cuadro=fila['serie_cuadro'],
            dni_usuario=fila['dni_usuario']
        )
        registros.append(registro)
    
    return registros


def guardar_registro(registro):
    """
    Añade un registro al archivo CSV.
    
    Args:
        registro: Objeto Registro a guardar.
    """
    _escribir_csv(
        config.REGISTROS_FILE,
        config.HEADERS_REGISTROS,
        [registro.timestamp, registro.accion, registro.serie_cuadro, registro.dni_usuario]
    )
