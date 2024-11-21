import pytest
from pages.main_page import MainPage
from data import ExpectedResults


class TestMainPage:

    @pytest.mark.parametrize("num", [
        0, 1, 2, 3, 4, 5, 6, 7,
    ])
    def test_questions_and_answers(self, driver, num):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")

        expected_result = ExpectedResults.results[num]

        assert main_page.get_answer_text(num) == expected_result
