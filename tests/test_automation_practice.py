from selenium import webdriver

from pages.automation_practice_page import AutomationPracticePage

'''
def test_automation_practice():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")

    try:
        app = AutomationPracticePage(driver)

        app.enter_name("Kaushal More")
        app.enter_email("more@gmail.com")
        app.enter_phone("1234567890")
        app.enter_address("Thane")

        app.click_male()
        app.click_sunday()
        app.click_saturday()

        app.enter_start_date("20-11-2025")
        app.enter_end_date("11-02-2026")
        app.click_submit()

        days = app.get_calculated_days()
        print(days)

        app.select_country_by_value("india")
        app.select_colors_by_visible_text("Green")
        app.select_animals_by_visible_text("Dog")

    except Exception as e:
        print(f"Test Failed : {e}")
    finally:
        driver.quit()
'''
