import allure
import pytest
from selenium import webdriver

import data.data
from constants import Constants
from locators.home_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.data import DataOrder


class TestClickLogoScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_click_logo_scooter(self):
        home_page = HomePage(self.driver, Constants.url_base_page)
        home_page.go_to_site()
        home_page.click_logo_scooter()
        assert home_page.get_current_url() == Constants.url_base_page

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()