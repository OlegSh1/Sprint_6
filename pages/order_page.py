import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from pages.base_object import BaseObject


class OrderPage(BaseObject):

    def set_first_name(self, name):
        self.find_element(OrderPageLocators.input_first_name).send_keys(name)

    def set_last_name(self, last_name):
        self.find_element(OrderPageLocators.input_last_name).send_keys(last_name)

    def set_address(self, address):
        self.find_element(OrderPageLocators.input_address).send_keys(address)

    def set_metro(self, metro):
        self.find_element(OrderPageLocators.input_metro).click()
        self.find_element([By.XPATH, f".//*[text()='{metro}']"]).click()

    def set_phone(self, phone):
        self.find_element(OrderPageLocators.input_phone).send_keys(phone)

    def click_button_next(self):
        if self.find_element([By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"]):
            self.find_element([By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"]).click()
        self.find_element(OrderPageLocators.button_next).click()

    def set_date_delivery_date(self, delivery_date):
        self.find_element(OrderPageLocators.input_delivery_date).click()
        self.find_element([By.XPATH, f".//div[@aria-label='{delivery_date}']"]).click()

    def set_rental_period(self, date_rent_period):
        self.find_element(OrderPageLocators.input_rental_period).click()
        self.find_element([By.XPATH, f".//*[text()='{date_rent_period}']"]).click()

    def set_color(self, color):
        self.find_element([By.ID, color]).click()

    def set_comment(self, comment):
        self.find_element(OrderPageLocators.input_comment).send_keys(comment)

    def button_click_order(self):
        self.find_element(OrderPageLocators.button_order).click()

    @allure.step('Вводим контактные данные в форму заказа')
    def set_contact_information(self, name, last_name, address, metro, phone):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_button_next()

    @allure.step('Вводим данные заказа')
    def set_info_order(self, delivery_date, date_rent_period, color, comment):
        self.set_date_delivery_date(delivery_date)
        self.set_rental_period(date_rent_period)
        self.set_color(color)
        self.set_comment(comment)
        self.button_click_order()