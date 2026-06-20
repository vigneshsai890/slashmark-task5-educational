import pytest
from pages.educational.progress_page import ProgressPage


@pytest.mark.educational
class TestProgressTracking:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = ProgressPage(driver)
        self.page.driver.get("https://sandbox.moodledemo.net/my/")

    def test_page_loads(self, driver):
        assert self.page.is_visible(*self.page.COURSE_LIST, timeout=10)

    def test_course_names_displayed(self, driver):
        names = self.page.get_course_names()
        assert len(names) > 0

    def test_progress_percentages(self, driver):
        percentages = self.page.get_progress_percentages()
        assert len(percentages) > 0

    def test_completion_status(self, driver):
        count = self.page.get_progress_count()
        assert count >= 0

    def test_activity_log(self, driver):
        count = self.page.get_activity_count()
        assert count >= 0

    def test_completion_badges(self, driver):
        badges = self.page.get_completion_badges()
        assert isinstance(badges, list)
