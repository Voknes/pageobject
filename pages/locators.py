from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_OF_PRODUCT_IN_BSK = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_OF_BASKET_IN_BSK = (By.XPATH,"//*[@id='messages']/div[3]/div/p[1]/strong")
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > .price_color")