from pages.orangehrm_login import OrgLoginPage
from utils.config_reader import ConfigReader
import allure

@allure.feature("Orange Login")
def test_orangehrm_login(cross_browser_driver):
    config = ConfigReader.read_config()
    orange_config = config["environments"]["orange_hrm"]

    base_url = orange_config["base_url"]
    username = orange_config["username"]
    password = orange_config["password"]

    login_page = OrgLoginPage(cross_browser_driver)
    with allure.step("Open Orange login page"):
        login_page.open_orglogin_page(base_url)
        login_page.login(username, password)