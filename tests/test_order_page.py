import pytest
import allure

from data.data import OrderForm
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @pytest.mark.parametrize(
        'locator, order_form_data',
        [
            (MainPageLocators.ORDER_HEADER_BUTTON, OrderForm.test_data_sets[1]),
            (MainPageLocators.ORDER_BUTTON_BELOW, OrderForm.test_data_sets[2]),
        ]
    )
    @allure.title("Тестирование создания заказа с локатором {locator}")
    @allure.step("Тестируем создание заказа с локатором {locator}")
    def test_create_order(self, driver, locator, order_form_data: dict):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_to_element(locator)
        order_page.set_order(order_form_data)

        assert "Заказ оформлен" in order_page.check_order(OrderPageLocators.ORDER_MODAL_HEADER)



