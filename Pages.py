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
    add_number_button = (By.XPATH, '//div[@class="np-button"]') #
    add_number_text = (By.XPATH, '//div[@class="np-text"]')
    input_number = (By.XPATH, '//div[@class="np-input"]/div')
    write_number = (By.ID, 'phone')
    number_button = (By.CLASS_NAME, "button.full")
    code_phone_field = (By.ID, 'code')
    confirmation_code_button = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    add_payment_method = (By.XPATH, '//div[contains(@class,"pp-text")]')
    select_the_card_payment_method = (By.XPATH, '//img[contains(@class,"pp-plus")]')
    add_a_credit_card = (By.XPATH, '//input[contains(@id,"number")]')
    enter_code_card = (By.XPATH, '//input[contains(@name,"code")]')
    space_between_code_and_add_button = (By.XPATH, '//div[contains(@class,"card-wrapper")]')
    add_card_button = (By.XPATH, '//div[@class="pp-buttons"]/button[@type="submit"]')
    close_button_payment_methods = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    message_field = (By.XPATH, '//input[@name="comment"]')
    order_a_blanket_and_tissues = (By.XPATH, '(//span[@class="slider round"])[1]')
    ice_creams = (By.XPATH, '(//div[contains(.,"0")])[30]')
    search_for_a_taxi = (By.XPATH, '//span[@class="smart-button-secondary"]')


    def __init__(self, driver):
        self.driver = driver


    # Seleccionar la ruta
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


    # Seleccionar ordenar un taxi
    def set_order_a_taxi(self):
        self.wait_for_element(self.order_a_taxi)
        order_button = self.driver.find_element(*self.order_a_taxi)
        order_button.click()


    # Selección de la tarifa
    def select_comfort_tariff(self):
        element = self.wait_for_element(self.comfort_tariff)
        element.click()
        assert element.is_selected()


    # Llenado de numero de telefono
    def click_add_number(self):
        self.driver.find_element(*self.add_number_button).click()

    def click_input_number_field(self):
        self.driver.find_element(*self.input_number).click()

    def set_number_input(self, number):
        self.driver.find_element(*self.write_number).send_keys(number)

    def click_number_button(self):
        self.driver.find_element(*self.number_button).click()

    def set_code_phone(self):
        self.driver.find_element(*self.code_phone_field).send_keys(helpers.retrieve_phone_code(self.driver))

    def click_confirmation_code_button(self):
        self.driver.find_element(*self.confirmation_code_button).click()

    def get_add_number_text(self):
        return self.driver.find_element(*self.add_number_text).text

    def set_phone_number(self, number):
        self.click_add_number()
        self.click_input_number_field()
        self.set_number_input(number)
        self.click_number_button()
        self.set_code_phone()
        self.click_confirmation_code_button()


    # Selección del metodo de pago
    def add_payments_method(self):
        self.driver.find_element(*self.add_payment_method).click()

    def select_the_card_payment_methods(self):
        self.driver.find_element(*self.select_the_card_payment_method).click()

    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.add_a_credit_card).send_keys(card_number)
        self.driver.find_element(*self.enter_code_card)
        self.driver.find_element(*self.enter_code_card).send_keys(card_code)
        self.driver.find_element(*self.space_between_code_and_add_button).send_keys(Keys.TAB)

    def get_credit_card(self):
        return self.driver.find_element(*self.add_a_credit_card).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.enter_code_card).get_property('value')

    def add_button_and_close_button(self):
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.close_button_payment_methods).click()


     # Mensaje para el conductor
    def set_message_driver(self,message):
        self.driver.find_element(*self.message_field).click()
        self.driver.find_element(*self.message_field).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')


    # Solicitud de mantas y pañuelos
    def set_blanket_and_tissues(self):
        self.driver.find_element(*self.order_a_blanket_and_tissues).click()


    # Solicitud de helados
    def request_ice_creams(self, quantity=2):
        for _ in range(quantity):
            self.driver.find_element(*self.ice_creams).doubleClick()


    def search_taxi(self):
        self.driver.find_element(*self.search_for_a_taxi).click()


