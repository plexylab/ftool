# ftool - Software de Carga de Firmware para Dispositivos Compatibles
Herramienta para carga de firmware mediante interfaz USB en dispositivos desarrollados por PLEXYLAB RESEARCH.

![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fplexylab%2Fftool%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&label=Estado&query=%24.project.status&color=orange)
![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fplexylab%2Fftool%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&label=Versión&query=%24.project.version&color=red)
![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fplexylab%2Fftool%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&label=Licencia&query=%24.project.license.text)

## Características principales
Este repositorio contiene el código fuente de ftool, una herramienta para la carga de firmware propietario y de código abierto, incluyendo **Micropython**, en dispositivos compatibles desarrollados por **PLEXYLAB RESEARCH**. Basado en **Esptool**, permite actualizar, flashear y gestionar el firmware de manera confiable y eficiente.

> **⚠️ Nota:** Esta versión de `ftool`, por el momento carga el firmware **v1.1.0** del dispositivo **DoorLink**. En la próxima versión, se incorporará la funcionalidad para descargar automáticamente la última versión del firmware del dispositivo DoorLink.

## Instalación

Para ejecutar este proyecto, necesita tener instalado **Python 3.8 o una versión posterior**. Si aún no lo tiene, descárguelo e instálale desde la página oficial de Python: [Descargar Python](https://www.python.org/downloads/)

### Verificar que Python está instalado
Para comprobar si Python está instalado en su sistema, ejecute el siguiente comando en la terminal o consola:

```sh
python --version
```

## Dependencias

Antes de ejecutar el proyecto, instalar las dependencias necesarias:

```sh
pip install pyserial
```

## Instrucciones de Ejecución

Para ejecutar correctamente el software, siga los pasos detallados a continuación:

1. **Conexión del dispositivo:**
   - Asegúrese de que el dispositivo esté conectado al PC mediante la interfaz **USB-C**.

2. **Verificación de reconocimiento del dispositivo:**
   - Acceda al **Administrador de dispositivos** (Windows) o utilice el comando `ls /dev/tty*` en Linux/Mac para verificar si el dispositivo es reconocido.
   - Si el dispositivo es detectado correctamente, debe aparecer un dispositivo COM cuya descripción contenga el texto **CH340**.
   - Si el dispositivo **no es detectado**, será necesario instalar el controlador correspondiente para el chip **CH340**.
     - El driver CH340 puede ser descargado en la sección **Driver&Tools** del siguiente enlace: [Descargar CH340](https://www.wch-ic.com/search?q=CH340&t=downloads)
     - Seleccione la opción correcta según su sistema operativo (**Windows, Linux o Mac**).

3. **Ejecución del script `ftool.py`:**
   - Una vez que el dispositivo haya sido reconocido por el sistema, ejecute el siguiente comando en la terminal o consola:
     
     ```sh
     python ftool.py
     ```
   - Al ejecutar el script, se abrirá una interfaz de consola que solicitará al usuario seleccionar el puerto **COM** en el que está conectado el dispositivo.
     
   ![image](https://github.com/user-attachments/assets/46379be2-6b90-4291-b04d-bb062ee662c5)


4. **Selección del puerto COM:**
   - Se mostrará una lista enumerando los puertos disponibles. Para seleccionar el puerto correcto, ingrese el **[número]** que lista al puerto correspondiente.
   - Verifique que en la descripción del puerto **COM** seleccionado aparezca el texto **CH340**, lo que confirmará que el dispositivo ha sido correctamente identificado.
  
   ![image](https://github.com/user-attachments/assets/50bbbb97-98ed-4e93-b550-2ba7e5730082)


5. **Proceso de instalación del firmware:**
   - Si el puerto seleccionado es válido, el proceso de **borrado e instalación del firmware** se iniciará automáticamente.

   ![image](https://github.com/user-attachments/assets/4c8b2f19-ac7c-4240-9049-016b93dae196)


6. **Finalización del proceso:**
   - Una vez finalizado el proceso de instalación, desconecte el dispositivo del PC.
   - El dispositivo estará listo para su uso.
  
   ![image](https://github.com/user-attachments/assets/866e0155-60fc-49af-b597-cc66493b0cb8)


Siguiendo estos pasos, se garantizará una instalación y ejecución correctas del software.

## Reconocimiento

Este proyecto se basa en **Esptool**, una herramienta desarrollada y mantenida por **Espressif Systems**, con contribuciones significativas de **Fredrik Ahlberg (@themadinventor)** y otros colaboradores de la comunidad.

Agradecemos a **Fredrik Ahlberg** por su trabajo en la creación de **Esptool**, que ha sido fundamental para la programación y gestión de dispositivos **ESP8266**, **ESP32** y variantes.

Para más información sobre **Esptool**, visita su repositorio oficial en: 🔗 [GitHub - Esptool](https://github.com/espressif/esptool)

## Licencia

Este proyecto se distribuye bajo la **Licencia Pública General de GNU, versión 2 (GPL-2.0)**. Esto significa que el software es libre y de código abierto, permitiendo su uso, modificación y distribución, siempre y cuando se mantenga la misma licencia y se conserve la atribución al desarrollador (PLEXYLAB RESEACH).

Al utilizar o modificar este software, aceptas los términos de la **GPL-2.0**, que puedes consultar en el siguiente enlace: 🔗 [Licencia GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
