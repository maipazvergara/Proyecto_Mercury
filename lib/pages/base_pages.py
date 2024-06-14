from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def init(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)