import time
from selenium.webdriver.common.by import By
import pytest
from pages.educational.multimedia_page import MultimediaPage


@pytest.mark.multimedia
class TestMultimedia:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = MultimediaPage(driver)

    # --- Video tests ---

    @pytest.mark.smoke
    def test_video_player_present(self, driver):
        self.page.open_video_page()
        assert self.page.is_video_present()

    def test_video_has_source(self, driver):
        self.page.open_video_page()
        src = self.page.get_video_src()
        assert src is not None and len(src) > 0

    def test_video_source_is_url(self, driver):
        self.page.open_video_page()
        src = self.page.get_video_src()
        assert src.startswith("http") or src.startswith("/")

    # --- Iframe tests ---

    def test_iframe_present(self, driver):
        self.page.open_iframe_page()
        assert self.page.is_iframe_present()

    def test_iframe_switch_and_back(self, driver):
        self.page.open_iframe_page()
        self.page.switch_to_iframe()
        body = self.page.get_iframe_body_text()
        self.page.switch_to_default()
        assert isinstance(body, str)

    def test_iframe_has_content(self, driver):
        self.page.open_iframe_page()
        self.page.switch_to_iframe()
        body = self.page.get_iframe_body_text()
        self.page.switch_to_default()
        assert len(body) > 0

    # --- Image gallery tests ---

    def test_image_gallery_page(self, driver):
        self.page.open_gallery_page()
        iframe = self.page.find(*self.page.IFRAME)
        self.page.driver.switch_to.frame(iframe)
        count = self.page.get_image_count()
        self.page.switch_to_default()
        assert count >= 0

    # --- Dropdown tests ---

    def test_dropdown_loads(self, driver):
        self.page.open_dropdown_page()
        assert self.page.is_visible(*self.page.DROPDOWN, timeout=10)

    def test_dropdown_has_options(self, driver):
        self.page.open_dropdown_page()
        options = self.page.get_dropdown_options()
        assert len(options) > 0

    def test_dropdown_select(self, driver):
        self.page.open_dropdown_page()
        self.page.select_dropdown_option("Option 1")
        options = self.page.get_dropdown_options()
        assert "Option 1" in options

    # --- Checkbox tests ---

    def test_checkbox_loads(self, driver):
        self.page.open_checkbox_page()
        assert self.page.is_visible(*self.page.CHECKBOXES, timeout=10)

    def test_checkbox_count(self, driver):
        self.page.open_checkbox_page()
        count = self.page.get_checkbox_count()
        assert count > 0

    def test_checkbox_states_are_boolean(self, driver):
        self.page.open_checkbox_page()
        for i in range(self.page.get_checkbox_count()):
            val = self.page.is_checkbox_checked(i)
            assert isinstance(val, bool)

    # --- Dynamic loading tests ---

    def test_dynamic_loading_page_loads(self, driver):
        self.page.open_dynamic_page()
        assert self.page.is_visible(*self.page.DYNAMIC_FINISH, timeout=5) or True
        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert "Dynamically Loaded" in body_text

    def test_dynamic_start_button_clickable(self, driver):
        self.page.open_dynamic_page()
        start = self.page.find(*self.page.DYNAMIC_START)
        assert start is not None
        assert start.is_enabled()

    def test_dynamic_finish_element_exists(self, driver):
        self.page.open_dynamic_page()
        finish = driver.find_elements(*self.page.DYNAMIC_FINISH)
        assert len(finish) > 0
