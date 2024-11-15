
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class QuestionPage:

    def __init__(self, driver):
        self.driver = driver

    def click_question(self, question_index):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Прокрутить страницу вниз.
        question_arrows = self.driver.find_elements(By.CSS_SELECTOR, ".accordion__button") # Получить все стрелочки по общему локатору.
        question_arrows[question_index].click() # Клик по стрелочке с заданным индксом.

    def get_answer_text(self, question_index):
        answer_locator = f".accordion__item:nth-of-type({question_index + 1}) p"  # Локатор ответа
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, answer_locator))) # Ожидайте, пока элемент будет доступен, и виден
            return self.driver.find_element(By.CSS_SELECTOR, answer_locator).text
        except TimeoutException:
            print(f"Ответ по индексу {question_index} не доступен.")
            return None








