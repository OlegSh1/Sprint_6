import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import BasePageLocators


class BaseObject:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=3):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))
        except:
            return False
