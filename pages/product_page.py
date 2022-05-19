from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        link.click()
    
    def should_be_product_title_in_basket(self):
        in_basket = self.browser.find_element(*ProductPageLocators.TITLE_OF_PRODUCT_IN_BSK).text
        in_product = self.browser.find_element(*ProductPageLocators.TITLE_OF_PRODUCT).text
        assert in_basket == in_product, "Title wrong"
    
    def should_be_product_price_in_basket(self):
        in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET_IN_BSK).text
        in_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert in_basket == in_product, "Price wrong"

