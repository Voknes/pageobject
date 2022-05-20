from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
        "Products is presented, but should not be"
    
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
        "Products is presented, but should not be"