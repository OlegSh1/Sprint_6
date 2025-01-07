import allure
import pytest
from selenium import webdriver

import data.data
from constants import Constants
from locators.home_page_locators import BasePageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestCreatOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('name,last_name,address,metro,phone,delivery_date,date_rent_period,color,comment', [data.data.DataOrder.first_paramtrize, data.data.DataOrder.second__paramtrize])
    def test_create_order(self, name, last_name, address, metro,phone, delivery_date, date_rent_period, color, comment):
        home_page = HomePage(self.driver, Constants.url_base_page)
        home_page.go_to_site()
        orderPage = OrderPage(self.driver, Constants.url_order_bage)

        home_page.click_button_order()

        orderPage.set_contact_information(name, last_name, address, metro, phone)
        orderPage.set_info_order(delivery_date ,date_rent_period, color, comment)

        assert orderPage.get_order_button_text() == 'Да'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()