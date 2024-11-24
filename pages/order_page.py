import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Устанавливаем заказ с данными: {order_form_data}")
    @allure.title("Настройка заказа с указанными данными")
    def set_order(self, order_form_data: dict):
        self.fill_user_data_form(order_form_data)
        self.fill_rent_data_form(order_form_data)

    @allure.step("Заполняем форму данных пользователя")
    @allure.title("Заполнение формы данных пользователя")
    def fill_user_data_form(self, order_form_data: dict):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, order_form_data["name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT, order_form_data["last_name"])
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, order_form_data["address"])

        self.add_text_to_element(OrderPageLocators.STATION_INPUT_TEXT, order_form_data["station"])

        self.click_to_element(OrderPageLocators.get_station_input_click(order_form_data["station"]))

        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, order_form_data["phone"])

        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполняем форму данных аренды")
    @allure.title("Заполнение формы данных аренды")
    def fill_rent_data_form(self, order_form_data: dict):
        self.add_text_to_element(OrderPageLocators.TIME_INPUT, order_form_data["time"])

        self.click_to_element(OrderPageLocators.RENT_INPUT_CLICK)
        self.click_to_element(OrderPageLocators.get_rental_period_selection(order_form_data["rental_period"]))

        self.click_to_element(OrderPageLocators.get_scooter_color_selection(order_form_data["scooter_color"]))
        self.add_text_to_element(OrderPageLocators.COMMENT_COURIER, order_form_data["comment"])

        self.click_to_element(OrderPageLocators.FINAL_ORDER_BUTTON)

        self.click_to_element(OrderPageLocators.ORDER_CONFIRMATION)

    @allure.step("Проверяем заказ по локатору: {locator}")
    @allure.title("Проверка заказа")
    def check_order(self, locator):
        return self.get_text_from_element(locator)




