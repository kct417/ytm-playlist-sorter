import logging
import logging.config


# Custom formatter to add color to log messages
class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
        "RESET": "\033[0m",
    }

    # Override the format method to add color
    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        reset = self.COLORS["RESET"]
        message = super().format(record)
        return f"{color}{message}{reset}"


# Setup logger with custom configuration
def setup_logger(name, **kwargs):
    level = kwargs.get("level", logging.INFO)
    log_file = kwargs.get("log_file", "ytm-sorter.log")

    console_level = kwargs.get("console_level", "INFO")
    file_level = kwargs.get("file_level", "DEBUG")

    fmt = kwargs.get(
        "fmt", "%(name)s - %(funcName)s - %(levelname)s:\n[%(asctime)s] %(message)s\n"
    )
    datefmt = kwargs.get("datefmt", "%m-%d-%Y %H:%M:%S")

    # Configuration for logging
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "color": {"()": ColorFormatter, "format": fmt, "datefmt": datefmt},
            "standard": {"format": fmt, "datefmt": datefmt},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": console_level,
                "formatter": "color",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.FileHandler",
                "level": file_level,
                "formatter": "standard",
                "filename": log_file,
                "mode": "a",
                "encoding": "utf-8",
            },
        },
        "root": {"handlers": ["console", "file"]},
    }

    logging.config.dictConfig(config)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Uncomment lines and comment config if you want to add handlers manually

    # outputHandler = logging.StreamHandler()
    # outputHandler.setFormatter(ColorFormatter(fmt=fmt, datefmt=datefmt))

    # fileHandler = logging.FileHandler(log_file)
    # fileHandler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    # if not logger.handlers:
    #     logger.addHandler(outputHandler)
    #     logger.addHandler(fileHandler)

    return logger
