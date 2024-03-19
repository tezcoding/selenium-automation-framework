from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def __get_inventory_items(self):
        return WW(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
        )

    def get_count_of_inventory_displayed(self):
        return len(self.__get_inventory_items())
