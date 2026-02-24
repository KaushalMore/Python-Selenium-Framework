import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
import os
import allure


# driver fixture
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://practicetestautomation.com/practice-test-login/")
#     yield driver
#     driver.quit()


# config fixture
@pytest.fixture(scope="session")
def config():
    return ConfigReader.read_config()


# driver fixture
@pytest.fixture
def driver(config):
    browser = config.get("browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise Exception(f"Unsupported browser {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


# screenshots on failed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            file_path = os.path.join(screenshot_dir, f"{item.name}.png")

            driver.save_screenshot(file_path)

            allure.attach.file(
                file_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

# how to skip to test cases
