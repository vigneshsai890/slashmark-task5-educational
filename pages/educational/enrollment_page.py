from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EnrollmentPage(BasePage):
    URL = "https://www.w3schools.com"
    TUTORIAL_URL = "https://www.w3schools.com/html/"

    MAIN = (By.ID, "main")
    SIDEBAR = (By.ID, "sidenav")
    SIDEBAR_LINKS = (By.CSS_SELECTOR, "#sidenav a")
    CONTENT_HEADING = (By.CSS_SELECTOR, "#main h1")
    CONTENT_H2 = (By.CSS_SELECTOR, "#main h2")
    SEARCH_CONTAINER = (By.ID, "tnb-google-search-container")
    MAIN_LINKS = (By.CSS_SELECTOR, "#main a")
    FOOTER = (By.ID, "footer")
    Sidenav = (By.ID, "sidenav")
    NAV_HOME = (By.CSS_SELECTOR, "#sidenav a[href='default.asp']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def open_tutorial_page(self):
        self.driver.get(self.TUTORIAL_URL)
        return self

    def get_heading_text(self):
        el = self.find(*self.CONTENT_HEADING)
        return el.text

    def get_h2_texts(self):
        els = self.find_all(*self.CONTENT_H2)
        return [e.text for e in els if e.text.strip()]

    def is_main_present(self):
        return self.is_visible(*self.MAIN)

    def is_sidebar_present(self):
        try:
            self.find(*self.SIDEBAR)
            return True
        except:
            return False

    def is_sidenav_present(self):
        try:
            self.find(*self.Sidenav)
            return True
        except:
            return False

    def get_sidebar_link_count(self):
        try:
            return len(self.find_all(*self.SIDEBAR_LINKS))
        except:
            return 0

    def get_main_link_count(self):
        try:
            return len(self.find_all(*self.MAIN_LINKS))
        except:
            return 0

    def has_search(self):
        try:
            self.find(*self.SEARCH_CONTAINER)
            return True
        except:
            return False

    def has_footer(self):
        try:
            self.find(*self.FOOTER)
            return True
        except:
            return False

    def has_home_link(self):
        try:
            self.find(*self.NAV_HOME)
            return True
        except:
            return False

    def get_page_title(self):
        return self.driver.title
