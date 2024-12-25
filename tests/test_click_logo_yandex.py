import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data.data
from constants import Constants
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage
from data.data import DataOrder


class TestClickLogoYandex:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_click_logo_yandex(self):
        base_page = BasePage(self.driver)
        base_page.go_to_site()

        base_page.find_element(BasePageLocators.logo_yandex).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        assert self.driver.current_url == Constants.url_dzen


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()