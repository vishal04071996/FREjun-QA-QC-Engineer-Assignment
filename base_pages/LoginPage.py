from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
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
