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
import allure

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
@allure.feature("PracticeTestAutomation Login")
class TestLogin(BaseTest):
    def test_valid_login(self):
        login_page = LoginPage(self.driver)

        with allure.step("Opening Login Page"):
            login_page.open_login_page()

        with allure.step(f"Entering Valid Username: {self.config['environments']['practice']['valid_username']}"):
            login_page.enter_username(self.config["environments"]["practice"]["valid_username"])

        with allure.step(f"Entering Valid Password: {self.config['environments']['practice']['valid_password']}"):
            login_page.enter_password(self.config["environments"]["practice"]["valid_password"])

        with allure.step("Click submit button"):
            login_page.click_submit()

        with allure.step("Verifying Success Login"):
            assert "Logged In Successfully" in login_page.get_success_message()

    @pytest.mark.regression
    @allure.feature("PracticeTestAutomation Login")
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)

        with allure.step("Opening Login Page"):
            login_page.open_login_page()

        with allure.step(f"Entering Invalid Username: {self.config['environments']['practice']['invalid_username']}"):
            login_page.enter_username(self.config["environments"]["practice"]["invalid_username"])

        with allure.step(f"Entering Invalid Password: {self.config['environments']['practice']['invalid_password']}"):
            login_page.enter_password(self.config["environments"]["practice"]["invalid_password"])

        with allure.step("Click Submit Button"):
            login_page.click_submit()

        with allure.step("Verifying Error Message"):
            assert "Your username is invalid!" in login_page.get_error_message()
