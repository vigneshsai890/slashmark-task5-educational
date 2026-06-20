import pytest
from pages.educational.progress_page import ProgressPage


@pytest.mark.educational
class TestProgressTracking:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = ProgressPage(driver)
        self.page.open()

    @pytest.mark.smoke
    def test_page_loads(self, driver):
        assert self.page.is_progress_present()

    def test_progress_has_value(self, driver):
        val = self.page.get_progress_value()
        assert val is not None

    def test_progress_has_max(self, driver):
        mx = self.page.get_progress_max()
        assert mx is not None

    def test_progress_percentage(self, driver):
        pct = self.page.get_progress_percentage()
        assert 0 < pct <= 100

    def test_progress_value_is_numeric(self, driver):
        val = self.page.get_progress_value()
        assert val.isdigit()

    def test_progress_max_is_100(self, driver):
        mx = self.page.get_progress_max()
        assert mx == "100"
