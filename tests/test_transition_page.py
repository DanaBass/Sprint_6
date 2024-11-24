import pytest
import locators.transition_page_locators
import allure

from pages.transition_page import TransitionPage


class TestTransitionPage:
    @pytest.mark.parametrize(
        'image_locator, text_locator, expected_text',
        [
            (locators.transition_page_locators.TransitionPageLocators.SCOOTER_IMAGE, locators.transition_page_locators.TransitionPageLocators.UNIQUE_ELEMENT_SCOOTER, 'на пару дней'),
            (locators.transition_page_locators.TransitionPageLocators.YANDEX_IMAGE, locators.transition_page_locators.TransitionPageLocators.UNIQUE_ELEMENT_YANDEX, 'Главное'),
        ]
    )
    @allure.title("Тестирование перехода с изображением: {image_locator}")
    @allure.step("Тестируем переход с изображением: {image_locator}")
    def test_transition(self, driver, image_locator, text_locator, expected_text):
        transition_page = TransitionPage(driver)
        transition_page.open_order_page()

        transition_page.click_to_element(image_locator)

        transition_page.switch_to_last_page()

        text_from_page = transition_page.get_text_from_element(text_locator)

        assert expected_text in text_from_page
