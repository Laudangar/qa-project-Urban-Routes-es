from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import helpers



class UrbanRoutesPage:
    from_field = (By.XPATH, '//input[@id="from"]')
    to_field = (By.XPATH, '//input[@id="to"]')
    order_a_taxi = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    comfort_tariff = (By.XPATH, '//div[text() = "10"]')
    select_phone_number = (By.XPATH, '//div[text() = "Número de teléfono"]')
    stuffed_phone_number = (By.XPATH, '//label[contains(@for,"phone")]')
    next_phone_button = (By.XPATH, '//button[text() = "Siguiente"]')
    space_enter_the_code = (By.XPATH, '//label[contains(@for,"code")]')
    button_confirmation_phone = (By.XPATH, '//button[text() = "Confirmar"]')
    add_payment_method = (By.XPATH, '//div[contains(@class,"pp-text")]')
    select_the_card_payment_method = (By.XPATH, '//img[contains(@class,"pp-plus")]')
    add_a_credit_card = (By.XPATH, '//input[contains(@id,"number")]')
    enter_code_card = (By.XPATH, '//input[contains(@name,"code")]')
    add_card_button = (By.XPATH, '//button[text() = "Agregar"]')
    close_button_payment_methods = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    message_field = (By.XPATH, '//label[@for="comment"][contains(.,"Mensaje para el conductor...")]')
    order_a_blanket_and_tissues = (By.XPATH, '(//span[@class="slider round"])[1]')
    ice_creams = (By.XPATH, '(//div[contains(.,"0")])[30]')
    search_for_a_taxi = (By.XPATH, '//span[@class="smart-button-secondary"]')


    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))


    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)


    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')


    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    def set_order_a_taxi(self):
        self.wait_for_element(*self.order_a_taxi)
        order_button = self.driver.find_element(*self.order_a_taxi)
        order_button.click()


    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()
        self.driver.find_element(*self.comfort_tariff).is_selected()


    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.select_phone_number).click()
        self.driver.find_element(*self.stuffed_phone_number).click()
        self.driver.find_element(*self.stuffed_phone_number).send_keys(phone_number)
        self.driver.find_element(*self.next_phone_button).click()

    def code_phone_number(self):
        self.driver.find_element(*self.space_enter_the_code).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.space_enter_the_code)
                                             ).click()
        phone_code = helpers.retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.space_enter_the_code).send_keys(phone_code)
        self.driver.find_element(*self.button_confirmation_phone).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.stuffed_phone_number).get_property('value')

    def get_code_phone(self):
        return self.driver.find_element(*self.space_enter_the_code).get_property('value')


    def add_payments_method(self):
        self.driver.find_element(*self.add_payment_method).click()


    def select_the_card_payment_methods(self):
        self.driver.find_element(*self.select_the_card_payment_method).click()


    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.add_a_credit_card).send_keys(card_number)
        self.driver.find_element(*self.enter_code_card)
        card_code.send_keys(card_code)
        card_code.send_keys(Keys.TAB)
        self.driver.find_element(*self.add_card_button).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_button_payment_methods)
        ).click()
        self.driver.find_element(*self.close_button_payment_methods).click()


    def get_credit_card(self):
        return self.driver.find_element(*self.add_a_credit_card).get_property('value')


    def get_card_code(self):
        return self.driver.find_element(*self.enter_code_card).get_property('value')


    def set_message_driver(self,message):
        self.driver.find_element(*self.message_field).click()
        self.driver.find_element(*self.message_field).send_keys(message)


    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')


    def set_blanket_and_tissues(self):
        self.driver.find_element(*self.order_a_blanket_and_tissues).click()


    def request_ice_creams(self, quantity=2):
        for _ in range(quantity):
            self.driver.find_element(*self.ice_creams).doubleClick()


    def search_taxi(self):
        self.driver.find_element(*self.search_for_a_taxi).click()


