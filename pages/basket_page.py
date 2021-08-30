from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.basket_items), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.basket_empty_message), "Message about adding is not present"

        actual = self.browser.find_element(*BasketPageLocators.basket_empty_message).text
        expected = "Your basket is empty."
        assert expected in actual, "Message did not match"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.basket_items), "Basket is empty"


