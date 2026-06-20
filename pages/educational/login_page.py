from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EducationalLoginPage(BasePage):
    URL = "https://sandbox.moodledemo.net/login/index.php"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
    ERROR_MSG = (By.CSS_SELECTOR, ".loginerror")
    GUEST_LOGIN = (By.LINK_TEXT, "Log in as a guest")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(*self.USERNAME, username)
        self.type_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        return self

    def login_as_guest(self):
        self.click(*self.GUEST_LOGIN)
        return self

    def get_error(self):
        return self.get_text(*self.ERROR_MSG)

    def is_error_displayed(self):
        return self.is_visible(*self.ERROR_MSG)
