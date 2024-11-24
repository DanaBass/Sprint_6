from selenium.webdriver.common.by import By


class TransitionPageLocators:

    SCOOTER_IMAGE = By.XPATH, "//img[@alt='Scooter']"# Локатор для кнопки "Самокат".
    YANDEX_IMAGE = By.XPATH, "//img[@alt='Yandex']"# Локатор для кнопки "Яндекс".

    UNIQUE_ELEMENT_SCOOTER = By.XPATH, "//div[@class='Home_Header__iJKdX']"# Локатор для проверки перехода по кнопке "Самокат".
    UNIQUE_ELEMENT_YANDEX = By.XPATH, "//div[@aria-label='Новости на тему']"# Локатор для проверки перехода по кнопке "Яндекс".


