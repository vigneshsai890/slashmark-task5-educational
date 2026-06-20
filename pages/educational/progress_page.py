from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProgressPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    PROGRESS_BARS = (By.CSS_SELECTOR, ".progress-bar")
    PROGRESS_LABELS = (By.CSS_SELECTOR, ".progress-label")
    PROGRESS_PERCENTAGES = (By.CSS_SELECTOR, ".progress-percentage")

    COURSE_LIST = (By.CSS_SELECTOR, ".course-progress-item")
    COURSE_NAMES = (By.CSS_SELECTOR, ".course-progress-item .course-name")
    COMPLETION_STATUS = (By.CSS_SELECTOR, ".completion-status")
    COMPLETION_BADGE = (By.CSS_SELECTOR, ".completion-badge")

    CERTIFICATE_BTN = (By.ID, "download-certificate")
    ACTIVITY_LOG = (By.CSS_SELECTOR, ".activity-log-entry")

    def get_page_title_text(self):
        return self.get_text(*self.PAGE_TITLE)

    def get_progress_count(self):
        try:
            return len(self.find_all(*self.PROGRESS_BARS))
        except:
            return 0

    def get_progress_percentages(self):
        elements = self.find_all(*self.PROGRESS_PERCENTAGES)
        return [el.text for el in elements]

    def get_course_names(self):
        elements = self.find_all(*self.COURSE_NAMES)
        return [el.text for el in elements]

    def is_course_completed(self, index):
        statuses = self.find_all(*self.COMPLETION_STATUS)
        return "completed" in statuses[index].text.lower()

    def has_certificate(self):
        return self.is_visible(*self.CERTIFICATE_BTN)

    def download_certificate(self):
        self.click(*self.CERTIFICATE_BTN)

    def get_activity_count(self):
        try:
            return len(self.find_all(*self.ACTIVITY_LOG))
        except:
            return 0

    def get_completion_badges(self):
        elements = self.find_all(*self.COMPLETION_BADGE)
        return [el.text for el in elements]
