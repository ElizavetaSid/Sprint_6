import pytest
from selenium.webdriver.common.by import By

class OrderPagesLocators:
    
    TITLE_PAGE_PERSONAL = (By.XPATH, '//div[text()="Для кого самокат" and contains(@class="Order_Header__BZXOb")]')
    
    # "Для кого самокат"
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    SELECT_ITEM_METRO_DROP_DOWN = (By.XPATH, '//div[@class="select-search__select"]')
    PHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]')


    # "Про аренду" 
    TITLE_PAGE_RENT = (By.XPATH, '//div[text()="Про аренду" and contains(@class,"Order_Header")]')
    DATA_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CALENDAR_ICON = (By.XPATH, '//div[@class="react-datepicker-popper"]')
    CALENDAR_ITEM = (By.XPATH, '//div[contains(@class, "react-datepicker") and contains(@tabindex, "-1")]')
    RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    DROPDOWN_RENTAL_PERIOD = (By.XPATH, '//div[@class="Dropdown-menu"]/div[text() ="сутки"]')
    CHECKBOX_BLACK_COLOR_SCOOTER = (By.ID, 'black')
    COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_MAKE_ORDER = (By.XPATH, '//div[contains(@class,"Order_Buttons")]/button[text()="Заказать"]')


    # "Окно подтверждения заказа"
    CONFIRMATION_ORDER = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    BUTTON_YES = (By.XPATH, '//button[text()="Да"]')
    BUTTON_CHECK_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')