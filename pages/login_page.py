from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

class LoginPage(BasePage):
    
    logger = get_logger()

    USERNAME_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()