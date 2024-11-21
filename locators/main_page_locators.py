from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.ID, "accordion__heading-7"

