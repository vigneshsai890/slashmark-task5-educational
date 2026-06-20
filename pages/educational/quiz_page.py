from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QuizPage(BasePage):
    URL = "https://www.w3schools.com/quiztest/quiztest.asp?qtest=HTML"

    QUIZ_FORM = (By.CSS_SELECTOR, "form")
    RADIO_BUTTONS = (By.CSS_SELECTOR, "input[type='radio']")
    SUBMIT_BUTTONS = (By.CSS_SELECTOR, "button[type='submit']")
    QUESTION_HEADER = (By.CSS_SELECTOR, "form h2")
    LABELS = (By.CSS_SELECTOR, "label")

    def open(self):
        self.driver.get(self.URL)
        self._remove_overlays()
        return self

    def _remove_overlays(self):
        self.driver.execute_script("""
            document.querySelectorAll('iframe[title="blank"]').forEach(f => f.remove());
            document.querySelectorAll('[data-hbdbrk]').forEach(e => e.remove());
            document.querySelectorAll('[data-actirise]').forEach(e => e.remove());
            document.querySelectorAll('div[style*="position: fixed"]').forEach(e => {
                var z = parseInt(e.style.zIndex) || 0;
                if (z > 100) e.remove();
            });
        """)

    def is_quiz_loaded(self):
        return self.is_visible(*self.QUIZ_FORM, timeout=10)

    def get_radio_count(self):
        try:
            return len(self.find_all(*self.RADIO_BUTTONS))
        except:
            return 0

    def select_answer(self, index=0):
        radios = self.find_all(*self.RADIO_BUTTONS)
        if index < len(radios):
            self.driver.execute_script("arguments[0].click();", radios[index])
        return self

    def get_selected_value(self):
        return self.driver.execute_script(
            "var r = document.querySelector('input[type=radio]:checked'); return r ? r.value : null;"
        )

    def submit_quiz(self):
        buttons = self.find_all(*self.SUBMIT_BUTTONS)
        if buttons:
            self.driver.execute_script("arguments[0].click();", buttons[0])
        return self

    def get_label_texts(self):
        labels = self.find_all(*self.LABELS)
        return [l.text for l in labels if l.text.strip()]

    def get_current_url(self):
        return self.driver.current_url

    def has_submitted(self):
        url = self.driver.current_url
        return "=" in url.split("?")[-1] if "?" in url else False
