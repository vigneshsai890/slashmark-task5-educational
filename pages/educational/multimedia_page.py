from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MultimediaPage(BasePage):
    VIDEO_URL = "https://www.w3schools.com/html/html5_video.asp"
    IFRAME_URL = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default"
    GALLERY_URL = "https://www.w3schools.com/css/tryit.asp?filename=trycss_image_gallery"
    DROPDOWN_URL = "https://the-internet.herokuapp.com/dropdown"
    CHECKBOX_URL = "https://the-internet.herokuapp.com/checkboxes"
    DYNAMIC_URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    VIDEO_PLAYER = (By.CSS_SELECTOR, "video")
    VIDEO_SOURCE = (By.CSS_SELECTOR, "video source")
    IFRAME = (By.ID, "iframeResult")
    GALLERY_IMAGES = (By.CSS_SELECTOR, ".gallery img, .w3-col img, #main img")
    DROPDOWN = (By.ID, "dropdown")
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")
    DYNAMIC_START = (By.ID, "start")
    DYNAMIC_FINISH = (By.ID, "finish")

    def open_video_page(self):
        self.driver.get(self.VIDEO_URL)
        return self

    def open_iframe_page(self):
        self.driver.get(self.IFRAME_URL)
        return self

    def open_gallery_page(self):
        self.driver.get(self.GALLERY_URL)
        return self

    def open_dropdown_page(self):
        self.driver.get(self.DROPDOWN_URL)
        return self

    def open_checkbox_page(self):
        self.driver.get(self.CHECKBOX_URL)
        return self

    def open_dynamic_page(self):
        self.driver.get(self.DYNAMIC_URL)
        return self

    def is_video_present(self):
        return self.is_visible(*self.VIDEO_PLAYER, timeout=10)

    def get_video_src(self):
        try:
            el = self.find(*self.VIDEO_SOURCE)
            return el.get_attribute("src")
        except:
            return None

    def switch_to_iframe(self):
        iframe = self.find(*self.IFRAME)
        self.driver.switch_to.frame(iframe)
        return self

    def switch_to_default(self):
        self.driver.switch_to.default_content()
        return self

    def is_iframe_present(self):
        return self.is_visible(*self.IFRAME, timeout=10)

    def get_iframe_body_text(self):
        try:
            return self.driver.find_element(By.TAG_NAME, "body").text
        except:
            return ""

    def get_image_count(self):
        try:
            self.driver.switch_to.default_content()
        except:
            pass
        try:
            images = self.find_all(*self.GALLERY_IMAGES)
            return len(images)
        except:
            return 0

    def select_dropdown_option(self, value):
        from selenium.webdriver.support.ui import Select
        dropdown = self.find(*self.DROPDOWN)
        sel = Select(dropdown)
        sel.select_by_visible_text(value)
        return self

    def get_dropdown_options(self):
        from selenium.webdriver.support.ui import Select
        dropdown = self.find(*self.DROPDOWN)
        sel = Select(dropdown)
        return [opt.text for opt in sel.options]

    def get_checkbox_count(self):
        try:
            return len(self.find_all(*self.CHECKBOXES))
        except:
            return 0

    def is_checkbox_checked(self, index):
        try:
            checkboxes = self.find_all(*self.CHECKBOXES)
            return checkboxes[index].is_selected()
        except:
            return False

    def start_dynamic_loading(self):
        self.click(*self.DYNAMIC_START)
        return self

    def is_dynamic_complete(self, timeout=10):
        return self.is_visible(*self.DYNAMIC_FINISH, timeout=timeout)

    def get_dynamic_finish_text(self):
        return self.get_text(*self.DYNAMIC_FINISH)
