from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrgLoginPage(BasePage):

    #----locators---
    USERNAME_FIELD = (By.NAME,"username")
    PASSWORD_FIELD = (By.NAME,"password")
    SUBMIT_BUTTON = (By.XPATH,"//button[@type='submit']")

    def open_orglogin_page(self,base_url):
        self.get_url(base_url)

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    #-----Business Method-----
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()