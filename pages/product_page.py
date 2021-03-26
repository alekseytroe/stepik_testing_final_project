from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        login_link.click()

    def should_be_message_equal_product_name(self):
        product_name = self.get_product_name()
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        # print(message)
        assert product_name == message, 'No equal product name message'

    def should_be_message_equal_product_price(self):
        product_price = self.get_product_price()
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_price == message, 'No equal product price message'

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

