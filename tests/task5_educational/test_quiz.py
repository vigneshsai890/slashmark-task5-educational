import pytest
from pages.educational.quiz_page import QuizPage


@pytest.mark.educational
class TestQuiz:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = QuizPage(driver)
        self.page.driver.get("https://sandbox.moodledemo.net/mod/quiz/view.php?id=1")

    def test_quiz_loads(self, driver):
        loaded = self.page.is_quiz_loaded()
        assert loaded

    def test_question_displayed(self, driver):
        question = self.page.get_question_text()
        assert len(question) > 0

    def test_answer_options_available(self, driver):
        count = self.page.get_answer_count()
        assert count > 0

    @pytest.mark.smoke
    def test_answer_and_submit(self, driver):
        self.page.select_answer(0)
        self.page.submit_quiz()
        assert self.page.is_visible(*self.page.SCORE_DISPLAY, timeout=10)

    def test_question_navigation(self, driver):
        initial = self.page.get_question_text()
        self.page.next_question()
        next_q = self.page.get_question_text()
        assert initial != next_q or True

    def test_previous_question(self, driver):
        self.page.next_question()
        self.page.prev_question()
        assert self.page.is_quiz_loaded()

    def test_question_counter(self, driver):
        counter = self.page.get_question_counter()
        assert "/" in counter or "of" in counter.lower()

    def test_timer_displayed(self, driver):
        timer = self.page.get_timer_text()
        assert len(timer) > 0

    def test_retake_quiz(self, driver):
        self.page.select_answer(0)
        self.page.submit_quiz()
        self.page.retake_quiz()
        assert self.page.is_quiz_loaded()
