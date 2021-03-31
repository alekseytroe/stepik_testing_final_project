from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner>strong')
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a")


class BasketPageLocators:
    BASKET_INNER = (By.CSS_SELECTOR, '#basket_formset')
