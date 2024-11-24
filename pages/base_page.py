from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Находим элемент по локатору: {locator}")
    @allure.title("Поиск элемента по локатору")
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликаем на элемент по локатору: {locator}")
    @allure.title("Клик по элементу")
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)


    @allure.step("Переключаемся на последнюю открытую страницу")
    @allure.title("Переключение на последнюю открытую страницу")
    def switch_to_last_page(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

    @allure.step("Добавляем текст '{text}' в элемент по локатору: {locator}")
    @allure.title("Добавление текста в элемент")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получаем текст из элемента по локатору: {locator}")
    @allure.title("Получение текста из элемента")
    def get_text_from_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    @staticmethod
    @allure.step("Форматируем локатор: {locator} с номером: {num}")
    @allure.title("Форматирование локатора")
    def format_locators(locator, num):
        method, locator = locator
        locator = locator.format(num)

        return method, locator

    @allure.step("Прокручиваем до элемента по локатору: {locator}")
    @allure.title("Прокрутка до элемента")
    def scroll_to_element(self, locator):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

            self.driver.execute_script("arguments[0].scrollIntoView();", element)




