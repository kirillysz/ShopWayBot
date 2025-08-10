import logging

_logger = logging.getLogger("Logger")
_logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
_logger.addHandler(console_handler)