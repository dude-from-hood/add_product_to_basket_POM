from pages.product_page import ProductPage
import pytest
from selenium.webdriver import Chrome
import time


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


def test_guest_can_add_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, url)
    page.load()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    assert page.get_book_name() == page.get_alert_text()
    assert page.price_on_card() == page.price_on_message()
    time.sleep(3)
