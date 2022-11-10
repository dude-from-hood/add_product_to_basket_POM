from pages.product_page import ProductPage
import pytest
from selenium.webdriver import Chrome
import time


@pytest.fixture
def browser():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.load()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    assert page.get_book_name() == page.get_alert_text()
    assert page.price_on_card() == page.price_on_message()
