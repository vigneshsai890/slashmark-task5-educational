from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProgressPage(BasePage):
    PROGRESS_URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_progress"
    SIMPLE_URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_default"

    IFRAME = (By.ID, "iframeResult")
    PROGRESS_ELEMENT = (By.CSS_SELECTOR, "progress")
    PAGE_HEADING = (By.TAG_NAME, "h1")
    BODY_TEXT = (By.TAG_NAME, "body")

    def open(self):
        self.driver.get(self.PROGRESS_URL)
        try:
            iframe = self.find(*self.IFRAME)
            self.driver.switch_to.frame(iframe)
        except Exception:
            pass
        return self

    def switch_to_default(self):
        self.driver.switch_to.default_content()
        return self

    def is_progress_present(self):
        return self.is_visible(*self.PROGRESS_ELEMENT, timeout=15)

    def get_progress_value(self):
        el = self.find(*self.PROGRESS_ELEMENT)
        return el.get_attribute("value")

    def get_progress_max(self):
        el = self.find(*self.PROGRESS_ELEMENT)
        return el.get_attribute("max")

    def get_progress_percentage(self):
        val = self.get_progress_value()
        mx = self.get_progress_max()
        if val and mx:
            return int(val) / int(mx) * 100
        return 0

    def get_body_text(self):
        body = self.find(*self.BODY_TEXT)
        return body.text

    def get_heading_text(self):
        try:
            h1 = self.find(*self.PAGE_HEADING)
            return h1.text
        except Exception:
            return ""
