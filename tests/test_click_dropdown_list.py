import pytest
from selenium import webdriver
from constants import Constants
from pages.home_page import HomePage


class TestDropDownList:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('element,info', Constants.info_dropdown_list)
    def test_click_drop_down_list(self, element, info):
        homePage = HomePage(self.driver, Constants.url_base_page)
        homePage.go_to_site()
        homePage.scroll_to_element(element)
        homePage.click_dropdown_list(element)
        assert homePage.find_info_dropdown_list(element).text == info

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 