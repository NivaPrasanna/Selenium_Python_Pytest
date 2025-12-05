import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# For Edge (IE is deprecated and not recommended for modern testing)
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # For Edge

from selenium.webdriver.remote.webdriver import WebDriver
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="function")
def driver(request) -> WebDriver:
    """
    Provides a function-scoped Selenium WebDriver instance,
    dynamically selecting the browser based on the --driver CLI argument.
    """
    # Get the browser name from the command line argument (e.g., 'chrome', 'firefox', 'edge')
    # The default value is set to 'chrome' if the argument isn't provided in the CLI or pytest.ini
    browser_name = request.config.getoption("driver_name") or 'chrome'
    headless_mode = False  # Set to True if you want headless by default

    driver_instance = None

    if browser_name.lower() == 'chrome':
        options = ChromeOptions()
        if headless_mode:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        service = ChromeService(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=service, options=options)

    elif browser_name.lower() == 'firefox':
        options = FirefoxOptions()
        if headless_mode:
            options.add_argument('--headless')
        service = FirefoxService(GeckoDriverManager().install())
        driver_instance = webdriver.Firefox(service=service, options=options)

    elif browser_name.lower() == 'edge':
        # IE testing is obsolete; Edge is the modern Microsoft browser
        options = EdgeOptions()
        if headless_mode:
            options.add_argument('--headless')
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver_instance = webdriver.Edge(service=service, options=options)

    else:
        raise pytest.UsageError(f"Unsupported browser specified: {browser_name}. Use chrome, firefox, or edge.")

    # General driver setup
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)
    logging.info(f"Driver initialized for {browser_name} (Headless: {headless_mode})")

    # For pytest-selenium plugins/hooks
    if request.instance:
        request.instance.driver = driver_instance

    yield driver_instance

    # Teardown
    logging.info(f"Quitting {browser_name} driver...")
    driver_instance.quit()
