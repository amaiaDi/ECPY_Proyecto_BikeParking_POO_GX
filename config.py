"""
config.py - Configuración centralizada de la aplicación.

Lee la configuración desde:
1. config.yml - Configuración general.
2. .env - Variables de entorno (sobrescribe config.yml).

Uso:
    from config import config
    
    print(config.APP_NAME)
    print(config.DATA_FOLDER)
"""

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv


# =============================================================================
# RUTA BASE DEL PROYECTO
# =============================================================================
# Al estar config.py en la raíz, BASE_DIR es simplemente su directorio padre.
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent

# Cargamos .env desde la raíz del proyecto
load_dotenv(BASE_DIR / ".env")


def cargar_yaml():
    """
    Carga la configuración desde config.yml.
    
    Returns:
        Diccionario con la configuración.
    """
    config_path = BASE_DIR / "config.yml"
    
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {}


def cargar_env():
    """Carga las variables de entorno desde .env."""
    env_path = BASE_DIR / ".env"
    load_dotenv(env_path)


class Config:
    """
    Clase de configuración que combina config.yml y .env.
    
    Prioridad: .env > config.yml > valores por defecto
    """
    
    def __init__(self):
        """Inicializa la configuración cargando yml y env."""
        # Cargar configuración
        cargar_env()
        self._yaml_config = cargar_yaml()
        
        # === Información de la aplicación ===
        self.APP_NAME = os.getenv(
            'APP_NAME', 
            self._get_yaml('app', 'name', 'BikeParking')
        )
        self.APP_VERSION = os.getenv(
            'APP_VERSION',
            self._get_yaml('app', 'version', '1.0.0')
        )
        
        # === Entorno ===
        self.ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
        self.DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
        
        # === Rutas del proyecto ===
        self.SOURCE_FOLDER = os.getenv(
            'SOURCE_FOLDER',
            self._get_yaml('paths', 'source', 'src')
        )
        self.TESTS_FOLDER = self._get_yaml('paths', 'tests', 'tests')
        self.DOCS_FOLDER = self._get_yaml('paths', 'docs', 'docs')
        
        # === Configuración de datos ===
        self.DATA_FOLDER = os.getenv(
            'DATA_FOLDER',
            self._get_yaml('data', 'folder', 'data')
        )
        self.USUARIOS_FILE = self._get_yaml('data', 'usuarios_file', 'usuarios.csv')
        self.BICIS_FILE = self._get_yaml('data', 'bicis_file', 'bicis.csv')
        self.REGISTROS_FILE = self._get_yaml('data', 'registros_file', 'registros.csv')
        
        # === Configuración CSV ===
        self.CSV_DELIMITER = os.getenv(
            'CSV_DELIMITER',
            self._get_yaml('csv', 'delimiter', ';')
        )
        self.CSV_ENCODING = os.getenv(
            'CSV_ENCODING',
            self._get_yaml('csv', 'encoding', 'utf-8')
        )
        
        # === Cabeceras CSV ===
        self.HEADERS_USUARIOS = self._get_yaml(
            'csv_headers', 'usuarios',
            ['dni', 'nombre', 'apellidos', 'email', 'movil', 'password']
        )
        self.HEADERS_BICIS = self._get_yaml(
            'csv_headers', 'bicis',
            ['id', 'marca', 'modelo', 'dni_propietario']
        )
        self.HEADERS_REGISTROS = self._get_yaml(
            'csv_headers', 'registros',
            ['id', 'id_bici', 'tipo', 'fecha_hora']
        )
        
        # === Validaciones ===
        self.DNI_LENGTH = self._get_yaml('validations', 'dni_length', default=9)
        self.MIN_PASSWORD_LENGTH = self._get_yaml('validations', 'min_password_length', default=4)
        self.MOVIL_LENGTH = self._get_yaml('validations', 'movil_length', default=9)
    
    def _get_yaml(self, section, key, default=None):
        """
        Obtiene un valor del YAML.
        
        Args:
            section: Sección del YAML (ej: 'app').
            key: Clave dentro de la sección (ej: 'name').
            default: Valor por defecto si no existe.
            
        Returns:
            El valor encontrado o el default.
        """
        if section in self._yaml_config:
            section_data = self._yaml_config[section]
            if isinstance(section_data, dict) and key in section_data:
                return section_data[key]
        return default
    
    def __str__(self):
        """Representación de la configuración."""
        return f"Config(app={self.APP_NAME}, env={self.ENVIRONMENT}, data={self.DATA_FOLDER})"


# Instancia global de configuración
config = Config()


# Para acceso directo a las constantes más usadas
APP_NAME = config.APP_NAME
SOURCE_FOLDER = config.SOURCE_FOLDER
DATA_FOLDER = config.DATA_FOLDER
CSV_DELIMITER = config.CSV_DELIMITER
CSV_ENCODING = config.CSV_ENCODING
