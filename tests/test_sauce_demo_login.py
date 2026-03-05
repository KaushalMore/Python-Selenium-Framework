import allure
import pytest
from pages.sauce_demo_login_page import SauceDemoLoginPage
from utils.excel_reader import get_test_data

test_data = get_test_data()


@pytest.mark.parametrize("username, password, scenario", test_data)
def test_sauce_demo_login(driver, username, password, scenario):
    login_page = SauceDemoLoginPage(driver)

    allure.dynamic.feature("SauceDemo Login")

    allure.dynamic.story(f"{scenario} Testing")

    allure.dynamic.description(
        f"This test verifies {scenario.lower()} login using username '{username}' and password '{password}'.")

    with allure.step("Open SauceDemo - Login page"):
        login_page.open_login_page()

    with allure.step(f"Login with username: {username}"):
        login_page.login(username, password)
