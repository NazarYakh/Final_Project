from .base_page import BasePage
from .locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual = self.browser.current_url
        expected = "login"
        assert expected in actual, "login in current url is not found"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.Login), "login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.Reg), "Reg form not found"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.reg_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.reg_pass1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.reg_pass2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.reg_button).click()
