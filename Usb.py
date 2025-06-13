import Errores   # Mensajes de error específicos para manejo de excepciones
import Archivo   # Variables de archivo y carpeta para logs
import Display   # Funciones de MSG
import Sistema   # Funciones con compponentes de SO
import wmi       # Módulo para acceder a la información de hardware en Windows



def detector_discos():
    # Detecta dispositivos USB conectados y ejecuta acciones según la detección
    try:
        detector = wmi.WMI()  # Inicializa WMI para obtener info hardware
        for dispositivo in detector.Win32_DiskDrive():
            try:
                interfaz = getattr(dispositivo, 'InterfaceType', '')
                media_type = getattr(dispositivo, 'MediaType', '')

                # Solo interesan dispositivos removibles o externos (USB)
                if not any(tipo in media_type for tipo in ['Removable', 'External']):
                    Display.display_monitoreo()                    
                    continue

                nombre_disco = getattr(dispositivo, 'Caption', 'Desconocido')
                serial = getattr(dispositivo, 'SerialNumber', 'Desconocido')
                modelo = getattr(dispositivo, 'Model', 'Desconocido')              
                
                Display.display_info_disco(nombre_disco, interfaz, modelo, serial)
                infopc =  Display.display_info_pc()
                Archivo.archivo(infopc, nombre_disco, serial, modelo, interfaz)
                Display.display_alerta()
                Sistema.bloqueo()  # Bloquea USB si detecta dispositivo
                
            except Exception as e:
                print(f"{Errores.MSG_ERROR_DISPOSITIVO}{e}")
    except Exception as e:
        print(f"{Errores.MSG_ERROR_INFO}{e}")