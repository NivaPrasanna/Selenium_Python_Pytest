import pytest
import logging
from selenium.common.exceptions import WebDriverException, TimeoutException
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.helpers import get_config, setup_driver
#from utils.logger_setup import test_logger  # Import the test runner specific logger
from faker import Faker
import os

fake = Faker()
test_logger = logging.getLogger(__name__)
# Ensure logging is configured to output INFO messages (usually done in conftest.py or run command)
logging.basicConfig(level=logging.INFO)
CONFIG = get_config()
os.makedirs('reports/screenshots', exist_ok=True)


class TestSauceDemo:


  def test_successful_login_and_form_submission(self,driver, request):
     test_name = request.node.name
     test_logger.info(f"--- Starting Test Case: {test_name} ---")
     # Use a finalizer for actions that must happen after the test (e.g., screenshots on failure)
     # This is more robust than a generic try/except in the test body.
     # def finalizer():
     #     if request.node.rep_call.failed:
     #         test_logger.error(f"Test failed. Capturing screenshot for {test_name}.")
     #         # This method needs to be implemented in your InventoryPage class
     #         screenshot_path = InventoryPage(driver).take_screenshot(test_name)
     #         test_logger.info(f"Screenshot captured at: {screenshot_path}")
     #
     # request.addfinalizer(finalizer)
     try:
          # --- Test Logic Starts Here ---
          login_page = LoginPage(driver)
          inventory_page = InventoryPage(driver)


          # --- Login Automation ---
          test_logger.info(f"Action: Login to website.")
          login_page.login(CONFIG['valid_username'], CONFIG['valid_password'])

          # --- Assertion & Verification ---
          assert inventory_page.is_dashboard_visible(), "Dashboard page did not load."
          assert "Swag Labs" in driver.title
          test_logger.info("Verification: User successfully logged in and dashboard elements are present.")

          # --- Form Submission ---
          test_logger.info("Action: Navigating to checkout form.")
          inventory_page.navigate_to_checkout_form()

          first_name = fake.first_name()
          last_name = fake.last_name()
          postal_code = fake.postcode()

          test_logger.info("Action: Filling form fields with Faker data.")
          inventory_page.fill_checkout_form(first_name, last_name, postal_code)

          # Submit the form
          test_logger.info("Action: Submitting the order.")
          inventory_page.submit_checkout()

          # Verify the success message appears
          success_message = inventory_page.get_success_message()
          test_logger.info("Verification: Checking for order confirmation message.")
          assert "THANK YOU FOR YOUR ORDER" in success_message, f"Expected success message not found."

          test_logger.info("--- Test Passed Successfully ---")

     except AssertionError as e:
          test_logger.error(f"Assertion failed for test '{test_name}': {e}")
          screenshot_path = inventory_page.take_screenshot(test_name)
          test_logger.info(f"Screenshot captured at: {screenshot_path}")
          pytest.fail(f"Test failed due to assertion error: {e}")

     except (WebDriverException, TimeoutException) as e:
          test_logger.error(f"A WebDriver error occurred during test '{test_name}': {e}", exc_info=True)
          screenshot_path = inventory_page.take_screenshot(test_name)
          test_logger.info(f"Screenshot captured at: {screenshot_path}")
          pytest.fail(f"Test failed due to WebDriver issue: {e}")

     except Exception as e:
          test_logger.error(f"An unexpected error occurred during test '{test_name}': {e}", exc_info=True)
          screenshot_path = inventory_page.take_screenshot(test_name)
          test_logger.info(f"Screenshot captured at: {screenshot_path}")
          pytest.fail(f"Test failed due to unexpected error: {e}")
