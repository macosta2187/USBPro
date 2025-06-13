import Mensajes  # Mensajes estáticos para mostrar al usuario
import time      # Para manejar pausas y temporizadores
import os        # Para ejecutar comandos del sistema y manipular archivos
import Sistema   # Funciones con compponentes de SO
import Usb       # Función USB
import Errores   # Mensajes de error específicos para manejo de excepciones


TIEMPO_POLEO = 2  # Tiempo en segundos entre cada chequeo de dispositivos USB 



def iniciar_tarea():
    # Bucle principal que realiza el monitoreo periódico de dispositivos USB conectados.
    try:
        while True:
            time.sleep(Sistema.TIEMPO_POLEO)
            Usb.detector_discos()            
    except KeyboardInterrupt:
        print(Mensajes.MSG_INT_USUARIO)  # Captura CTRL+C para terminar el programa
    except Exception as e:
        print(f"{Errores.MSG_ERROR}{e}") 
        
        
def desbloqueo():
    # Habilita el uso de dispositivos USB modificando el registro de Windows
    os.system('powershell -Command "Set-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR -Name Start -Value 3"')   
    print(Mensajes.MSG_DESBLOQUEO)


def bloqueo():
    # Bloquea el acceso a dispositivos USB y toma medidas de seguridad, incluyendo reiniciar el PC
    os.system('powershell -Command "Set-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR -Name Start -Value 4"')   
    print(Mensajes.MSG_BLOQUEO)
    time.sleep(5)
    
    for _ in range(1, 10):
          print("############################")    
          os.system('msg * "¡Violación a la política de seguridad de la empresa!"')  
          os.system('msg * "Debe comunicarse de inmediato con su SUPERVISOR."')  
          os.system('msg * "Este tipo de comportamiento será reportado al Departamento de Seguridad Informática."')
          os.system('msg * "Acceso restringido: se han aplicado medidas de contención."')  
          print("############################")
    
   
    time.sleep(5)
    os.system("shutdown /r /f /t 0")  # Reinicio forzado del sistema