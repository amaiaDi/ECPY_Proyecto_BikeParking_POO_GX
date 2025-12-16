"""
main.py - Punto de entrada de la aplicación BikeParking.

Ejecuta la aplicación de gestión de parking de bicicletas.

Uso:
    python -m src.main
"""

from src.controlador import ParkingController
from src.vista import Menu


def main():
    """Función principal que inicia la aplicación."""
    print("Iniciando sistema de parking de bicicletas...")
    
    # Crear el controlador (contiene la lógica de negocio)
    controlador = ParkingController()
    
    # Crear la vista (interfaz de usuario) conectada al controlador
    menu = Menu(controlador)
    
    # Ejecutar el bucle principal del menú
    menu.ejecutar()


if __name__ == "__main__":
    main()
