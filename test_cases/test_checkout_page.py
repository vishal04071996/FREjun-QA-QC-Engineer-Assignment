from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.CartPage import CartPage
from base_pages.CheckoutPage import CheckoutPage
from base_pages.LoginPage import LoginPage
from base_pages.ProductsPage import ProductsPage


class Test_04_checkout:
    page_URL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    first_name = "demo"
    last_name = "test"
    zip_code = "test zip code"

    def test_checkout(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_URL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        self.ck = CheckoutPage(self.driver)
        self.ck.click_add_to_cart()
        self.ck.click_to_checkout_icon()
        self.ck.check_out_button







