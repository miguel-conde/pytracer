# Expected Behavior
# With LOG_LEVEL=INFO, the logger will:

# Ignore: DEBUG messages.
# Display: INFO, WARNING, ERROR, and CRITICAL messages.

# You can override the log level programmatically if required:
#     tracer.setLevel(logging.WARNING)  # Show only warnings and above

import logging
import os
from dotenv import load_dotenv, find_dotenv

# Cargar variables de entorno desde .env si está disponible
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

def get_log_level() -> int:
    """
    Obtiene el nivel de log desde la variable de entorno LOG_LVL.
    Si es inválido, devuelve INFO por defecto.
    """
    log_level_str = os.getenv("LOG_LVL", "INFO").upper()
    valid_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    
    if log_level_str not in valid_levels:
        print(f"⚠️ Nivel de log inválido '{log_level_str}', usando INFO por defecto.")
        return logging.INFO

    return valid_levels[log_level_str]

def setup_logger() -> logging.Logger:
    """
    Configura un logger global con formato estándar y manejo de errores en el archivo de logs.
    """
    logger = logging.getLogger("app_tracer")

    # Verificar si el logger ya está configurado
    if logger.hasHandlers():
        return logger

    log_level = get_log_level()
    logger.setLevel(log_level)

    # Formato de logs
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(module)s:%(funcName)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler para archivo (validando permisos)
    log_file = os.getenv("LOG_FILE", "application.log")
    
    try:
        file_handler = logging.FileHandler(log_file, mode="a")  # Append mode
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as e:
        logger.warning(f"No se pudo escribir en el archivo de logs '{log_file}': {e}")

    return logger

# Instancia global del logger
tracer = setup_logger()

# Registrar nivel de log actual
log_level_name = logging.getLevelName(tracer.getEffectiveLevel())
tracer.info(f"✅ Logger configurado. Nivel de log: {log_level_name}")
