import pytest
from pages.educational.enrollment_page import EnrollmentPage


@pytest.mark.educational
class TestEnrollment:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = EnrollmentPage(driver)
        self.page.open()

    @pytest.mark.smoke
    def test_page_loads(self, driver):
        assert self.page.is_main_present()

    def test_sidebar_on_tutorial(self, driver):
        self.page.open_tutorial_page()
        assert self.page.is_sidebar_present()

    def test_sidebar_link_count(self, driver):
        self.page.open_tutorial_page()
        count = self.page.get_sidebar_link_count()
        assert count > 10

    def test_tutorial_heading(self, driver):
        self.page.open_tutorial_page()
        heading = self.page.get_heading_text()
        assert heading is not None and len(heading) > 0

    def test_tutorial_h2_sections(self, driver):
        self.page.open_tutorial_page()
        sections = self.page.get_h2_texts()
        assert len(sections) > 0

    def test_main_links(self, driver):
        count = self.page.get_main_link_count()
        assert count > 0

    def test_search_present(self, driver):
        assert self.page.has_search()

    def test_footer_present(self, driver):
        assert self.page.has_footer()

    def test_page_title(self, driver):
        title = self.page.get_page_title()
        assert title is not None and len(title) > 0

    def test_sidenav_present(self, driver):
        self.page.open_tutorial_page()
        assert self.page.is_sidenav_present()

    def test_home_link_in_sidebar(self, driver):
        self.page.open_tutorial_page()
        assert self.page.has_home_link()
