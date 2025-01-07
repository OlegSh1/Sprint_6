import time
import allure
import pytest
from selenium import webdriver
from constants import Constants
from pages.home_page import HomePage


class TestClickLogoYandex:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_click_logo_yandex(self):
        home_page = HomePage(self.driver, Constants.url_base_page)
        home_page.go_to_site()
        home_page.click_logo_yandex()
        assert home_page.get_current_url() == Constants.url_dzen

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()