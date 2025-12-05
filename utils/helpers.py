import json
from selenium import webdriver
from utils.logger_setup import helpers_logger


def get_config():
    helpers_logger.info("Reading configuration from config.json")
    with open('config.json', 'r') as f:
        return json.load(f)


def setup_driver(headless=False):
    helpers_logger.info(f"Setting up Chrome WebDriver (Headless mode: {headless})")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        helpers_logger.info("Configured options for headless execution.")

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        helpers_logger.info("Driver initialized successfully and window maximized.")
        return driver
    except Exception as e:
        helpers_logger.error(f"Failed to initialize WebDriver: {e}", exc_info=True)
        raise


def capture_screenshot(driver, name):
    # This utility function is essentially replaced by the BasePage method now
    pass
