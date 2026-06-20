from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EnrollmentPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    COURSE_CATALOG = (By.ID, "course-catalog")
    COURSE_CARDS = (By.CSS_SELECTOR, ".course-card")
    COURSE_NAMES = (By.CSS_SELECTOR, ".course-card .course-name")
    COURSE_DESCRIPTIONS = (By.CSS_SELECTOR, ".course-card .course-desc")
    ENROLL_BTN = (By.CSS_SELECTOR, ".enroll-btn")
    SEARCH_COURSE = (By.ID, "course-search")
    SEARCH_BTN = (By.ID, "search-btn")

    CATEGORY_FILTER = (By.ID, "category-filter")
    DIFFICULTY_FILTER = (By.ID, "difficulty-filter")

    ENROLLED_COURSES = (By.CSS_SELECTOR, ".enrolled-course")
    CONFIRM_ENROLLMENT = (By.ID, "confirm-enroll")
    ENROLLMENT_SUCCESS = (By.CSS_SELECTOR, ".enrollment-success")

    def get_page_title_text(self):
        return self.get_text(*self.PAGE_TITLE)

    def get_course_count(self):
        try:
            return len(self.find_all(*self.COURSE_CARDS))
        except:
            return 0

    def get_course_names(self):
        elements = self.find_all(*self.COURSE_NAMES)
        return [el.text for el in elements]

    def search_course(self, query):
        self.type_text(*self.SEARCH_COURSE, query)
        self.click(*self.SEARCH_BTN)
        return self

    def enroll_in_course(self, index=0):
        btns = self.find_all(*self.ENROLL_BTN)
        btns[index].click()
        return self

    def confirm_enrollment(self):
        self.click(*self.CONFIRM_ENROLLMENT)
        return self

    def is_enrollment_successful(self):
        return self.is_visible(*self.ENROLLMENT_SUCCESS)

    def get_enrolled_count(self):
        try:
            return len(self.find_all(*self.ENROLLED_COURSES))
        except:
            return 0

    def get_course_descriptions(self):
        elements = self.find_all(*self.COURSE_DESCRIPTIONS)
        return [el.text for el in elements]
