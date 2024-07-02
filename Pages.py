from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import helpers
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    home_url = 'https://cnt-7bfe5a33-d796-4d82-87af-589c8aa0e6a3.containerhub.tripleten-services.com?lng=es'
    from_field = (By.CSS_SELECTOR, '#from')
    to_field = (By.CSS_SELECTOR, '#to')
    order_a_taxi = (By.CLASS_NAME, "button.round")
    comfort_tariff = (By.XPATH, '//div[text() = "10"]')
    select_phone_number = (By.XPATH, '//div[text() = "Número de teléfono"]')
    stuffed_phone_number = (By.CSS_SELECTOR, '#phone')
    next_phone_button = (By.XPATH, '//button[text() = "Siguiente"]')
    space_enter_the_code = (By. CSS_SELECTOR, '#code.input')
    button_confirmation_phone = (By.XPATH, '//button[text() = "Confirmar"]')
    add_payment_method = (By.CSS_SELECTOR, '.pp-text')
    select_the_card_payment_method = (By.CSS_SELECTOR, '.pp-plus-container')
    add_a_credit_card = (By.CSS_SELECTOR, '#number')
    enter_code_card = (By.CSS_SELECTOR, '#code.card-input')
    add_card_button = (By.XPATH, '//button[text() = "Agregar"]')
    close_button_payment_methods = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    message_field = (By.CSS_SELECTOR, '#comment')
    order_a_blanket_and_tissues = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    ice_creams = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    search_for_a_taxi = (By.XPATH, '//span[@class="smart-button-secondary"]')


    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 5).until(EC.expected_conditions.visibility_of_element())


    def select_from(self):
        self.driver.find_element(*self.from_field).click()


    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)


    def select_to(self):
        self.driver.find_element(*self.to_field).click()


    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')


    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    def set_order_a_taxi(self):
        self.driver.find_element(*self.order_a_taxi).click()


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


