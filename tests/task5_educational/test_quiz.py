import pytest
import time
from pages.educational.quiz_page import QuizPage


@pytest.mark.educational
class TestQuiz:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = QuizPage(driver)
        self.page.open()

    @pytest.mark.smoke
    def test_quiz_loads(self, driver):
        assert self.page.is_quiz_loaded()

    def test_radio_buttons_present(self, driver):
        count = self.page.get_radio_count()
        assert count > 0

    def test_select_answer(self, driver):
        self.page.select_answer(0)
        val = self.page.get_selected_value()
        assert val is not None

    def test_label_texts(self, driver):
        labels = self.page.get_label_texts()
        assert len(labels) > 0

    def test_submit_advances_quiz(self, driver):
        self.page.select_answer(0)
        self.page.submit_quiz()
        time.sleep(3)
        assert self.page.get_radio_count() > 0 or "=" in self.page.get_current_url()

    def test_multiple_answers_selectable(self, driver):
        radios = self.page.get_radio_count()
        if radios >= 2:
            self.page.select_answer(1)
            val = self.page.get_selected_value()
            assert val is not None
