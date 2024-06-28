import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi = (By.XPATH, '//button[text() = "Pedir un taxi"]')
    comfort_tariff = (By.XPATH, '//div[text() = "10"]')
    stuffed_phone_number = (By.CSS_SELECTOR, '#phone')
    next_phone_button = (By.XPATH, '//button[text() = "Siguiente"]')
    button_confirmation_phone = (By.XPATH, '//button[text() = "Confirmar"]')
    add_payment_method = (By.CSS_SELECTOR, '.pp-text')
    select_the_card_payment_method = (By.CSS_SELECTOR, '.pp-plus-container')
    add_a_credit_card = (By.CSS_SELECTOR, '#number')
    enter_code = (By.CSS_SELECTOR, '#code.card-input')
    add_card_button = (By.XPATH, '//button[text() = "Agregar"]')
    close_button_payment_methods = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    message_field = (By.CSS_SELECTOR, '#comment')
    order_a_blanket_and_tissues = (By.XPATH, '//span[@class="slider round"]')
    ice_creams (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    search_for_a_taxi (By.XPATH, '//span[@class="smart-button-secondary"]')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_order_a_taxi(self):
        self.driver.find_element(*self.order_a_taxi).click()

    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.stuffed_phone_number).send_keys(phone_number)
        code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.phone_number_field).send_keys(code)

    def set_next_phone_button(self):
        self.driver.find_element(*self.next_phone_button).click()

    def set_confirmation_phone(self):
        self.driver.find_element(*self.button_confirmation_phone).click()

    def add_payments_method(self):
        self.driver.find_element(*self.add_payment_method).click()

    def select_the_card_payment_methods(self):
        self.driver.find_element(*self.select_the_card_payment_method).click()

    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.add_a_credit_card).send_keys(card_number)
        self.driver.find_element(*self.enter_code)
        card_code_input.send_keys(card_code)
        card_code_input.send_keys(Keys.TAB)

    def add_cards_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def close_button_payment(self):
        self.driver.find_element(*self.close_button_payment_methods).click()

    def set_message_driver(self,massage):
        self.driver.find_element(*self.message_field).send_keys(message)

    def set_blanket_and_tissues(self):
        self.driver.find_element(*self.order_a_blanket_and_tissues).click()

    def request_ice_creams(self, quantity=2):
        for _ in range(quantity):
            self.driver.find_element(*self.ice_creams).doubleClick()

    def search_taxi(self):
        self.driver.find_element(*self.search_for_a_taxi).click()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_order_a_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_order_a_taxi()

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)

    def test_set_next_phone_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_next_phone_button()

    def test_set_confirmation_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_confirmation_phone()

    def test_add_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_payments_method()

    def test_select_the_card_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_the_card_payment_methods()

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_credit_card(card_number, card_code)

    def test_add_card_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_cards_button()

    def test_close_button_payment(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.close_button_payment()

    def test_set_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        messaje_driver = data.message_for_driver
        routes_page.set_message_driver(messaje_driver)

    def test_set_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket_and_tissues()

    def test_request_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_creams(2)

    def test_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.search_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
