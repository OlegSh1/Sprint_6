from selenium.webdriver.common.by import By

class BasePageLocators:
    button_order = [By.CLASS_NAME, 'Button_Button__ra12g']
    dropdown_list_1 = [By.XPATH, ".//div[@id='accordion__heading-0']"]
    info_in_dropdown_list_1 = [By.XPATH, ".//div[@class='accordion__item']/div[@id='accordion__panel-0']/p"]
    logo_scooter = [By.XPATH, ".//img[@alt='Scooter']"]
    logo_yandex = [By.XPATH, ".//img[@alt='Yandex']"]
    button_cookie = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"]