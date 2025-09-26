import pytest
import allure
import sys
import os

# Добавляем корень проекта в путь Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.main_page import MainPageFAQ

class TestLogo:

    @allure.title('Проверка перехода на главную страницу при клике на логотип "Самокат"')
    def test_logo_main_page(self, driver):
        main_page = MainPageFAQ(driver)
        main_page.wait_visibility_of_order_button_in_heder()
        main_page.click_on_button_in_heder()
        main_page.wait_visibility_of_heder_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_dzen(self, driver):
        main_page = MainPageFAQ(driver)
        main_page.wait_visibility_of_heder_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()