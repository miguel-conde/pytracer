# Expected Behavior
# With LOG_LEVEL=INFO, the logger will:

# Ignore: DEBUG messages.
# Display: INFO, WARNING, ERROR, and CRITICAL messages.

# You can override the log level programmatically if required:
#     tracer.setLevel(logging.WARNING)  # Show only warnings and above

import logging
import os
from dotenv import load_dotenv, find_dotenv


# Load environment variables from .env if available
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

def get_log_level() -> int:
    """
    Retrieves the log level from the environment variable LOG_LVL.
    If it is invalid, returns INFO by default.
    
    Returns:
        int: Log level constant from the logging module.
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
        print(f"⚠️ Invalid log level '{log_level_str}', using INFO by default.")
        return logging.INFO

    return valid_levels[log_level_str]


def setup_logger() -> logging.Logger:
    """
    Configures the global logger with advanced formatting and options.
    
    Environment variables:
    + LOG_LVL: Sets the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default is INFO.
    + LOG_TO_FILE: If set to "true", logs will be written to a file. Default is "false".
    + LOG_DIR: Directory where log files will be stored. Default is "./logs".
    + LOG_UNIQUE_FILE: If set to "true", each log file will have a unique name based on the current timestamp. Default is "false".
    + LOG_NAME: Name of the log file. Default is "application.log".

    Returns:
        logging.Logger: Configured logger instance.
        
    Usage example:
    ```python	
    # Global logger instance
    tracer = setup_logger()
    
    # Use example
    if __name__ == "__main__":
        tracer.debug("This message will not be displayed")
        tracer.info("This message will be displayed")
        tracer.warning("This message will be displayed")
        tracer.error("This message will be displayed")
        tracer.critical("This message will be displayed")
    ```
    """
    logger = logging.getLogger("app_tracer")

    # Retrieve the log level from the environment variable
    log_level = os.getenv("LOG_LVL", "INFO").upper()
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if log_level not in valid_levels:
        log_level = "INFO"
    log_level = getattr(logging, log_level)

    # Configure the log format
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(module)s:%(funcName)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Configure the log level
    logger.setLevel(log_level)
    
    # Check if logging to file is enabled
    log_to_file = os.getenv("LOG_TO_FILE", "false").lower() == "true"
    log_dir = os.getenv("LOG_DIR", "./logs")
    unique_log = os.getenv("LOG_UNIQUE_FILE", "false").lower() == "true"
    log_name = os.getenv("LOG_NAME", "application.log")
    
    if log_to_file:
        os.makedirs(log_dir, exist_ok=True)
        if unique_log:
            from datetime import datetime
            log_filename = datetime.now().strftime("%Y%m%d%H%M%S_") + log_name
        else:
            log_filename = log_name
        log_file_path = os.path.join(log_dir, log_filename)

        has_file_handler = any(
            isinstance(h, logging.FileHandler) and h.baseFilename == log_file_path
            for h in logger.handlers
        )
        
        if not has_file_handler:
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
    # Configure the console handler only if not already added
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Global logger instance
tracer = setup_logger()

# Log current log level
log_level_name = logging.getLevelName(tracer.getEffectiveLevel())
tracer.info(f"✅ Logger configured. Log level: {log_level_name}")


# Use example

import logging
# from pytracer.tracer import tracer  # Importamos el logger configurado

# Optional configuration: Change the logging level dynamically
tracer.setLevel(logging.DEBUG)

# Uso del logger
def main():
    tracer.debug("🔍 Debug message: Useful for diagnosing issues during development.")
    tracer.info("ℹ️ Info message: General application progress updates.")
    tracer.warning("⚠️ Warning message: Something unexpected but not an error.")
    tracer.error("❌ Error message: A serious issue that needs attention.")
    tracer.critical("🔥 Critical message: A severe failure, the program may crash.")

if __name__ == "__main__":
    main()