import pytest
from selenium import webdriver
from page_objects.question_page import QuestionPage


class TestQuestionPage:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("expected_answer, index", [
        ("Сутки — 400 рублей. Оплата курьеру — наличными или картой.", 0),  # Ожидаемый ответ и индекс вопросов
        ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.", 1),
        ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.", 2),
        ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.", 3),
        ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.", 4),
        ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.", 5),
        ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.", 6),
        ("Да, обязательно. Всем самокатов! И Москве, и Московской области.", 7),
    ])
    def test_question(self, expected_answer, index):
        question_page = QuestionPage(self.driver)
        question_page.click_question(index)  # Клик по вопросу
        answer_text = question_page.get_answer_text(index)  # Получаем текст ответа
        assert answer_text == expected_answer, f"Ответ для вопроса {index + 1} не совпадает!"

