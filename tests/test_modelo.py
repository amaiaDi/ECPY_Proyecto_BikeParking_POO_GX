"""
test_modelo.py - Tests para las clases del modelo.

Ejecutar con: pytest tests/test_modelo.py -v

Estructura de datos simplificada:
- Usuario: dni, nombre, email
- Bici: serie_cuadro, dni_usuario, marca, modelo
- Registro: timestamp, accion (IN/OUT), serie_cuadro, dni_usuario
"""

from src.modelo import Usuario, Bici, Registro


class TestUsuario:
    """Tests para la clase Usuario."""
    
    def test_crear_usuario(self):
        """Se puede crear un usuario con todos los atributos."""
        usuario = Usuario("12345678Z", "Juan García", "juan@email.com")
        
        assert usuario.dni == "12345678Z"
        assert usuario.nombre == "Juan García"
        assert usuario.email == "juan@email.com"
    
    def test_str_usuario(self):
        """__str__ devuelve representación legible."""
        usuario = Usuario("12345678Z", "Juan García", "juan@email.com")
        
        resultado = str(usuario)
        assert "Juan García" in resultado
        assert "12345678Z" in resultado


class TestBici:
    """Tests para la clase Bici."""
    
    def test_crear_bici(self):
        """Se puede crear una bici con todos los atributos."""
        bici = Bici("BICI001", "12345678Z", "Giant", "Escape 3")
        
        assert bici.serie_cuadro == "BICI001"
        assert bici.dni_usuario == "12345678Z"
        assert bici.marca == "Giant"
        assert bici.modelo == "Escape 3"
    
    def test_str_bici(self):
        """__str__ devuelve representación legible."""
        bici = Bici("BICI001", "12345678Z", "Giant", "Escape 3")
        
        resultado = str(bici)
        assert "Giant" in resultado
        assert "Escape 3" in resultado
        assert "BICI001" in resultado


class TestRegistro:
    """Tests para la clase Registro."""
    
    def test_crear_registro(self):
        """Se puede crear un registro con todos los atributos."""
        registro = Registro("2024-01-15 10:30:00", "IN", "BICI001", "12345678Z")
        
        assert registro.timestamp == "2024-01-15 10:30:00"
        assert registro.accion == "IN"
        assert registro.serie_cuadro == "BICI001"
        assert registro.dni_usuario == "12345678Z"
    
    def test_es_entrada(self):
        """es_entrada() devuelve True para entradas (IN)."""
        registro = Registro("2024-01-15 10:30:00", "IN", "BICI001", "12345678Z")
        
        assert registro.es_entrada() is True
        assert registro.es_salida() is False
    
    def test_es_salida(self):
        """es_salida() devuelve True para salidas (OUT)."""
        registro = Registro("2024-01-15 10:30:00", "OUT", "BICI001", "12345678Z")
        
        assert registro.es_entrada() is False
        assert registro.es_salida() is True
