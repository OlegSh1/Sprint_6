import allure
import pytest
from selenium import webdriver

import data.data
from constants import Constants
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage
from data.data import DataOrder


class TestClickLogoScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_click_logo_scooter(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        base_page.find_element(BasePageLocators.logo_scooter).click()

        assert self.driver.current_url == Constants.url_base_page

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()