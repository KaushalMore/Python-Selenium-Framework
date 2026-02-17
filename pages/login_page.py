from selenium.common import NoSuchElementException
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = ("id", "username")
    PASSWORD_FIELD = ("id", "password")
    SUBMIT_BUTTON = ("id", "submit")
    ERROR_MESSAGE = ("id", "error")
    SUCCESS_MESSAGE = ("tag name", "h1")

    # def __init__(self, driver):
    #     super().__init__(driver)

    def open_login_page(self, base_url):
        self.get_url(f"{base_url}/practice-test-login/")

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)
        self.logger.info(f"Entered username : {username}")

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        self.logger.info(f"Entered password : {password}")

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)
        self.logger.info(f"submitted button is clicked")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except NoSuchElementException:
            return None
