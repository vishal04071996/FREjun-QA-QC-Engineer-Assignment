from selenium import webdriver
from base_pages.CartPage import CartPage
import pytest

class TestCartPayment:
    page_URL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def setup_method(self):
        """
        Setup the test environment.
        """
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_URL)
        self.driver.implicitly_wait(10)

        # Login to the application
        self.driver.find_element("id", "user-name").send_keys(self.username)
        self.driver.find_element("id", "password").send_keys(self.password)
        self.driver.find_element("id", "login-button").click()

    def teardown_method(self):
        """
        Quit the driver after the test.
        """
        self.driver.quit()

    def test_add_to_cart_and_verify_payment(self):
        """
        Test adding items to the cart and verifying payment values.
        """
        cart_page = CartPage(self.driver)

        # Add specific products to the cart
        cart_page.add_products_to_cart([0, 2, 4])  # Adding products by their indices

        # Navigate to cart and proceed to checkout
        cart_page.go_to_cart()
        cart_page.proceed_to_checkout()

        # Fill out checkout info
        cart_page.fill_checkout_info("John", "Doe", "12345")

        # Get payment values
        payment_values = cart_page.get_payment_values()

        # Verify payment values
        subtotal = payment_values["subtotal"]
        tax = payment_values["tax"]
        total = payment_values["total"]

        # Assert that the subtotal is the sum of selected product prices
        item_prices = self.driver.find_elements_by_class_name("inventory_item_price")
        selected_prices = [float(item_prices[i].text.replace("$", "")) for i in [0, 2, 4]]
        assert subtotal == sum(selected_prices), "Subtotal does not match the sum of selected item prices."

        # Assert that total equals subtotal + tax
        assert total == round(subtotal + tax, 2), "Total does not match subtotal + tax."

        print("Test passed: Payment values are correct.")
