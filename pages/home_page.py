import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_object import BaseObject


class HomePage(BaseObject):

    def find_dropdown_list(self, element):
        return WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, f".//div[@id='accordion__heading-{element}']")))

    def click_dropdown_list(self, element):
        if self.find_element(BasePageLocators.button_cookie):
            self.find_element(BasePageLocators.button_cookie).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, f".//div[@id='accordion__heading-{element}']"))).click()

    def scroll_to_element(self, num):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, f".//div[@id='accordion__heading-{num}']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_info_dropdown_list(self, element):
        return WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, f".//div[@class='accordion__item']/div[@id='accordion__panel-{element}']/p")))

    def click_logo_yandex(self):
        self.find_element(BasePageLocators.logo_yandex).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)

    def click_logo_scooter(self):
        self.find_element(BasePageLocators.logo_scooter).click()

    def get_current_url(self):
        return self.driver.current_url

    def click_button_order(self):
        self.click_button(BasePageLocators.button_order)