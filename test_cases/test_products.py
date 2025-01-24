from _pytest import mark

from base_pages.LoginPage import LoginPage
from base_pages.ProductsPage import ProductsPage
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_02_products:

    page_URL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_Products(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_URL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        products_page = ProductsPage(self.driver)
        products_page.sort_by_name()
        product_names = products_page.get_product_names()
        assert product_names == sorted(product_names), "Products are not sorted by name."
        products_page = ProductsPage(self.driver)
        products_page.add_all_products_to_cart()

        # Verify cart icon shows the number of items added
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert int(cart_icon) > 0, "No items were added to the cart."







