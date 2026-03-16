from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    USERS_MENU = (By.XPATH, "//a[contains(text(),'Users')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_users_page(self):

        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        users_menu = self.wait.until(
            EC.element_to_be_clickable(self.USERS_MENU)
        )

        users_menu.click()