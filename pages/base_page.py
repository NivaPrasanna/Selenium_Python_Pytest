from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from utils.logger_setup import base_logger
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        base_logger.info("BasePage initialized.")

    def visit(self, url):
        base_logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)

    def find_element(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            base_logger.debug(f"Found element using locator: {locator}")
            return element
        except (TimeoutException, NoSuchElementException):
            base_logger.error(f"Could not find element with locator {locator} within timeout period.")
            raise

    def click_element(self, locator):
        base_logger.info(f"Attempting to click element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        base_logger.debug("Element clicked successfully.")

    def fill_text(self, locator, text):
        base_logger.info(f"Filling text field {locator} with data.")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        base_logger.debug("Text entered successfully.")

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            base_logger.debug(f"Element {locator} is visible.")
            return True
        except TimeoutException:
            base_logger.debug(f"Element {locator} is not visible.")
            return False

    def take_screenshot(self, test_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f'reports/screenshots/{test_name}_{timestamp}.png'
        self.driver.save_screenshot(screenshot_name)
        base_logger.info(f"Screenshot captured: {screenshot_name}")
        return screenshot_name

    # def take_screenshot_on_failure(self, test_name):
    #     """
    #     Captures a screenshot with a timestamp specifically for failed tests.
    #     """
    #     # Ensure the directory exists
    #     os.makedirs(self.save_dir, exist_ok=True)
    #
    #     timestamp = time.strftime("%Y%m%d-%H%M%S")
    #     # Naming convention: FAILED_TESTNAME_TIMESTAMP.png
    #     screenshot_name = f'FAILED_{test_name}_{timestamp}.png'
    #     screenshot_path = os.path.join(self.save_dir, screenshot_name)
    #
    #     self.driver.save_screenshot(screenshot_path)
    #     base_logger.info(f"Screenshot captured due to failure: {screenshot_path}")
    #     return screenshot_path
