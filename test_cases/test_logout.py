import pytest
from _pytest import mark
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from base_pages.LoginPage import LoginPage
from base_pages.LogoutPage import LogoutPage


class Test_01_login:
    page_URL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_valid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_URL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        self.lo = LogoutPage(self)
        self.lo.Click_menu()
        self.lo.Click_logout_button()
