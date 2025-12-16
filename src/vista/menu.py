"""
menu.py - Interfaz de usuario por consola.

Contiene la clase Menu que gestiona la interacción con el usuario.
"""


class Menu:
    """
    Gestiona la interfaz de usuario del sistema de parking.
    
    Muestra menús, recoge datos del usuario y muestra resultados.
    """
    
    def __init__(self, controlador):
        """
        Inicializa el menú con una referencia al controlador.
        
        Args:
            controlador: Instancia del controlador del parking.
        """
        self.controlador = controlador
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal y devuelve la opción elegida."""
        print("\n" + "=" * 50)
        print("       SISTEMA DE PARKING DE BICICLETAS")
        print("=" * 50)
        print("1. Registrar usuario")
        print("2. Registrar bicicleta")
        print("3. Registrar entrada")
        print("4. Registrar salida")
        print("5. Ver usuarios")
        print("6. Ver bicicletas")
        print("7. Ver registros")
        print("8. Ver bicis en el parking")
        print("0. Salir")
        print("-" * 50)
        
        opcion = input("Seleccione una opción: ").strip()
        return opcion
    
    def pedir_datos_usuario(self):
        """Pide al usuario los datos para registrar un nuevo usuario."""
        print("\n--- REGISTRO DE USUARIO ---")
        dni = input("DNI: ").strip().upper()
        nombre = input("Nombre: ").strip().title()
        apellidos = input("Apellidos: ").strip().title()
        email = input("Email: ").strip().lower()
        movil = input("Móvil: ").strip()
        password = input("Contraseña: ").strip()
        
        return dni, nombre, apellidos, email, movil, password
    
    def pedir_datos_bici(self):
        """Pide al usuario los datos para registrar una bicicleta."""
        print("\n--- REGISTRO DE BICICLETA ---")
        id_bici = input("ID/Número de serie: ").strip().upper()
        marca = input("Marca: ").strip().title()
        modelo = input("Modelo: ").strip()
        dni_propietario = input("DNI del propietario: ").strip().upper()
        
        return id_bici, marca, modelo, dni_propietario
    
    def pedir_id_bici(self, accion):
        """
        Pide el ID de una bicicleta.
        
        Args:
            accion: Texto descriptivo ('entrada' o 'salida').
        """
        print(f"\n--- REGISTRAR {accion.upper()} ---")
        id_bici = input("ID de la bicicleta: ").strip().upper()
        return id_bici
    
    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje al usuario."""
        print(f"\n>>> {mensaje}")
    
    def mostrar_lista_usuarios(self, usuarios):
        """
        Muestra una lista de usuarios.
        
        Args:
            usuarios: Lista de objetos Usuario.
        """
        print("\n--- LISTA DE USUARIOS ---")
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        
        print(f"{'DNI':<12} {'Nombre':<20} {'Email':<25}")
        print("-" * 60)
        for u in usuarios:
            print(f"{u.dni:<12} {u.nombre_completo():<20} {u.email:<25}")
        print(f"\nTotal: {len(usuarios)} usuario(s)")
    
    def mostrar_lista_bicis(self, bicis):
        """
        Muestra una lista de bicicletas.
        
        Args:
            bicis: Lista de objetos Bici.
        """
        print("\n--- LISTA DE BICICLETAS ---")
        if not bicis:
            print("No hay bicicletas registradas.")
            return
        
        print(f"{'ID':<15} {'Marca':<15} {'Modelo':<15} {'Propietario':<12}")
        print("-" * 60)
        for b in bicis:
            print(f"{b.id:<15} {b.marca:<15} {b.modelo:<15} {b.dni_propietario:<12}")
        print(f"\nTotal: {len(bicis)} bicicleta(s)")
    
    def mostrar_lista_registros(self, registros):
        """
        Muestra una lista de registros de movimiento.
        
        Args:
            registros: Lista de objetos Registro.
        """
        print("\n--- HISTORIAL DE MOVIMIENTOS ---")
        if not registros:
            print("No hay registros de movimientos.")
            return
        
        print(f"{'Tipo':<10} {'ID Bici':<15} {'Fecha/Hora':<20}")
        print("-" * 50)
        for r in registros:
            print(f"{r.tipo:<10} {r.id_bici:<15} {r.fecha_hora:<20}")
        print(f"\nTotal: {len(registros)} registro(s)")
    
    def mostrar_bicis_parking(self, bicis):
        """
        Muestra las bicicletas actualmente en el parking.
        
        Args:
            bicis: Lista de objetos Bici en el parking.
        """
        print("\n--- BICICLETAS EN EL PARKING ---")
        if not bicis:
            print("No hay bicicletas en el parking.")
            return
        
        for b in bicis:
            print(f"  - {b}")
        print(f"\nTotal: {len(bicis)} bicicleta(s) en el parking")
    
    def ejecutar(self):
        """Bucle principal del menú."""
        while True:
            opcion = self.mostrar_menu_principal()
            
            if opcion == "1":
                datos = self.pedir_datos_usuario()
                resultado = self.controlador.registrar_usuario(*datos)
                self.mostrar_mensaje(resultado)
                
            elif opcion == "2":
                datos = self.pedir_datos_bici()
                resultado = self.controlador.registrar_bici(*datos)
                self.mostrar_mensaje(resultado)
                
            elif opcion == "3":
                id_bici = self.pedir_id_bici("entrada")
                resultado = self.controlador.registrar_entrada(id_bici)
                self.mostrar_mensaje(resultado)
                
            elif opcion == "4":
                id_bici = self.pedir_id_bici("salida")
                resultado = self.controlador.registrar_salida(id_bici)
                self.mostrar_mensaje(resultado)
                
            elif opcion == "5":
                usuarios = self.controlador.obtener_usuarios()
                self.mostrar_lista_usuarios(usuarios)
                
            elif opcion == "6":
                bicis = self.controlador.obtener_bicis()
                self.mostrar_lista_bicis(bicis)
                
            elif opcion == "7":
                registros = self.controlador.obtener_registros()
                self.mostrar_lista_registros(registros)
                
            elif opcion == "8":
                bicis = self.controlador.obtener_bicis_en_parking()
                self.mostrar_bicis_parking(bicis)
                
            elif opcion == "0":
                print("\n¡Hasta pronto!")
                break
                
            else:
                self.mostrar_mensaje("Opción no válida. Intente de nuevo.")
