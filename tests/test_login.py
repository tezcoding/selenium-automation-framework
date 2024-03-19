import sys

sys.path.append(".")
from pages.login_page import LoginPage
from pages.home_page import HomePage

import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time


baseUrl = "https://www.saucedemo.com/"
driver = webdriver.Chrome()
login_page = LoginPage(driver)
home_page = HomePage(driver)


class LoginTests(unittest.TestCase):
    def test_can_login(self):
        driver.get(baseUrl)
        logo_text = login_page.get_login_logo_text()
        self.assertEqual("Swag Labs", logo_text)
        login_page.perform_a_login("standard_user", "secret_sauce")
        self.assertEqual(7, home_page.get_count_of_inventory_displayed())


if __name__ == "__main__":
    unittest.main()
