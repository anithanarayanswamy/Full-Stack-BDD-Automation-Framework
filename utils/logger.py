"""
Logging setup for test framework
"""
import logging
import os
from datetime import datetime

def setup_logger(name):
    """Setup logger for test execution"""
    
    # Create logs directory
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Create file handler
    log_file = f"reports/test_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Test the logger
if __name__ == "__main__":
    logger = setup_logger("test")
    logger.info("Logger setup successful!")
    logger.debug("This is a debug message")
    logger.warning("This is a warning")