import allure
import sys
import os

# Добавляем корень проекта в путь Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page.base_page import BasePage
from locators.main_pages_locators import MainPagesLocators

class MainPageFAQ(BasePage):

    @allure.step('Проскролить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPagesLocators.FAQ_SECTION)

    @allure.step('Подождать загрузки нужного номера вопроса в аккордеоне "Вопросы о важном"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPagesLocators.FAQ_SECTION_ITEM_QUISTIONS[data])

    @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важном"')
    def click_on_faq_item(self, data):
        self.click_on_element(MainPagesLocators.FAQ_SECTION_ITEM_QUISTIONS[data])

    @allure.step('Подождать загрузки нужного номера ответа в аккордеоне "Вопросы о важном"')
    def wait_visibility_of_faq_answers(self, data):
        self.wait_visibility_of_element(MainPagesLocators.FAQ_SECTION_ITEM_ANSWERS[data])

    @allure.step('Получить текст нужного номера ответа в аккордеоне "Вопросы о важном"')
    def get_displayed_text_from_faq_answers(self, data):
        return self.get_text_on_element(MainPagesLocators.FAQ_SECTION_ITEM_ANSWERS[data])
    
    @allure.step('Проскролить до кнопки "Заказать" в середине')
    def scroll_to_button_main(self):
        self.scroll_to_element(MainPagesLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Подождать загрузки кнопки "Заказать" в середине')
    def wait_visibility_of_order_button_in_main(self):
        self.wait_visibility_of_element(MainPagesLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Кликнуть по кнопке "Заказать" в середине странице')
    def click_on_button_in_main(self):
        self.click_on_element(MainPagesLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Подождать загрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_heder(self):
        self.wait_visibility_of_element(MainPagesLocators.ORDER_BUTTON_IN_HEDER)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_button_in_heder(self):
        self.click_on_element(MainPagesLocators.ORDER_BUTTON_IN_HEDER)

    @allure.step('Подождать загрузки части лого с надписью "Самокат" в хэдере')
    def wait_visibility_of_heder_logo_scooter(self):
        self.wait_visibility_of_element(MainPagesLocators.HEDER_LOGO_SCOOTER)

    @allure.step('Подождать загрузки части лого с надписью "Яндекс" в хэдере')
    def wait_visibility_of_heder_logo_yandex(self):
        self.wait_visibility_of_element(MainPagesLocators.HEDER_LOGO_YANDEX)

    @allure.step('Кликнуть по лого с надписью "Самокат" в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPagesLocators.HEDER_LOGO_SCOOTER)

    @allure.step('Кликнуть по лого с надписью "Яндекс" в хэдере')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPagesLocators.HEDER_LOGO_YANDEX)

    @allure.step('Подождать загрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPagesLocators.MAIN_HEADER)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPagesLocators.MAIN_HEADER)