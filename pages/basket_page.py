# https://selenium1py.pythonanywhere.com/en-gb/basket/
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_INNER), "Product not found"

    def should_be_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_INNER), "Product found"
