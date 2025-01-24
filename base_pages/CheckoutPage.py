from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    # Locators
    check_out_button = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        # Logic to add items to the cart
        pass

    def click_to_checkout_icon(self):
        # Logic to click on the cart icon
        pass

    def click_check_out_button(self):
        """Click the checkout button after waiting for it to be clickable."""
        # Wait for the checkout button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.check_out_button)
        )
        self.driver.find_element(*self.check_out_button).click()
