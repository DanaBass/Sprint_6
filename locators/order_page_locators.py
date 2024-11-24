from selenium.webdriver.common.by import By


class OrderPageLocators:
    STATION_INPUT_TEXT = By.XPATH, '//input[@placeholder="* Станция метро" and @value=""]'# Локатор для поля ввода станции метро.
    NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]'# Локатор для поля ввода имени пользователя.
    LAST_NAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]'# Локатор для поля ввода фамилии пользователя.
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'# Локатор для поля ввода адреса, куда должен быть доставлен заказ.
    PHONE_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]' # Локатор для поля ввода номера телефона, на который позвонит курьер.

    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    TIME_INPUT = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]' # Локатор для поля ввода даты, когда пользователь хочет получить самокат.
    RENT_INPUT_CLICK = By.XPATH, "//span[@class='Dropdown-arrow']"# Локатор для кнопки раскрытия выпадающего списка срока аренды.
    RENTAL_PERIOD = By.XPATH, '//div[text()="* Срок аренды"]'# Локатор для надписи "* Срок аренды", используемой для проверки наличия поля.
    COMMENT_COURIER = By.XPATH, "//input[@placeholder='Комментарий для курьера']"# Локатор для поля ввода комментария.


    FINAL_ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"# Локатор для оформления заказа.
    ORDER_CONFIRMATION = By.XPATH, "//button[text()='Да']" # Подтверждение заказа.
    ORDER_MODAL_HEADER = By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]"# Локатор для заголовка модального окна с подтверждением заказа.

    @staticmethod
    def get_station_input_click(station_name):
        # Возвращает локатор для элемента выбора станции, основанный на переданном имени станции.
        return By.XPATH, f'//li[@class="select-search__row" and .//div[contains(text(), "{station_name}")]]/button'

    @staticmethod
    def get_rental_period_selection(rental_period):
        # Возвращает локатор для элемента выбора срока аренды, основанный на переданном значении.
        return By.XPATH, f'//div[@class="Dropdown-option" and text()="{rental_period}"]'

    @staticmethod
    def get_scooter_color_selection(color):
        # Возвращает локатор для выбора цвета самоката, основанный на переданном названии цвета.
        return By.XPATH, f"//input[@id='{color}']"