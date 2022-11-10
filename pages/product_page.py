from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def click_on_basket_button(self):
        button_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def get_alert_text(self):
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_TEXT)
        print(alert_text.text)

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print(book_name.text)

    def price_on_card(self):
        price_card = self.browser.find_element(
            *ProductPageLocators.PRICE_ON_CARD)
        print(price_card.text)

    def price_on_message(self):
        alert_price = self.browser.find_element(
            *ProductPageLocators.ALERT_PRICE)
        print(alert_price.text)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
