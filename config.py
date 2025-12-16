"""
config.py - Configuración del proyecto.

Contiene las constantes de configuración de la aplicación.
Modifica estos valores según las necesidades del proyecto.

Uso:
    from config import DATA_FOLDER, CSV_DELIMITER
"""

# =============================================================================
# INFORMACIÓN DE LA APLICACIÓN
# =============================================================================

APP_NAME = "BikeParking"
APP_VERSION = "1.0.0"

# =============================================================================
# CARPETAS DEL PROYECTO
# =============================================================================

DATA_FOLDER = "data"
SOURCE_FOLDER = "src"
TESTS_FOLDER = "tests"
DOCS_FOLDER = "docs"

# =============================================================================
# ARCHIVOS CSV
# =============================================================================

USUARIOS_FILE = "usuarios.csv"
BICIS_FILE = "bicis.csv"
REGISTROS_FILE = "registros.csv"

# =============================================================================
# CONFIGURACIÓN CSV
# =============================================================================

CSV_DELIMITER = ","
CSV_ENCODING = "utf-8"

# =============================================================================
# CABECERAS DE LOS ARCHIVOS CSV
# =============================================================================

HEADERS_USUARIOS = ["dni", "nombre", "email"]
HEADERS_BICIS = ["serie_cuadro", "dni_usuario", "marca", "modelo"]
HEADERS_REGISTROS = ["timestamp", "accion", "serie_cuadro", "dni_usuario"]

# =============================================================================
# VALIDACIONES
# =============================================================================

DNI_LENGTH = 9
