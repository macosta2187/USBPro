import Display   # Funciones de MSG
import Sistema   # Funciones con compponentes de SO




def menu():
    # Función principal que muestra el menú y gestiona las opciones del usuario
    while True:
        print("--- Menú principal ---")
        print(Display.SEPARADOR)
        print("1. Monitorear y bloqueo USB")
        print("2. Desbloquear USB")
        print("3. Salir")
        print(Display.SEPARADOR)  
        opcion = input("Seleccioná una opción: ")

        # Estructura de control para decidir qué función ejecutar según la opción
        match opcion:
            case '1':
                Sistema.iniciar_tarea()  # Comienza la tarea de monitoreo
            case '2':
                Sistema.desbloqueo()     # Desbloquea el acceso USB
            case '3':
                print("Gracias por utilizar el programa ")
                break
            case _:
                print("Opción no válida")    