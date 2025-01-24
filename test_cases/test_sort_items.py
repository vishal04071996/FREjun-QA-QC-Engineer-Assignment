from selenium import webdriver
from base_pages.SortingPage import SortingPage
import pytest


class TestSorting:
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

    def test_sort_by_name_ascending(self):
        """
        Test sorting items by Name (A to Z).
        """
        sorting_page = SortingPage(self.driver)
        sorting_page.select_sort_option("Name (A to Z)")
        product_names = sorting_page.get_sorted_product_names()

        # Assert that the names are sorted alphabetically
        assert product_names == sorted(product_names), "Products are not sorted alphabetically."

    def test_sort_by_name_descending(self):
        """
        Test sorting items by Name (Z to A).
        """
        sorting_page = SortingPage(self.driver)
        sorting_page.select_sort_option("Name (Z to A)")
        product_names = sorting_page.get_sorted_product_names()

        # Assert that the names are sorted in reverse alphabetical order
        assert product_names == sorted(product_names,
                                       reverse=True), "Products are not sorted in reverse alphabetical order."

    def test_sort_by_price_low_to_high(self):
        """
        Test sorting items by Price (low to high).
        """
        sorting_page = SortingPage(self.driver)
        sorting_page.select_sort_option("Price (low to high)")
        product_prices = sorting_page.get_sorted_product_prices()

        # Assert that the prices are sorted from low to high
        assert product_prices == sorted(product_prices), "Products are not sorted by price from low to high."

    def test_sort_by_price_high_to_low(self):
        """
        Test sorting items by Price (high to low).
        """
        sorting_page = SortingPage(self.driver)
        sorting_page.select_sort_option("Price (high to low)")
        product_prices = sorting_page.get_sorted_product_prices()

        # Assert that the prices are sorted from high to low
        assert product_prices == sorted(product_prices,
                                        reverse=True), "Products are not sorted by price from high to low."
