# BikeParking 🚲

Sistema de gestión de parking de bicicletas desarrollado con arquitectura MVC (Modelo-Vista-Controlador) en Python.

## 📁 Estructura del Proyecto

```
ECPY_Proyecto_BikeParking_OO_GX/
├── config.py               # Configuración (constantes simples)
├── pyproject.toml          # Configuración del proyecto Python
├── requirements.txt        # Dependencias (solo pytest)
├── data/                   # Archivos de datos CSV
│   ├── usuarios.csv
│   ├── bicis.csv
│   └── registros.csv
├── src/                    # Código fuente
│   ├── main.py             # Punto de entrada
│   ├── modelo/             # Clases de dominio
│   │   ├── usuario.py      # Clase Usuario
│   │   ├── bici.py         # Clase Bici
│   │   └── registro.py     # Clase Registro
│   ├── vista/              # Interfaz de usuario
│   │   └── menu.py         # Funciones de menú por consola
│   ├── controlador/        # Lógica de negocio
│   │   ├── parking_controller.py    # Clase fachada (opcional)
│   │   ├── usuarios_controller.py   # Gestión de usuarios
│   │   ├── bicis_controller.py      # Gestión de bicicletas
│   │   └── movimientos_controller.py # Entradas/salidas
│   ├── datos/              # Persistencia
│   │   └── csv_manager.py  # Funciones de lectura/escritura CSV
│   └── utils/              # Utilidades
│       └── validaciones.py # Validación de DNI, email, etc.
├── tests/                  # Tests unitarios
└── docs/                   # Documentación
```

## 🏗️ Arquitectura

El proyecto sigue el patrón **MVC** (Modelo-Vista-Controlador):

| Capa            | Carpeta            | Responsabilidad                                |
|-----------------|--------------------|------------------------------------------------|
| **Modelo**      | `src/modelo/`      | Clases de datos: `Usuario`, `Bici`, `Registro` |
| **Vista**       | `src/vista/`       | Interacción con el usuario por consola         |
| **Controlador** | `src/controlador/` | Lógica de negocio y reglas                     |
| **Datos**       | `src/datos/`       | Persistencia en archivos CSV                   |
| **Utils**       | `src/utils/`       | Funciones auxiliares (validaciones)            |

### Estructura de datos CSV

```
usuarios.csv:   dni, nombre, email
bicis.csv:      serie_cuadro, dni_usuario, marca, modelo
registros.csv:  timestamp, accion (IN/OUT), serie_cuadro, dni_usuario
```

## ⚙️ Configuración

### config.py

Contiene las constantes de configuración. Es un archivo Python simple:

```python
import config

# Constantes disponibles:
config.APP_NAME          # "BikeParking"
config.DATA_FOLDER       # "data"
config.CSV_DELIMITER     # ","
config.HEADERS_USUARIOS  # ["dni", "nombre", "email"]
```

### pyproject.toml

Estándar de Python (PEP 518/621) para definir:
- Metadatos del proyecto (nombre, versión, autores)
- Dependencias de producción y desarrollo
- Configuración de herramientas (pytest)

## 📚 Archivos de Configuración en Python

En proyectos Python es común encontrar varios archivos de configuración. Aquí explicamos cada uno:

| Archivo            | ¿Qué es?                         | ¿Cuándo usarlo?                               |
|--------------------|----------------------------------|-----------------------------------------------|
| **pyproject.toml** | Estándar del proyecto Python     | Metadatos, dependencias, herramientas (pytest)|
| **config.py**      | Constantes de la aplicación      | Rutas, valores por defecto, cabeceras CSV     |
| **config.yml**     | Configuración en formato YAML    | Valores que el usuario puede modificar        |
| **.env**           | Variables de entorno             | Secretos, contraseñas, configuración local    |

### ¿Por qué existen tantos archivos?

Cada archivo tiene un **propósito diferente**:

```
┌─────────────────────────────────────────────────────────────────┐
│                        DESARROLLO                               │
│  ┌─────────────────┐                                            │
│  │ pyproject.toml  │ → pip, pytest, versión, dependencias       │
│  └─────────────────┘                                            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                        EJECUCIÓN                                │
│  ┌──────────┐    ┌─────────────┐    ┌───────────┐               │
│  │   .env   │ →  │  config.py  │ ←  │config.yml │               │
│  │(secretos)│    │  (cargador) │    │ (valores) │               │
│  └──────────┘    └─────────────┘    └───────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

### Detalle de cada archivo

#### pyproject.toml
- **Audiencia**: Desarrolladores y herramientas (pip, pytest)
- **Estándar**: PEP 518/621 (oficial de Python)
- **Contenido**: Dependencias, versión, configuración de linters
- **Cuándo se lee**: Al instalar (`pip install`) o testear (`pytest`)

```toml
[project]
name = "bikeparking"
version = "1.0.0"
dependencies = ["pytest>=7.0"]
```

#### config.py
- **Audiencia**: La aplicación en ejecución
- **Formato**: Código Python (constantes simples)
- **Contenido**: Rutas, delimitadores CSV, cabeceras
- **Cuándo se lee**: Al ejecutar la aplicación

```python
DATA_FOLDER = "data"
CSV_DELIMITER = ","
HEADERS_USUARIOS = ["dni", "nombre", "email"]
```

#### config.yml (no usado en este proyecto)
- **Audiencia**: Usuarios/administradores
- **Formato**: YAML (legible por humanos)
- **Contenido**: Valores configurables sin tocar código
- **Requiere**: Librería `pyyaml`

```yaml
data:
  folder: "data"
csv:
  delimiter: ","
```

#### .env (no usado en este proyecto)
- **Audiencia**: Configuración local/secretos
- **Formato**: Clave=valor
- **Contenido**: Contraseñas, API keys, variables por entorno
- **Requiere**: Librería `python-dotenv`
- **⚠️ No se versiona** (añadir a .gitignore)

```env
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=sk-1234567890
DEBUG=true
```

### ¿Por qué este proyecto solo usa config.py?

Para **simplicidad pedagógica**:

| Enfoque | Archivos | Librerías extra |
|---------|----------|-----------------|
| **Complejo** | pyproject.toml + config.yml + .env + config.py | pyyaml, python-dotenv |
| **Simple** (este proyecto) | pyproject.toml + config.py | ninguna |

En proyectos profesionales es común usar los 4 archivos, pero para aprender POO es mejor empezar simple.

### 📂 Archivos de ejemplo incluidos

Para aprender cómo funcionan estos archivos, el proyecto incluye **ejemplos educativos**:

| Archivo | Descripción |
|---------|-------------|
| `config.yml.example` | Ejemplo de configuración YAML con comentarios explicativos |
| `.env.example` | Ejemplo de variables de entorno con explicación de uso |

Estos archivos **no se usan** en la aplicación, pero puedes estudiarlos para entender cómo funcionan en proyectos profesionales.

## 📖 Documentación automática de la API

La documentación técnica de las clases y funciones principales se genera automáticamente con **pydoc** y está disponible en:

- `docs/api/` — Archivos HTML navegables para cada módulo y clase principal.

Para consultarla:
1. Abre cualquier archivo `.html` de esa carpeta con tu navegador web.
2. Consulta el índice en `docs/api/README.md` para ver los módulos disponibles.

> Si modificas el código fuente, puedes regenerar la documentación ejecutando:
> 
> ```bash
> python -m pydoc -w src.modelo.bici src.modelo.usuario src.modelo.registro src.datos.csv_manager src.controlador.parking_controller src.controlador.usuarios_controller src.controlador.bicis_controller src.controlador.movimientos_controller src.utils.validaciones src.vista.menu
> ```

---

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

## 🎮 Uso

```bash
python -m src.main
```

### Ejemplo de uso directo (sin clase)

```python
# Usar las funciones directamente
from src.controlador import usuarios_controller
from src.controlador import bicis_controller
from src.utils import validar_dni

# Validar un DNI
if validar_dni("12345678Z"):
    usuarios_controller.registrar_usuario("12345678Z", "Juan", "juan@email.com")
```

### Ejemplo con clase fachada

```python
# Usar la clase ParkingController
from src.controlador import ParkingController

parking = ParkingController()
parking.registrar_usuario("12345678Z", "Juan", "juan@email.com")
parking.registrar_bici("BK001", "12345678Z", "Giant", "Escape")
parking.registrar_entrada("BK001")
```

## 🧪 Tests

```bash
pytest
```

Con detalle:
```bash
pytest -v
```

## 📝 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.
