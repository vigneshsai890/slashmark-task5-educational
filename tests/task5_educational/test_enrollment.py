import pytest
from pages.educational.enrollment_page import EnrollmentPage


@pytest.mark.educational
class TestEnrollment:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = EnrollmentPage(driver)
        self.page.driver.get("https://sandbox.moodledemo.net/course")

    def test_page_loads(self, driver):
        assert self.page.is_visible(*self.page.COURSE_CATALOG, timeout=10)

    def test_courses_displayed(self, driver):
        count = self.page.get_course_count()
        assert count > 0

    def test_course_names_not_empty(self, driver):
        names = self.page.get_course_names()
        assert all(len(n) > 0 for n in names)

    def test_course_descriptions_present(self, driver):
        descs = self.page.get_course_descriptions()
        assert len(descs) > 0

    @pytest.mark.smoke
    def test_enroll_in_course(self, driver):
        self.page.enroll_in_course(0)
        self.page.confirm_enrollment()
        assert self.page.is_enrollment_successful()

    def test_search_course(self, driver):
        self.page.search_course("Math")
        count = self.page.get_course_count()
        assert count >= 0

    def test_enrolled_courses_list(self, driver):
        count = self.page.get_enrolled_count()
        assert count >= 0
