import pytest
import allure
import sys
import os

# Добавляем корень проекта в путь Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page.order_page import OrderPage
from data import TestData
from locators.main_pages_locators import MainPagesLocators

class TestOrderPageOrder:

    @allure.title('Проверка позитивного сценария оформления заказа')
    @pytest.mark.parametrize('button, test_data', [(MainPagesLocators.ORDER_BUTTON_IN_HEDER, TestData.test_data_user1),
                                                    (MainPagesLocators.ORDER_BUTTON_IN_MAIN, TestData.test_data_user2)])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element_with_wait(button)
        order_page.data_input_first_form(test_data)
        order_page.data_input_second_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()