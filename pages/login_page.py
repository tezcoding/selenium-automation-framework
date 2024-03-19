from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def __get_username_field(self):
        return WW(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
        )

    def __get_password_field(self):
        return WW(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#password"))
        )

    def __get_login_button(self):
        return WW(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button"))
        )

    def __get_login_logo_element(self):
        return WW(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login_logo"))
        )

    def perform_a_login(self, username, password):
        self.__get_username_field().send_keys(username)
        self.__get_password_field().send_keys(password)
        self.__get_login_button().click()

    def get_login_logo_text(self):
        return self.__get_login_logo_element().text
