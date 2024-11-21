from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)

        self.scroll_to_element(locator_q_formatted)
        self.click_to_element(locator_q_formatted)

        return self.get_text_from_element(locator_a_formatted)

    # def set_order(self, station_locator, name_locator, name, last_name, address, time, button_locator):
    #     self.click_to_element(station_locator)
    #     self.add_text_to_element(name_locator, name)
    #     self.add_text_to_element(last_name, last_name)
    #     self.add_text_to_element(address, address)
    #     self.click_to_element(time)
    #     self.click_to_element(button_locator)
    #
    # def check_order(self, locator):
    #     return self.get_text_from_element(locator)







