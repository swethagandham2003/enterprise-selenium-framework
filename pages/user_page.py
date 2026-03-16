from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UsersPage:

    add_user_button = (By.XPATH,"//button[contains(text(),'Add New User')]")

    name = (By.XPATH,"//input[@type='text']")
    email = (By.XPATH,"//input[@type='email']")
    age = (By.XPATH,"//input[@type='number']")
    password = (By.XPATH,"//input[@type='password']")
    submit=(By.XPATH, "//button[@type='submit']")

    users_table_rows = (By.XPATH,"//table/tbody/tr")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_add_user(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_user_button)
        ).click()

    def create_user(self,name,email,age, password):

        self.wait.until(
            EC.visibility_of_element_located(self.name)
        ).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.age).send_keys(age)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit).click()
        self.wait.until(
            EC.invisibility_of_element_located(self.submit)
        )

    def verify_user_exists(self, name, email):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.users_table_rows)
        )
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            table_name = columns[1].text
            table_email = columns[2].text

            print("TABLE DATA:", table_name, table_email)

            if table_name == name and table_email == email:
                return True
            
        return False