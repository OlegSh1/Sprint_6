from selenium.webdriver.common.by import By

class OrderPageLocators:
    input_first_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    input_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    input_metro = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    input_phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    input_delivery_date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    div_date_delivery = [By.XPATH, ".//div[@aria-label='Choose вторник, 31-е декабря 2024 г.']"]
    input_rental_period = [By.XPATH, ".//div[@class='Dropdown-control']"]
    input_black = [By.XPATH, ".//input[@id='black']"]
    input_grey = [By.XPATH, ".//input[@id='grey']"]
    input_comment = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    order_button_yes = [By.XPATH, ".//button[text()='Да']"]