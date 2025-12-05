from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger_setup import inventory_logger


class InventoryPage(BasePage):
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ADD_SAUCE_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def is_dashboard_visible(self):
        is_visible = self.is_element_visible(self.INVENTORY_LIST)
        inventory_logger.info(f"Dashboard visibility check returned: {is_visible}")
        return is_visible

    def navigate_to_checkout_form(self):
        inventory_logger.info("Adding item to cart and proceeding to checkout form.")
        self.click_element(self.ADD_SAUCE_LABS_BACKPACK)
        self.click_element(self.CART_BUTTON)
        self.click_element(self.CHECKOUT_BUTTON)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        inventory_logger.info("Filling checkout user information.")
        self.fill_text(self.FIRST_NAME_INPUT, first_name)
        self.fill_text(self.LAST_NAME_INPUT, last_name)
        self.fill_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click_element(self.CONTINUE_BUTTON)

    def submit_checkout(self):
        inventory_logger.info("Submitting the final order.")
        self.click_element(self.FINISH_BUTTON)

    def get_success_message(self):
        success_text = self.find_element(self.COMPLETE_HEADER).text
        inventory_logger.info(f"Order success message retrieved: '{success_text}'")
        return success_text
