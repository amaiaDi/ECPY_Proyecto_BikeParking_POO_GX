"""
test_modelo.py - Tests para las clases del modelo.

Ejecutar con: pytest tests/test_modelo.py -v
"""

from src.modelo import Usuario, Bici, Registro


class TestUsuario:
    """Tests para la clase Usuario."""
    
    def test_crear_usuario(self):
        """Se puede crear un usuario con todos los atributos."""
        usuario = Usuario("12345678Z", "Juan", "García", "juan@email.com", "666111222", "1234")
        
        assert usuario.dni == "12345678Z"
        assert usuario.nombre == "Juan"
        assert usuario.apellidos == "García"
        assert usuario.email == "juan@email.com"
        assert usuario.movil == "666111222"
        assert usuario.password == "1234"
    
    def test_nombre_completo(self):
        """nombre_completo() devuelve nombre y apellidos."""
        usuario = Usuario("12345678Z", "Juan", "García", "", "", "")
        
        assert usuario.nombre_completo() == "Juan García"
    
    def test_str_usuario(self):
        """__str__ devuelve representación legible."""
        usuario = Usuario("12345678Z", "Juan", "García", "", "", "")
        
        resultado = str(usuario)
        assert "Juan" in resultado
        assert "García" in resultado
        assert "12345678Z" in resultado


class TestBici:
    """Tests para la clase Bici."""
    
    def test_crear_bici(self):
        """Se puede crear una bici con todos los atributos."""
        bici = Bici("BICI001", "Giant", "Escape 3", "12345678Z")
        
        assert bici.id == "BICI001"
        assert bici.marca == "Giant"
        assert bici.modelo == "Escape 3"
        assert bici.dni_propietario == "12345678Z"
    
    def test_str_bici(self):
        """__str__ devuelve representación legible."""
        bici = Bici("BICI001", "Giant", "Escape 3", "12345678Z")
        
        resultado = str(bici)
        assert "Giant" in resultado
        assert "Escape 3" in resultado


class TestRegistro:
    """Tests para la clase Registro."""
    
    def test_crear_registro(self):
        """Se puede crear un registro con todos los atributos."""
        registro = Registro("REG001", "BICI001", "entrada", "2024-01-15 10:30:00")
        
        assert registro.id == "REG001"
        assert registro.id_bici == "BICI001"
        assert registro.tipo == "entrada"
        assert registro.fecha_hora == "2024-01-15 10:30:00"
    
    def test_es_entrada(self):
        """es_entrada() devuelve True para entradas."""
        registro = Registro("REG001", "BICI001", "entrada", "2024-01-15 10:30:00")
        
        assert registro.es_entrada() is True
        assert registro.es_salida() is False
    
    def test_es_salida(self):
        """es_salida() devuelve True para salidas."""
        registro = Registro("REG001", "BICI001", "salida", "2024-01-15 10:30:00")
        
        assert registro.es_entrada() is False
        assert registro.es_salida() is True
