from selenium.common import NoSuchElementException
from pages.base_page import BasePage


class AutomationPracticePage(BasePage):
    NAME_FIELD = ("id", "name")
    EMAIL_FIELD = ("id", "email")
    PHONE_FIELD = ("id", "phone")
    ADDRESS_FIELD = ("id", "textarea")
    COUNTRY_SELECTOR = ("id", "country")
    COLORS_SELECTOR = ("id", "colors")
    ANIMALS_SELECTOR = ("id", "animals")
    MALE_GENDER = ("id", "male")
    SUNDAY_CHECKBOX = ("id", "sunday")
    SATURDAY_CHECKBOX = ("id", "saturday")
    SUBMIT_BUTTON = ("css selector", "button.submit-btn")
    START_DATE_FIELD = ("id", "start-date")
    END_DATE_FIELD = ("id", "end-date")
    CALCULATED_DAYS = ("id", "result")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self, name):
        self.send_keys(self.NAME_FIELD, name)
        print(f"Entered name : {name}")

    def enter_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)
        print(f"Entered email : {email}")

    def enter_phone(self, phone):
        self.send_keys(self.PHONE_FIELD, phone)
        print(f"Entered phone : {phone}")

    def enter_address(self, address):
        self.send_keys(self.ADDRESS_FIELD, address)
        print(f"Entered address : {address}")

    def click_male(self):
        self.click(self.MALE_GENDER)

    def click_sunday(self):
        self.click(self.SUNDAY_CHECKBOX)

    def click_saturday(self):
        self.click(self.SATURDAY_CHECKBOX)

    def enter_start_date(self, date):
        self.send_keys(self.START_DATE_FIELD, date)
        print(f"Entered start date : {date}")

    def enter_end_date(self, date):
        self.send_keys(self.END_DATE_FIELD, date)
        print(f"Entered end date : {date}")

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_calculated_days(self):
        return self.get_text(self.CALCULATED_DAYS)

    def select_country_by_value(self, country_value):
        self.select_by_value(self.COUNTRY_SELECTOR, country_value)

    def select_colors_by_visible_text(self, color):
        self.select_by_visible_text(self.COLORS_SELECTOR, color)

    def select_animals_by_visible_text(self, animal):
        self.select_by_visible_text(self.ANIMALS_SELECTOR, animal)
