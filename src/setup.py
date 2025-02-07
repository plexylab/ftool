"""
`ESP32 Firmware Updater`
-----------------------

Este script permite flashear el firmware de un ESP32 utilizando `esptool.py`.

Esptool es una herramienta de código abierto desarrollada por Espressif para 
la programación de chips ESP32, ESP8266 y otros dispositivos de la familia ESP.

Esptool Repository: https://github.com/espressif/esptool
Licencia: GNU General Public License v2.0 (GPL-2.0)

Author(s): 
    Sebastián Abril

Copyright:
    * (c) 2025 Sebastián Abril for PLEXYLAB RESEARCH (R)

License:
    GNU General Public License v2.0 (GPL-2.0)
    
Organization:
    `PLEXYLAB RESEARCH (R)`
"""

import sys
import time
import serial.tools.list_ports
import subprocess
from pathlib import Path

# Ruta del directorio raíz del proyecto.
ROOT_PATH = Path(__file__).resolve().parent.parent

# Ruta del ejecutable de esptool.py dentro del proyecto
ESPTOOL_PATH = ROOT_PATH / "lib" / "esptool" / "esptool.py"

# Ruta del directorio de binarios
BINS_PATH = ROOT_PATH / "bins"

# Archivos de firmware
BOOTLOADER = BINS_PATH / "bootloader.bin"
PARTITIONS = BINS_PATH / "partitions.bin"
FIRMWARE = BINS_PATH / "firmware.bin"   

# Listar los puertos COM disponibles
def listar_puertos():
    print("│  ├─ Listando puertos COM:")
    puertos = serial.tools.list_ports.comports()
    if not puertos:
        print("│  │ └─ No se encontraron puertos COM.")
        sys.exit()
    
    print(f"│  │  ├─ [0] EXIT\t- Para salir")
    i = 0
    for i, puerto in enumerate(puertos):
        print(f"│  │  ├─ [{i+1}] {puerto.device}\t- {puerto.description}")
    
    print(f"│  │  └─ Total: {i+1} puertos.")
    return puertos

# Solicitar puerto al usuario
def seleccionar_puerto():
    print("├─ Seleccionar puerto COM:")
    puertos = listar_puertos()
    seleccion = input("│  ├─ Seleccione el COM usando el [número] de la lista: ")
    try:
        seleccionInt = int(seleccion)-1
        if seleccionInt < 0:
            print("│  │  └─ Terminando programa.")
            sys.exit()

        return puertos[seleccionInt]
    except (IndexError, ValueError):
        print("│  │  └─ Selección inválida.")
        sys.exit()

# Validacion simple si el dispositivo es 
# compatible con hardware de PLEXYLAB.
def validar_dispositivo(puerto):
    if not "CH340" in puerto.description and not "CP2100" in puerto.description:
        print("│  ├─ El dispositivo parece no ser compatible, no está basado en el Driver CH340 o CP2100")
        respuesta = input("│  ├─ Desea continuar? [s] para si, [n] para no: ")
        if respuesta != "s":
            return False
    return True

# Borra toda la flash del dispositivo.
def borrar_dispositivo(puerto):
    print("│")
    print(f"├─ Iniciando borrado en {puerto}...")

    # Comando para ejecutar esptool.py desde la carpeta local
    comando = [
        sys.executable, ESPTOOL_PATH,  # Ejecutar con Python local
        "--chip", "esp32",
        "--port", puerto,
        "erase_flash"
    ]

    # Ejecutar esptool con subprocess
    try:
        subprocess.run(comando, check=True)
        print("│  └─ Borrado completado. Reinicie el dispositivo.")
    except subprocess.CalledProcessError:
        print("│  └─ Error durante el borrado.")
    time.sleep(1)

# Flashear dispositivo
def flashear_dispositivo(puerto):
    print("│")
    print(f"├─ Iniciando actualización en {puerto}...")
    print(BOOTLOADER)
    print(PARTITIONS)
    print(FIRMWARE)

    # Comando para ejecutar esptool.py desde la carpeta local
    comando = [
        sys.executable, ESPTOOL_PATH,  # Ejecutar con Python local
        "--chip", "esp32",
        "--port", puerto,
        "--baud", "460800",
        "write_flash", "-z",
        "--flash_mode", "dio",
        "--flash_freq", "40m",
        "--flash_size", "detect",
        "0x1000", BOOTLOADER,
        "0x8000", PARTITIONS,
        "0x10000", FIRMWARE
    ]

    # Ejecutar esptool con subprocess
    try:
        subprocess.run(comando, check=True)
        print("│  └─ Flasheo completado. Reinicie el dispositivo.")
    except subprocess.CalledProcessError:
        print("│  └─ Error durante el flasheo.")
    time.sleep(1)

# 
def init(modo=None):
    print("╻")
    puerto = seleccionar_puerto()
    if validar_dispositivo(puerto):
        borrar_dispositivo(puerto.device)
        flashear_dispositivo(puerto.device)
    else:
        print("│  └─ Terminando programa.")
    print("╹")