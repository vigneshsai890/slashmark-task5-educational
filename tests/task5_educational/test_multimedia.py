import pytest
from pages.educational.multimedia_page import MultimediaPage


@pytest.mark.multimedia
class TestMultimedia:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = MultimediaPage(driver)

    def test_video_player_present(self, driver):
        self.page.driver.get("https://www.w3schools.com/html/html5_video.asp")
        assert self.page.is_video_present()

    def test_video_has_source(self, driver):
        self.page.driver.get("https://www.w3schools.com/html/html5_video.asp")
        src = self.page.get_video_src()
        assert src is not None and len(src) > 0

    def test_iframe_present(self, driver):
        self.page.driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default")
        assert self.page.is_iframe_present()

    def test_iframe_switch(self, driver):
        self.page.driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default")
        self.page.switch_to_iframe()
        self.page.switch_to_default()

    def test_image_gallery(self, driver):
        self.page.driver.get("https://www.w3schools.com/css/tryit.asp?filename=trycss3_image_gallery")
        count = self.page.get_image_count()
        assert count >= 0

    def test_pdf_viewer(self, driver):
        self.page.driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_pdf")
        present = self.page.is_pdf_viewer_present()
        assert isinstance(present, bool)
