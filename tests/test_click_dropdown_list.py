from selenium import webdriver
from constants import Constants
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class TestDropDownList:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_click_drop_down_list_1(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_1)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_1).text == Constants.dropdown_list_1

    def test_click_drop_down_list_2(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_2)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_2).text == Constants.dropdown_list_2

    def test_click_drop_down_list_3(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_3)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_3).text == Constants.dropdown_list_3

    def test_click_drop_down_list_4(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_4)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_4)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_4).text == Constants.dropdown_list_4

    def test_click_drop_down_list_5(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_5)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_5)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_5).text == Constants.dropdown_list_5

    def test_click_drop_down_list_6(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_6)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_6)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_6).text == Constants.dropdown_list_6

    def test_click_drop_down_list_7(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_7)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_7).text == Constants.dropdown_list_7

    def test_click_drop_down_list_8(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        element = base_page.find_element(BasePageLocators.dropdown_list_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        base_page.click_dropdown_list(BasePageLocators.dropdown_list_8)
        assert base_page.find_element(BasePageLocators.info_in_dropdown_list_8).text == Constants.dropdown_list_8

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 