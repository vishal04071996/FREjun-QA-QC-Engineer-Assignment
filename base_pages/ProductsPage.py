from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductsPage:
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='inventory_container']")
    PRODUCT_NAMES = (By.XPATH, "//div[@class='inventory_item_name ']")
    SORT_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//div[@class = 'inventory_list']//button")
    CART_ICON = (By.XPATH, "//a[@class = 'shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    # Locators

    # Methods
    def get_product_names(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_ITEMS)
        product_names = [product.find_element(*self.PRODUCT_NAMES).text for product in product_elements]
        return product_names

    def sort_by_name(self):
        sort_dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text("Name (A to Z)")

    def add_all_products_to_cart(self):
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        for button in add_to_cart_buttons:
            button.click()

    def click_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
