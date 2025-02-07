
import src.setup as setup
import src.utils as utils

# main.py o __init__.py
__author__ = "Sebastián Abril"
__copyright__ = "PLEXYLAB RESEARCH (C) 2025"
__license__ = "GNU-2.0"
__version__ = "1.1.0"
__email__ = "sebastiabril2@gmail.com"
__status__ = "Desarrollo"  # Puede ser 'Producción', 'Beta', etc.

# Ejecutar el script
if __name__ == "__main__":
    
    print(utils.PLEXY_CMD_HEADER)
    print(f"│ Actualizador de firmware FTOOL v{__version__}", end="\n│")
    print(utils.SW_ACKNOW)

    setup.init()