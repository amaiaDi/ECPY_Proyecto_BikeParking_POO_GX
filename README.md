# BikeParking 🚲

Sistema de gestión de parking de bicicletas desarrollado con arquitectura MVC (Modelo-Vista-Controlador) en Python.

## 📁 Estructura del Proyecto

```
ECPY_Proyecto_BikeParking_OO_GX/
├── pyproject.toml          # Configuración del proyecto Python
├── config.yml              # Configuración de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno (no versionado)
├── data/                   # Archivos de datos CSV
│   ├── usuarios.csv
│   ├── bicis.csv
│   └── registros.csv
├── src/                    # Código fuente
│   ├── config.py           # Carga centralizada de configuración
│   ├── main.py             # Punto de entrada
│   ├── modelo/             # Clases de dominio (Usuario, Bici, Registro)
│   ├── vista/              # Interfaz de usuario (menús)
│   ├── controlador/        # Lógica de negocio
│   └── datos/              # Gestión de persistencia CSV
├── tests/                  # Tests unitarios
└── docs/                   # Documentación
```

## ⚙️ Archivos de Configuración

Este proyecto utiliza varios archivos de configuración con propósitos diferentes:

| Archivo            | Propósito                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------|
| **pyproject.toml** | Configuración del **proyecto Python** (metadatos, dependencias, herramientas de desarrollo) |
| **config.yml**     | Configuración de la **aplicación en ejecución** (rutas, formato CSV, validaciones)          |
| **config.py**      | Módulo Python que **carga y unifica** la configuración de yml y .env                        |
| **.env**           | Variables de entorno sensibles o específicas del entorno (no se versiona)                   |

### ¿Por qué tener pyproject.toml Y config.yml?

Ambos archivos cumplen **roles diferentes y complementarios**:

| Aspecto              | pyproject.toml | config.yml |
|----------------------|----------------------------------------------------------|--------------------------------------------|
| **Propósito**        | Cómo **construir/desarrollar** el proyecto               | Cómo **se comporta** la aplicación         |
| **Audiencia**        | Desarrolladores y herramientas (pip, pytest, black)      | La aplicación en ejecución                 |
| **Estándar**         | PEP 518/621 (estándar Python) | Específico del proyecto  |
| **Contenido típico** | Dependencias, metadatos, configuración de linters        | Rutas de datos, formato CSV, validaciones |
| **Cuándo se usa**    | Al instalar, testear o construir el proyecto             | Al ejecutar la aplicación |

**En resumen:** `pyproject.toml` define el "cómo" del desarrollo, mientras que `config.yml` define el "qué" de la ejecución.

### pyproject.toml

Estándar de Python (PEP 518/621) para definir:
- Metadatos del proyecto (nombre, versión, autores)
- Dependencias de producción y desarrollo
- Configuración de herramientas (pytest, black, flake8)
- Scripts de entrada (`bikeparking`)

```toml
[project]
name = "bikeparking"
version = "1.0.0"

[tool.pytest]
testpaths = ["tests"]
```

### config.yml

Configuración específica de la aplicación:
- Rutas de carpetas de datos
- Nombres de archivos CSV
- Formato CSV (delimitador, encoding)
- Cabeceras de los archivos
- Parámetros de validación

```yaml
data:
  folder: "data"
  usuarios_file: "usuarios.csv"

csv:
  delimiter: ";"
  encoding: "utf-8"
```

### config.py

Módulo Python que:
1. Detecta automáticamente la raíz del proyecto buscando `pyproject.toml`
2. Carga `config.yml` y `.env`
3. Permite sobrescribir valores de yml con variables de entorno
4. Expone una instancia global `config` para usar en toda la aplicación

```python
from src.config import config

print(config.APP_NAME)      # "BikeParking"
print(config.DATA_FOLDER)   # "data"
print(config.CSV_DELIMITER) # ";"
```

**Prioridad de configuración:** `.env` > `config.yml` > valores por defecto

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/amaiaDi/ECPY_Proyecto_BikeParking_POO_GX.git
cd ECPY_Proyecto_BikeParking_OO_GX
```

### 2. Crear entorno virtual

```bash
python -m venv bikeParkingPooVenv
```

### 3. Activar entorno virtual

**Windows (PowerShell):**
```powershell
.\bikeParkingPooVenv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
bikeParkingPooVenv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source bikeParkingPooVenv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

O para desarrollo:
```bash
pip install -e ".[dev]"
```

## 🎮 Uso

```bash
python -m src.main
```

O si instalaste el proyecto:
```bash
bikeparking
```

## 🧪 Tests

```bash
pytest
```

Con cobertura:
```bash
pytest --cov=src
```

## 📝 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.
