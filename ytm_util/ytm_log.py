import logging
import logging.config


class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add color to log messages based on level.
    """

    COLORS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
        "RESET": "\033[0m",  # White
    }

    def format(self, record):
        """
        Format the log record with color based on the level.
        """

        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        reset = self.COLORS["RESET"]
        message = super().format(record)
        return f"{color}{message}{reset}"


def setup_logger(name, **kwargs):
    """
    Setup a logger with custom configuration.
    """

    # Log settings
    level = kwargs.get("level", logging.INFO)
    log_file = kwargs.get("log_file", "ytm-sorter.log")

    # Default levels for console and file handlers
    console_level = kwargs.get("console_level", "INFO")
    file_level = kwargs.get("file_level", "DEBUG")

    # Disable console and file handlers
    disable_console = kwargs.get("disable_console", False)
    disable_file = kwargs.get("disable_file", False)

    # Default format and date format
    fmt = kwargs.get(
        "fmt", "%(name)s - %(funcName)s - %(levelname)s:\n[%(asctime)s] %(message)s\n"
    )
    datefmt = kwargs.get("datefmt", "%m-%d-%Y %H:%M:%S")

    handlers = {}

    if not disable_console:
        handlers["console"] = {
            "class": "logging.StreamHandler",
            "level": console_level,
            "formatter": "color",
            "stream": "ext://sys.stdout",
        }

    if not disable_file:
        handlers["file"] = {
            "class": "logging.FileHandler",
            "level": file_level,
            "formatter": "standard",
            "filename": log_file,
            "mode": "a",
            "encoding": "utf-8",
        }

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": fmt, "datefmt": datefmt},
            "color": {"()": ColorFormatter, "format": fmt, "datefmt": datefmt},
        },
        "handlers": handlers,
        "root": {"handlers": list(handlers.keys())},
    }

    logging.config.dictConfig(config)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger


def set_third_party_logging_level(modules, level=logging.ERROR):
    """
    Set the logging level for third-party libraries.
    """

    for name, logger in logging.root.manager.loggerDict.items():
        if not isinstance(logger, logging.Logger):
            continue

        # Keep loggers that match the given modules or their submodules
        if not any(name == mod or name.startswith(mod + ".") for mod in modules):
            logger.setLevel(level)
