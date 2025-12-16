"""
test_controlador.py - Tests para el controlador.

Ejecutar con: pytest tests/test_controlador.py -v

Estructura de datos simplificada:
- Usuario: dni, nombre, email
- Bici: serie_cuadro, dni_usuario, marca, modelo
- Registro: timestamp, accion (IN/OUT), serie_cuadro, dni_usuario
"""

import os
import shutil
import pytest

from src.controlador import ParkingController


class TestValidaciones:
    """Tests para las funciones de validación del controlador."""
    
    def setup_method(self):
        """Prepara el controlador para cada test."""
        self.controlador = ParkingController()
    
    def test_validar_dni_correcto(self):
        """Un DNI con formato y letra correctos es válido."""
        # 12345678 % 23 = 14 -> Z
        assert self.controlador.validar_dni("12345678Z") is True
    
    def test_validar_dni_letra_incorrecta(self):
        """Un DNI con letra incorrecta no es válido."""
        assert self.controlador.validar_dni("12345678A") is False
    
    def test_validar_dni_formato_incorrecto(self):
        """Un DNI con formato incorrecto no es válido."""
        assert self.controlador.validar_dni("1234567") is False
        assert self.controlador.validar_dni("ABCDEFGHI") is False
        assert self.controlador.validar_dni("") is False
    
    def test_validar_email_correcto(self):
        """Un email con formato correcto es válido."""
        assert self.controlador.validar_email("usuario@dominio.com") is True
        assert self.controlador.validar_email("test.user@empresa.es") is True
    
    def test_validar_email_incorrecto(self):
        """Un email con formato incorrecto no es válido."""
        assert self.controlador.validar_email("sinArroba.com") is False
        assert self.controlador.validar_email("@dominio.com") is False
        assert self.controlador.validar_email("") is False


class TestRegistroUsuarios:
    """Tests para el registro de usuarios."""
    
    def setup_method(self):
        """Prepara datos temporales para cada test."""
        self.carpeta_test = "data_test"
        if os.path.exists(self.carpeta_test):
            shutil.rmtree(self.carpeta_test)
        
        # Crear controlador con carpeta de test
        from src.datos.csv_manager import CsvManager
        self.controlador = ParkingController()
        self.controlador.csv_manager = CsvManager(self.carpeta_test)
    
    def teardown_method(self):
        """Limpia datos temporales después de cada test."""
        if os.path.exists(self.carpeta_test):
            shutil.rmtree(self.carpeta_test)
    
    def test_registrar_usuario_ok(self):
        """Se puede registrar un usuario con datos válidos."""
        resultado = self.controlador.registrar_usuario(
            "12345678Z", "Juan García", "juan@email.com"
        )
        
        assert "OK" in resultado
        assert "Juan" in resultado
    
    def test_registrar_usuario_dni_duplicado(self):
        """No se puede registrar un usuario con DNI duplicado."""
        self.controlador.registrar_usuario(
            "12345678Z", "Juan García", "juan@email.com"
        )
        
        resultado = self.controlador.registrar_usuario(
            "12345678Z", "Pedro López", "pedro@email.com"
        )
        
        assert "ERROR" in resultado
        assert "DNI" in resultado
    
    def test_registrar_usuario_dni_invalido(self):
        """No se puede registrar un usuario con DNI inválido."""
        resultado = self.controlador.registrar_usuario(
            "12345678A", "Juan García", "juan@email.com"
        )
        
        assert "ERROR" in resultado


class TestRegistroBicis:
    """Tests para el registro de bicicletas."""
    
    def setup_method(self):
        """Prepara datos temporales para cada test."""
        self.carpeta_test = "data_test"
        if os.path.exists(self.carpeta_test):
            shutil.rmtree(self.carpeta_test)
        
        from src.datos.csv_manager import CsvManager
        self.controlador = ParkingController()
        self.controlador.csv_manager = CsvManager(self.carpeta_test)
        
        # Registrar un usuario para las pruebas
        self.controlador.registrar_usuario(
            "12345678Z", "Juan García", "juan@email.com"
        )
    
    def teardown_method(self):
        """Limpia datos temporales después de cada test."""
        if os.path.exists(self.carpeta_test):
            shutil.rmtree(self.carpeta_test)
    
    def test_registrar_bici_ok(self):
        """Se puede registrar una bici con propietario existente."""
        resultado = self.controlador.registrar_bici(
            "BICI001", "12345678Z", "Giant", "Escape 3"
        )
        
        assert "OK" in resultado
    
    def test_registrar_bici_propietario_no_existe(self):
        """No se puede registrar bici si el propietario no existe."""
        resultado = self.controlador.registrar_bici(
            "BICI001", "99999999R", "Giant", "Escape 3"
        )
        
        assert "ERROR" in resultado
        assert "propietario" in resultado.lower()


class TestMovimientos:
    """Tests para entrada y salida de bicis."""
    
    def setup_method(self):
        """Prepara datos temporales para cada test."""
        self.carpeta_test = "data_test"
        if os.path.exists(self.carpeta_test):
            shutil.rmtree(self.carpeta_test)
        
        from src.datos.csv_manager import CsvManager
        self.controlador = ParkingController()
        self.controlador.csv_manager = CsvManager(self.carpeta_test)
        
        # Registrar usuario y bici para las pruebas
        self.controlador.registrar_usuario(
            "12345678Z", "Juan García", "juan@email.com"
        )
        self.controlador.registrar_bici("BICI001", "12345678Z", "Giant", "Escape 3")
    
    def teardown_method(self):
        """Limpia datos temporales después de cada test."""
        if os.path.exists(self.carpeta_test):
            shutil.rmtree(self.carpeta_test)
    
    def test_registrar_entrada_ok(self):
        """Se puede registrar entrada de una bici."""
        resultado = self.controlador.registrar_entrada("BICI001")
        
        assert "OK" in resultado
    
    def test_no_entrada_si_ya_esta_dentro(self):
        """No se puede entrar si la bici ya está dentro."""
        self.controlador.registrar_entrada("BICI001")
        
        resultado = self.controlador.registrar_entrada("BICI001")
        
        assert "ERROR" in resultado
    
    def test_registrar_salida_ok(self):
        """Se puede registrar salida de una bici que está dentro."""
        self.controlador.registrar_entrada("BICI001")
        
        resultado = self.controlador.registrar_salida("BICI001")
        
        assert "OK" in resultado
    
    def test_no_salida_si_no_esta_dentro(self):
        """No se puede salir si la bici no está dentro."""
        resultado = self.controlador.registrar_salida("BICI001")
        
        assert "ERROR" in resultado
