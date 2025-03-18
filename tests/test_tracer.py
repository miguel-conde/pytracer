import os
import logging
import pytest
from pytracer.tracer import setup_logger


def test_logger_initialization():
    """Verifica que el logger se inicializa correctamente con el nombre esperado y el nivel adecuado."""
    os.environ.pop("LOG_LVL", None)  # Asegurar que no hay valores previos
    logger = setup_logger()
    assert logger.name == "app_tracer"
    assert isinstance(logger, logging.Logger)
    assert logger.hasHandlers()  # Debe tener al menos un handler (consola o archivo)
    assert logger.getEffectiveLevel() in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]

@pytest.mark.parametrize("log_level", ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
def test_logger_respects_env_variable(log_level):
    """Verifica que el logger respeta el nivel de logging configurado en LOG_LVL."""
    os.environ["LOG_LVL"] = log_level
    logger = setup_logger()
    assert logger.getEffectiveLevel() == getattr(logging, log_level)

@pytest.mark.parametrize("invalid_level", ["INVALID", "123", "", None])
def test_logger_defaults_to_info_on_invalid_level(invalid_level):
    """Verifica que el logger usa INFO si se configura un nivel inválido en LOG_LVL."""
    os.environ["LOG_LVL"] = invalid_level if invalid_level is not None else ""
    logger = setup_logger()
    assert logger.getEffectiveLevel() == logging.INFO

def test_logger_writes_to_file(tmp_path):
    """Verifica que el logger escribe en un archivo de log."""
    log_file = tmp_path / "application.log"
    os.environ["LOG_DIR"] = str(tmp_path)
    os.environ["LOG_TO_FILE"] = "true"
    os.environ["LOG_UNIQUE_FILE"] = "false"
    os.environ["LOG_LVL"] = "INFO"
    
    logger = setup_logger()
    logger.setLevel(logging.INFO)
    
    logger.info("Test message")
    
    # Asegurar que el archivo se ha creado correctamente
    assert log_file.exists(), f"El archivo de log no se creó: {log_file}"
    with open(log_file, "r") as f:
        content = f.read()
        assert "Test message" in content