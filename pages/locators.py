from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    Login = (By.CLASS_NAME, "col-sm-6.login_form")
    Reg = (By.CLASS_NAME, "col-sm-6.register_form")
    reg_email = (By.CSS_SELECTOR, "#id_registration-email")
    reg_pass1 = (By.CSS_SELECTOR, "#id_registration-password1")
    reg_pass2 = (By.CSS_SELECTOR, "#id_registration-password2")
    reg_button = (By.NAME, "registration_submit")


class ProductPageLocators:
    basket_button = (By.CLASS_NAME, "btn-add-to-basket")
    success_adding = (By.CSS_SELECTOR, "div.alertinner")
    product_name = (By.CSS_SELECTOR, "div.product_main h1")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    basket_price = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasketPageLocators:
    basket_items = (By.TAG_NAME, "[class='basket-items']")
    basket_empty_message = (By.CSS_SELECTOR, "#content_inner")


