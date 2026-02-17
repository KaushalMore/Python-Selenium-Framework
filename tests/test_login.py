'''
from selenium import webdriver

from pages.login_page import LoginPage

def test_valid_login(driver):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    try:
        login_page = LoginPage(driver)
        # login_page.login("student", "Password123")
        login_page.enter_username("student")
        login_page.enter_password("Password123")
        login_page.click_submit()

        assert "logged-in-successfully" in driver.current_url, login_page.get_error_message()
        print("Login Test Passed")

    except Exception as e:
        print(f"Login Test Failed {e}")
    finally:
        driver.quit()
'''

'''
# import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("student", "Password123")
    assert "logged-in-successfully" in driver.current_url, login_page.get_error_message()
    print("Login Test Passed")

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("student", "Password123")
    assert "logged-in-successfully" in driver.current_url, login_page.get_error_message()
    print("Login Test Passed")
'''

'''
from pages.login_page import LoginPage

def test_valid_login(driver, config):
    login_page = LoginPage(driver)

    login_page.open_login_page(config.get("base_url"))
    login_page.login(config.get("valid_username"), config.get("valid_password"))

    assert "Logged In Successfully" in login_page.get_success_message()


def test_invalid_login(driver, config):
    login_page = LoginPage(driver)

    login_page.open_login_page(config.get("base_url"))
    login_page.login(config.get("invalid_username"), config.get("invalid_password"))

    assert "Your username is invalid!" in login_page.get_error_message()
'''

from pages.login_page import LoginPage
from tests.base_test import BaseTest
import pytest


@pytest.mark.smoke
class TestLogin(BaseTest):
    def test_valid_login(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_page(self.config.get("base_url"))
        login_page.login(self.config.get("valid_username"), self.config.get("valid_password"))

        assert "Logged In Successfully" in login_page.get_success_message()

    @pytest.mark.regression
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_page(self.config.get("base_url"))
        login_page.login(self.config.get("invalid_username"), self.config.get("invalid_password"))

        assert "Your username is invalid!" in login_page.get_error_message()
