# Selenium Python Pytest Automation Framework

A test automation framework built using Selenium, Python, and Pytest following the Page Object Model (POM) design pattern. This project automates a standard login and checkout process on the Swag Labs demo website.

## Prerequisites

Before running the tests, ensure you have the following installed:

*   **Python:** Version 3.10+ is recommended.
*   **Git:** For cloning the repository.

## Setup Instructions

1.  **Clone the repository** to your local machine:
    ```bash
    git clone github.com
    cd Selenium_Python_Pytest
    ```

2.  **Create and activate a virtual environment** (recommended):
    *   **Windows:**
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirement.txt
    ```

## How to Run the Tests

Tests are executed using the `pytest` command line tool. The framework is configured to use Chrome as the default browser via the `pytest.ini` file.

### Default Execution (Chrome)

To run all tests using the default configuration (Chrome browser, visible mode), simply use the `pytest` command from the project root directory:

```bash
pytest tests/test_saucedemo.py
Run with different browser
pytest tests/test_saucedemo.py --driver_name chrome
pytest tests/test_saucedemo.py --driver_name firefox
pytest tests/test_saucedemo.py --driver_name edge
Running in headless browser
pytest tests/test_saucedemo.py --headless

Project Structure Overview
The project follows a standard Page Object Model structure:
tests/: Contains the actual test case files (test_*.py).
pages/: Contains the Page Object classes (e.g., LoginPage, InventoryPage) that interact with the web elements.
utils/: Contains helper functions, configuration loading, and logging setup.
reports/: Stores test execution artifacts (screenshots, HTML reports).
conftest.py: Defines Pytest fixtures and hooks (like the driver setup and teardown).
pytest.ini: Configuration file for Pytest default options
