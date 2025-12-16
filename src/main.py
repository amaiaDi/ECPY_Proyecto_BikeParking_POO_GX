"""
main.py - Punto de entrada de la aplicación BikeParking.

Ejecuta la aplicación de gestión de parking de bicicletas.

Uso:
    python -m src.main
"""

from src.controlador import ParkingController
from src.vista import (
    mostrar_menu_principal,
    pedir_datos_usuario,
    pedir_datos_bici,
    pedir_serie_bici,
    mostrar_mensaje,
    mostrar_lista_usuarios,
    mostrar_lista_bicis,
    mostrar_lista_registros,
    mostrar_bicis_parking,
)


def ejecutar_menu(controlador):
    """
    Bucle principal del menú.
    
    Args:
        controlador: Instancia del controlador del parking.
    """
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            datos = pedir_datos_usuario()
            resultado = controlador.registrar_usuario(*datos)
            mostrar_mensaje(resultado)
            
        elif opcion == "2":
            datos = pedir_datos_bici()
            resultado = controlador.registrar_bici(*datos)
            mostrar_mensaje(resultado)
            
        elif opcion == "3":
            serie_cuadro = pedir_serie_bici("entrada")
            resultado = controlador.registrar_entrada(serie_cuadro)
            mostrar_mensaje(resultado)
            
        elif opcion == "4":
            serie_cuadro = pedir_serie_bici("salida")
            resultado = controlador.registrar_salida(serie_cuadro)
            mostrar_mensaje(resultado)
            
        elif opcion == "5":
            usuarios = controlador.obtener_usuarios()
            mostrar_lista_usuarios(usuarios)
            
        elif opcion == "6":
            bicis = controlador.obtener_bicis()
            mostrar_lista_bicis(bicis)
            
        elif opcion == "7":
            registros = controlador.obtener_registros()
            mostrar_lista_registros(registros)
            
        elif opcion == "8":
            bicis = controlador.obtener_bicis_en_parking()
            mostrar_bicis_parking(bicis)
            
        elif opcion == "0":
            print("\n¡Hasta pronto!")
            break
            
        else:
            mostrar_mensaje("Opción no válida. Intente de nuevo.")


def main():
    """Función principal que inicia la aplicación."""
    print("Iniciando sistema de parking de bicicletas...")
    
    # Crear el controlador (contiene la lógica de negocio)
    controlador = ParkingController()
    
    # Ejecutar el bucle principal del menú
    ejecutar_menu(controlador)


if __name__ == "__main__":
    main()
