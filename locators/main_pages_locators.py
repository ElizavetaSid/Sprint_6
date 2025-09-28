from selenium.webdriver.common.by import By

class MainPagesLocators:
   
    HEDER_LOGO_SCOOTER = (By.XPATH, "//a[@href='/']")
    HEDER_LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru"]')

    #"Вопросы о важном"
    FAQ_SECTION = (By.XPATH, '//div[contains(@class,"Home_FAQ__")]')

    FAQ_SECTION_ITEM_QUISTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }

    FAQ_SECTION_ITEM_ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }
    COKKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")

    #Заказ
    ORDER_BUTTON_IN_HEDER = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_IN_MAIN = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
    
    #Переход с ЛОГО
    MAIN_HEADER = (By.XPATH, '//div[contains(@class,"Header_Logo__23yGT")]')
    TITLE_DZEN = (By.XPATH, './/span[text() = "Главная"]')