from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SortingPage:
    # Locators
    sorting_dropdown = (By.CLASS_NAME, "product_sort_container")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    product_prices = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def select_sort_option(self, sort_option):
        """
        Select a sorting option from the dropdown.
        :param sort_option: The text of the option to select.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.sorting_dropdown)
        )
        dropdown = Select(self.driver.find_element(*self.sorting_dropdown))
        dropdown.select_by_visible_text(sort_option)

    def get_sorted_product_names(self):
        """
        Get the list of product names currently displayed.
        :return: List of product names.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_names)
        )
        return [name.text for name in self.driver.find_elements(*self.product_names)]

    def get_sorted_product_prices(self):
        """
        Get the list of product prices currently displayed.
        :return: List of product prices as floats.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_prices)
        )
        return [float(price.text.replace("$", "")) for price in self.driver.find_elements(*self.product_prices)]
