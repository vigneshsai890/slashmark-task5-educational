from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QuizPage(BasePage):
    QUIZ_CONTAINER = (By.ID, "quiz-container")
    QUESTION_TEXT = (By.CSS_SELECTOR, ".question-text")
    ANSWER_OPTIONS = (By.CSS_SELECTOR, ".answer-option")
    ANSWER_RADIO = (By.CSS_SELECTOR, ".answer-option input[type='radio']")
    SUBMIT_QUIZ_BTN = (By.ID, "submit-quiz")
    NEXT_QUESTION_BTN = (By.ID, "next-question")
    PREV_QUESTION_BTN = (By.ID, "prev-question")
    QUIZ_TIMER = (By.CSS_SELECTOR, ".quiz-timer")
    QUESTION_COUNTER = (By.CSS_SELECTOR, ".question-counter")

    SCORE_DISPLAY = (By.CSS_SELECTOR, ".quiz-score")
    FEEDBACK = (By.CSS_SELECTOR, ".quiz-feedback")
    RETAKE_BTN = (By.ID, "retake-quiz")

    def is_quiz_loaded(self):
        return self.is_visible(*self.QUIZ_CONTAINER, timeout=10)

    def get_question_text(self):
        return self.get_text(*self.QUESTION_TEXT)

    def get_answer_count(self):
        return len(self.find_all(*self.ANSWER_OPTIONS))

    def select_answer(self, index):
        options = self.find_all(*self.ANSWER_RADIO)
        options[index].click()
        return self

    def submit_quiz(self):
        self.click(*self.SUBMIT_QUIZ_BTN)
        return self

    def next_question(self):
        self.click(*self.NEXT_QUESTION_BTN)
        return self

    def prev_question(self):
        self.click(*self.PREV_QUESTION_BTN)
        return self

    def get_score(self):
        return self.get_text(*self.SCORE_DISPLAY)

    def get_feedback(self):
        return self.get_text(*self.FEEDBACK)

    def retake_quiz(self):
        self.click(*self.RETAKE_BTN)
        return self

    def get_question_counter(self):
        return self.get_text(*self.QUESTION_COUNTER)

    def get_timer_text(self):
        return self.get_text(*self.QUIZ_TIMER)
