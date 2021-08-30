from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.basket_button), "Basket button is not found"
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.basket_button)
        add_to_basket_button.click()

    def success_message_after_adding(self):
        assert self.is_element_present(
            *ProductPageLocators.product_name), "Product name is not found"
        assert self.is_element_present(
            *ProductPageLocators.success_adding), "Product don`t add to basket"
        product_name = self.browser.find_element(
            *ProductPageLocators.product_name).text

        message = self.browser.find_element(*ProductPageLocators.success_adding).text

        assert product_name in message, "No product name in message"

    def basket_price(self):
        assert self.is_element_present(
            *ProductPageLocators.product_price), "Product price is not found"
        assert self.is_element_present(
            *ProductPageLocators.basket_price), "Total basket price is not found"
        product_price = self.browser.find_element(
            *ProductPageLocators.product_price).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.basket_price).text
        assert product_price == basket_price, "No product price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.success_adding), "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.success_adding), "Success message is not present, but should be"


