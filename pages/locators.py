from selenium.webdriver.common.by import By


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_TEXT = (By.XPATH, "//strong[(text() = 'Coders at Work')]")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_ON_CARD = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
