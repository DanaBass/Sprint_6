import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class TransitionPage(BasePage):

    @allure.step("Открываем страницу заказа")
    @allure.title("Переход на страницу заказа")
    def open_order_page(self):
        self.click_to_element(MainPageLocators.ORDER_HEADER_BUTTON)






