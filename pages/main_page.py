import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Получаем текст ответа для вопроса номер: {num}")
    @allure.title("Получение текста ответа для вопроса номер: {num}")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)

        self.scroll_to_element(locator_q_formatted)
        self.click_to_element(locator_q_formatted)

        answer_text = self.get_text_from_element(locator_a_formatted)
        allure.step(f"Получен текст ответа: '{answer_text}'")

        return answer_text










