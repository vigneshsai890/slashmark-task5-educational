from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EducationalLoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MSG = (By.ID, "flash")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(*self.USERNAME, username)
        self.type_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        return self

    def get_flash_message(self):
        return self.get_text(*self.FLASH_MSG)

    def is_flash_displayed(self):
        return self.is_visible(*self.FLASH_MSG)

    def is_login_successful(self):
        text = self.get_flash_message()
        return "You logged into a secure area!" in text

    def is_login_failed(self):
        text = self.get_flash_message()
        return "Your password is invalid!" in text or "Your username is invalid!" in text

    def is_logout_link_present(self):
        return self.is_visible(*self.LOGOUT_LINK)

    def logout(self):
        self.click(*self.LOGOUT_LINK)
        return self
