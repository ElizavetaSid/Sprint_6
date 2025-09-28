import allure
import sys
import os

# Добавляем корень проекта в путь Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page.base_page import BasePage
from locators.order_pages_locators import OrderPagesLocators
from data import *

class OrderPage(BasePage):
    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_input_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPagesLocators.NAME_INPUT)
        self.click_on_element(OrderPagesLocators.NAME_INPUT)
        self.send_keys_to_input(OrderPagesLocators.NAME_INPUT, test_data[0])
        self.click_on_element(OrderPagesLocators.LAST_NAME_INPUT)
        self.send_keys_to_input(OrderPagesLocators.LAST_NAME_INPUT, test_data[1])
        self.click_on_element(OrderPagesLocators.ADRESS_INPUT)
        self.send_keys_to_input(OrderPagesLocators.ADRESS_INPUT, test_data[2])
        self.click_on_element(OrderPagesLocators.METRO_STATION_INPUT)
        self.send_keys_to_input(OrderPagesLocators.METRO_STATION_INPUT, test_data[3])
        self.select_station()
        self.click_on_element(OrderPagesLocators.PHONE_NUMBER)
        self.send_keys_to_input(OrderPagesLocators.PHONE_NUMBER, test_data[4])
        self.click_on_element(OrderPagesLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_input_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPagesLocators.TITLE_PAGE_RENT)
        self.click_on_element(OrderPagesLocators.DATA_INPUT)
        self.send_keys_to_input(OrderPagesLocators.DATA_INPUT, test_data[5])
        self.click_date_in_calendar()
        self.wait_visibility_of_element(OrderPagesLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPagesLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPagesLocators.DROPDOWN_RENTAL_PERIOD)
        self.click_on_element(OrderPagesLocators.CHECKBOX_BLACK_COLOR_SCOOTER)
        self.click_on_element(OrderPagesLocators.COMMENT)
        self.send_keys_to_input(OrderPagesLocators.COMMENT, test_data[6])
        self.click_on_element(OrderPagesLocators.BUTTON_MAKE_ORDER)
        self.wait_visibility_of_element(OrderPagesLocators.CONFIRMATION_ORDER)
        self.click_on_element(OrderPagesLocators.BUTTON_YES)


    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self):
        self.click_on_element(OrderPagesLocators.SELECT_ITEM_METRO_DROP_DOWN)

    @allure.step('Ввести дату заказа в инпут "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self, test_data):
        self.send_keys_to_input(OrderPagesLocators.DATA_INPUT).send_keys(test_data)

    @allure.step('Кликнуть по выбранной дате в выпадающем списке календаря поля ввода даты начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPagesLocators.CALENDAR_ITEM)

    @allure.step('Проверить отображения кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPagesLocators.BUTTON_CHECK_STATUS)


