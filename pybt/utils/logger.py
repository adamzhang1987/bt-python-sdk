import logging
import sys
from typing import Optional

def setup_logger(
    name: str = "pybt",
    level: int = logging.DEBUG,
    log_file: Optional[str] = None
) -> logging.Logger:
    """Set up and configure the logger.
    
    Args:
        name: The name of the logger
        level: The logging level
        log_file: Optional file path to write logs to
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler if log_file is provided
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# Create default logger instance
logger = setup_logger() 