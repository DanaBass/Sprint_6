from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'# Общий локатор для нажатия на вопрос.
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'# Общий локатор для ответа.
    QUESTION_LOCATOR_TO_SCROLL = By.ID, "accordion__heading-7"# Локатор до последнего вопроса для скроллинга.

    ORDER_HEADER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g" and text()="Заказать"]'# Локатор для кнопки "Заказать" в шапке профиля.
    ORDER_BUTTON_BELOW = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'# Локатор для кнопки "Заказать" внизу страницы.

