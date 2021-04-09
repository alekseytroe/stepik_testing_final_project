# pytest -s test_product_page.py
# pytest -v --tb=line --language=en -m need_review
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        1. +открыть страницу регистрации;
        2. +зарегистрировать нового пользователя;
        3. проверить, что пользователь залогинен.
        """
        link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        # time.sleep(90)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_equal_product_name()
        page.should_be_message_equal_product_price()
        # time.sleep(15)

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        """
        1. Открываем страницу товара
        2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(self, browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_equal_product_name()
    page.should_be_message_equal_product_price()
    # time.sleep(15)


def test_guest_cant_see_success_message(self, browser):
    """
    1. Открываем страницу товара
    2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара
    2. Добавляем товар в корзину
    3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара
    2. Добавляем товар в корзину
    3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """"
    1. Гость открывает главную страницу
    2. Переходит в корзину по кнопке в шапке сайта
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    # time.sleep(10)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_product_in_basket()
