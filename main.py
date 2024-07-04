import data
from selenium import webdriver
import helpers
from Pages import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.home = data.urban_routes_url
        cls.driver.get(cls.home)


    def setup_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)


    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.select_from()
        self.routes_page.set_from(address_from)
        self.routes_page.select_to()
        self.routes_page.set_to(address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to


    def test_set_order_a_taxi(self):
        self.routes_page.set_order_a_taxi()


    def test_select_comfort_tariff(self):
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.driver.find_element(*self.routes_page.comfort_tariff).is_selected()


    def test_set_phone_number(self):
        phone_number = data.phone_number
        code_phone = helpers.retrieve_phone_code
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.code_phone_number()
        assert self.routes_page.get_phone_number() == phone_number
        assert self.routes_page.get_code_phone() == code_phone



    def test_add_payment_method(self):
        self.routes_page.add_payments_method()
        assert self.routes_page.driver.find_element(*self.routes_page.select_the_card_payment_method).is_displayed()


    def test_select_the_card_payment_method(self):
        self.routes_page.select_the_card_payment_methods()
        assert self.routes_page.driver.find_element(*self.routes_page.add_a_credit_card).is_displayed()


    def test_add_credit_card(self):
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.add_credit_card(card_number, card_code)
        assert self.routes_page.get_credit_card() == card_number
        assert self.routes_page.get_card_code() == card_code


    def test_set_message_driver(self):
        message_driver = data.message_for_driver
        self.routes_page.set_message_driver(message_driver)
        assert self.routes_page.get_message() == message_driver

    def test_set_blanket_and_tissues(self):
        self.routes_page.set_blanket_and_tissues()
        assert self.routes_page.driver.find_element(*self.routes_page.order_a_blanket_and_tissues).is_selecte

    def test_request_ice_creams(self):
        self.routes_page.request_ice_creams(2)
        assert int(self.routes_page.driver.find_element(*self.routes_page.ice_creams).text) == 2

    def test_search_taxi(self):
        self.routes_page.search_taxi()
        assert self.routes_page.driver.find_element(*self.routes_page.search_for_a_taxi).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
