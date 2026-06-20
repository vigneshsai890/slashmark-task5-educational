from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MultimediaPage(BasePage):
    VIDEO_PLAYER = (By.CSS_SELECTOR, "video")
    VIDEO_SOURCE = (By.CSS_SELECTOR, "video source")
    PLAY_BTN = (By.CSS_SELECTOR, ".play-btn")
    PAUSE_BTN = (By.CSS_SELECTOR, ".pause-btn")
    PROGRESS_BAR = (By.CSS_SELECTOR, "video")
    VOLUME_SLIDER = (By.CSS_SELECTOR, ".volume-slider")

    IFRAME_CONTAINER = (By.ID, "iframe-container")
    IFRAME = (By.TAG_NAME, "iframe")

    PDF_VIEWER = (By.ID, "pdf-viewer")
    PDF_CANVAS = (By.CSS_SELECTOR, "#pdf-viewer canvas")

    IMAGE_GALLERY = (By.CSS_SELECTOR, ".gallery-item")
    IMAGE_LIGHTBOX = (By.CSS_SELECTOR, ".lightbox-overlay")
    LIGHTBOX_CLOSE = (By.CSS_SELECTOR, ".lightbox-close")
    NEXT_IMAGE = (By.CSS_SELECTOR, ".next-image")
    PREV_IMAGE = (By.CSS_SELECTOR, ".prev-image")

    def is_video_present(self):
        return self.is_visible(*self.VIDEO_PLAYER, timeout=10)

    def play_video(self):
        self.click(*self.PLAY_BTN)
        return self

    def pause_video(self):
        self.click(*self.PAUSE_BTN)
        return self

    def get_video_src(self):
        element = self.find(*self.VIDEO_SOURCE)
        return element.get_attribute("src")

    def switch_to_iframe(self):
        iframe = self.find(*self.IFRAME)
        self.driver.switch_to.frame(iframe)
        return self

    def switch_to_default(self):
        self.driver.switch_to.default_content()
        return self

    def is_iframe_present(self):
        return self.is_visible(*self.IFRAME, timeout=10)

    def is_pdf_viewer_present(self):
        return self.is_visible(*self.PDF_VIEWER, timeout=10)

    def get_image_count(self):
        try:
            return len(self.find_all(*self.IMAGE_GALLERY))
        except:
            return 0

    def open_lightbox(self, index=0):
        items = self.find_all(*self.IMAGE_GALLERY)
        items[index].click()
        return self

    def is_lightbox_open(self):
        return self.is_visible(*self.IMAGE_LIGHTBOX)

    def close_lightbox(self):
        self.click(*self.LIGHTBOX_CLOSE)
        return self

    def next_image(self):
        self.click(*self.NEXT_IMAGE)
        return self

    def prev_image(self):
        self.click(*self.PREV_IMAGE)
        return self
