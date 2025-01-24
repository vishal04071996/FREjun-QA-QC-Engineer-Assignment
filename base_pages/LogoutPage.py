from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    # Locators
    menu_button = (By.XPATH, "//button[@type = 'button']")  # Menu button
    logout_button = (By.XPATH, "//a[@id = 'logout_sidebar_link']")  # Logout button

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.XPATH, "//input[@id = 'password']")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    # Methods
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def Click_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def Click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()