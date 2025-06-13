import Mensajes  # Mensajes estáticos para mostrar al usuario
import Errores   # Mensajes de error específicos para manejo de excepciones
import time      # Para manejar pausas y temporizadores
import datetime  # Para manejar fechas y horas
import getpass   # Para obtener el usuario actual del sistema
import socket    # Para obtener el nombre y la IP del equipo
import os        # Para ejecutar comandos del sistema y manipular archivos
import uuid      # Sirven para obtener la MAC address del equipo



SEPARADOR = "===================================================================" # Separador visual en consola

def display_limpiador(temporizador):
    # Cuenta regresiva que limpia la pantalla y muestra mensajes de búsqueda
    if temporizador == 0:
        os.system('cls')  # Limpia pantalla en Windows
        return
    print(f"{Mensajes.MSG_BUSQUEDA} {temporizador}")
    time.sleep(1)
    display_limpiador(temporizador - 1)


def display_alerta():
    # Muestra un mensaje de alerta visual y luego limpia la pantalla
    print(SEPARADOR)   
    print(Mensajes.MSG_ALERTA)
    print(SEPARADOR)
    display_limpiador(1)      


def display_monitoreo():
    # Mensaje que indica que no hay dispositivos USB conectados
    print(SEPARADOR)
    print(Mensajes.MSG_SIN_DISPOSITIVO)
    print(SEPARADOR)


def display_info_pc():
    # Obtiene y retorna información básica del PC: fecha, usuario, nombre y IP, MAC
    try:
        mac = ':'.join(f'{(uuid.getnode() >> i) & 0xff:02x}' for i in range(40, -1, -8))
        info = {
            "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Usuario": getpass.getuser(),
            "Nombre_PC": socket.gethostname(),
            "ip": socket.gethostbyname(socket.gethostname()),
            "MAC": mac
            
        }
        return info
    except Exception as e:
        print(f"{Errores.MSG_ERROR_INFO_SISTEMA}{e}")
        return Mensajes.MSG_SIN_DATOS
    

def display_info_disco(nombre_disco, interfaz, modelo, serial):
    # Imprime en pantalla la información del dispositivo USB detectado
    print(SEPARADOR)
    print(f"Dispositivo: {nombre_disco}")
    print(f"Tipo de interfaz: {interfaz}")
    print(f"Modelo: {modelo}")
    print(f"Serial: {serial}")
    print(SEPARADOR)