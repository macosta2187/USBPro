import Errores   # Mensajes de error específicos para manejo de excepciones
import Archivo   # Variables de archivo y carpeta para logs
import os        # Para ejecutar comandos del sistema y manipular archivos



# Ruta donde se guardará la carpeta de logs
CARPETALOG = "C:\\Logs"

# Ruta completa en Windows del archivo de log
ARCHIVOLOG = "C:\\Logs\\log.txt"



def archivo(infopc, nombre_disco, serial, modelo, interfaz):
    """Registra la información del dispositivo USB detectado en un archivo de log."""
    try:
        os.makedirs(Archivo.CARPETALOG, exist_ok=True)  # Crea carpeta de logs si no existe
        with open(Archivo.ARCHIVOLOG, "a", encoding="utf-8") as f:
            f.write(f"PC: {infopc}, Disco: {nombre_disco}, Modelo: {modelo}, Interfaz: {interfaz}, Serial: {serial}\n")
    except Exception as e:
        print(f"{Errores.MSG_ERROR_ARCHIVO}{e}")