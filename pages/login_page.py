from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger_setup import login_logger

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        login_logger.info(f"Attempting login for user: {username}")
        self.visit(self.URL)
        self.fill_text(self.USERNAME_INPUT, username)
        self.fill_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        login_logger.info("Login action complete, checking results.")

    def get_error_message(self):
        error_text = self.find_element(self.ERROR_MESSAGE).text
        login_logger.warning(f"Login failed. Error message displayed: '{error_text}'")
        return error_text
