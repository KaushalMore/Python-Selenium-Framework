import allure
import pytest
from pages.sauce_demo_login_page import SauceDemoLoginPage
from utils.excel_reader import get_test_data

test_data = get_test_data()


@pytest.mark.parametrize("username,password", test_data)
@allure.feature("SauceDemo Login")
def test_sauce_demo_login(driver, username, password):
    login_page = SauceDemoLoginPage(driver)

    with allure.step("Open SauceDemo Login page"):
        login_page.open_login_page()

    with allure.step(f"Login with username: {username}"):
        login_page.login(username, password)
