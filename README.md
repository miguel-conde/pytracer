# PyTracer

PyTracer is a Python library for setting up and managing a logger with advanced formatting and options. It supports logging to both console and file, with configurable log levels and file handling options.

## Features

- Configurable log levels via environment variables
- Logging to console and/or file
- Advanced log formatting
- Support for unique log files

## Installation

To install PyTracer directly from GitHub, use the following command:

```bash
pip install git+https://github.com/miguel-conde/pytracer.git
```

or, if you want to install it from the `develop` branch:

```bash
pip install git+https://github.com/miguel-conde/pytracer.git@develop
```

## Usage

### Basic Usage

To use PyTracer, import the `tracer` logger and log messages at different levels:

```python	
import logging
from pytracer.tracer import tracer  # Import the configured logger

# Optional: Change logging level dynamically
tracer.setLevel(logging.DEBUG)

def main():
    tracer.debug("🔍 Debug message: Useful for diagnosing issues during development.")
    tracer.info("ℹ️ Info message: General application progress updates.")
    tracer.warning("⚠️ Warning message: Something unexpected but not an error.")
    tracer.error("❌ Error message: A serious issue that needs attention.")
    tracer.critical("🔥 Critical message: A severe failure, the program may crash.")

if __name__ == "__main__":
    main()
```

Alternatively, you can use the `setup_logger` function to create a logger with the default configuration:

```python
from pytracer.tracer import setup_logger

# Setup the logger
logger = setup_logger()

# Log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

👉 Use `setup_logger()` (**Second Approach**) when:

+ You need more control over logging configuration.
+ You are working on a larger project where logging settings may change dynamically.
+ You want better testability (e.g., create fresh loggers in unit tests).

👉 Use `tracer` (**First Approach**) when:

+ You want a simpler and consistent logging setup.
+ The default logging configuration in `tracer.py` is good enough for your use case.
+ You are writing a small script where reconfiguring the logger isn't necessary.

Instead of choosing one, you can use **both strategically**:

```python
from pytracer.tracer import setup_logger

# Create a logger instance
logger = setup_logger()

# If needed, dynamically change settings
logger.setLevel(logging.DEBUG)

logger.info("Application started!")
logger.warning("This is a warning message.")
logger.error("Something went wrong!")

# Now, if another module imports `tracer`, it will use the same configuration.
```

This approach **keeps the flexibility of `setup_logger()` while maintaining a global logger instance**.

### Configuring Log Level

You can configure the log level using the `LOG_LVL` environment variable:

```bash
export LOG_LVL=DEBUG
```

### Logging to File

To enable logging to a file, set the `LOG_TO_FILE` environment variable to `true` and specify the log directory with `LOG_DIR`:

```bash
export LOG_TO_FILE=true
export LOG_DIR=/path/to/logs
```

### Unique Log Files

To create unique log files for each run, set the `LOG_UNIQUE_FILE` environment variable to `true`:

```bash
export LOG_UNIQUE_FILE=true
```

### Custom Log File Name

To specify a custom name for the log file, set the `LOG_NAME` environment variable:

```bash
export LOG_NAME=my_custom_log.log
```

## Testing

To run the tests, use `pytest`:

```bash
pytest
```

## License

This project is licensed under the MIT License.
