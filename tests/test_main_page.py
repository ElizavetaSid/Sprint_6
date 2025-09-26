import allure
import pytest
import sys
import os

# Добавляем корень проекта в путь Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.main_page import MainPageFAQ
from data import TestData

class TestMainPageFAQ():

    @allure.title("Проверка раздела 'Вопросы о важном'")
    @pytest.mark.parametrize('question_namber, expected_answer', TestData.test_data_faq_answer)
    def test_click_to_question_and_get_answer(self, driver, question_namber, expected_answer):
        main_page = MainPageFAQ(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_namber)
        main_page.click_on_faq_item(question_namber)
        main_page.wait_visibility_of_faq_answers(question_namber)
        assert main_page.get_displayed_text_from_faq_answers(question_namber) == expected_answer
