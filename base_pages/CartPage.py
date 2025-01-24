from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    # Locators
    product_add_buttons = (By.CLASS_NAME, "btn_inventory")  # Add to cart buttons for products
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    checkout_button = (By.ID, "checkout")
    cart_items = (By.CLASS_NAME, "cart_item")
    item_prices = (By.CLASS_NAME, "inventory_item_price")
    subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
    tax_label = (By.CLASS_NAME, "summary_tax_label")
    total_label = (By.CLASS_NAME, "summary_total_label")
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, product_indices):
        """
        Add specific products to the cart based on their indices.
        :param product_indices: List of indices for products to add (0-based).
        """
        buttons = self.driver.find_elements(*self.product_add_buttons)
        for index in product_indices:
            buttons[index].click()

    def go_to_cart(self):
        """Click on the cart icon to navigate to the cart."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()

    def proceed_to_checkout(self):
        """Click the checkout button to proceed."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """
        Fill in the checkout information.
        :param first_name: First name of the user.
        :param last_name: Last name of the user.
        :param postal_code: Postal code of the user.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_payment_values(self):
        """
        Retrieve payment details like subtotal, tax, and total.
        :return: A dictionary with 'subtotal', 'tax', and 'total' values.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.subtotal_label)
        )
        subtotal = float(self.driver.find_element(*self.subtotal_label).text.split("$")[-1])
        tax = float(self.driver.find_element(*self.tax_label).text.split("$")[-1])
        total = float(self.driver.find_element(*self.total_label).text.split("$")[-1])
        return {"subtotal": subtotal, "tax": tax, "total": total}
