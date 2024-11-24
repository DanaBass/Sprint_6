import pytest
import allure

from data.data import ExpectedResults
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize("num", [
        x for x in ExpectedResults.results.keys()
    ])
    @allure.step("Тестируем вопрос номер: {num}")
    def test_questions_and_answers(self, driver, num):
        main_page = MainPage(driver)

        expected_result = ExpectedResults.results[num]

        assert main_page.get_answer_text(num) == expected_result
