import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f'Not find element{locator}')

    def click_button_order(self):
        self.find_element(BasePageLocators.button_order).click()

    def click_dropdown_list(self, dropdown_list):
        self.find_element(dropdown_list).click()