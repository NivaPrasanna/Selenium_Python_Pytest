import logging
import os

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    handler = logging.FileHandler(f'logs/{log_file}', mode='w')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    # Also add a stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# Setup the main test logger
helpers_logger = setup_logger('helpers_log', 'automation.log')
base_logger = setup_logger('base_page_log', 'automation.log')
login_logger = setup_logger('login_page_log', 'automation.log')
inventory_logger = setup_logger('inventory_page_log', 'automation.log')
test_logger = setup_logger('test_runner_log', 'test_execution.log')


