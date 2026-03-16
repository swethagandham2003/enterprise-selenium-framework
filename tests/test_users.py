from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.user_page import UsersPage
from utils.logger import get_logger
import pytest

logger = get_logger()

@pytest.mark.regression
@pytest.mark.parametrize(
    "name,email,age,password",
    [
        ("tester1", "abc1234@gmail.com", "24", "Test@123"),
        ("Tester2", "def1234@gmail.com", "25", "Test@123"),
        ("Tester3", "ghi1234@gmail.com", "26", "Test@123"),
    ]
)
def test_create_users(driver, name, email, age, password):

    logger.info("Starting test: Add User")
    login = LoginPage(driver)

    login.login("admin@example.com", "Admin@123")

    dashboard = DashboardPage(driver)
    logger.info("Logging in as admin")

    dashboard.go_to_users_page()

    users = UsersPage(driver)
    logger.info("Opening Users page")

    logger.info("Clicking Add User")
    users.click_add_user()
    logger.info("Creating new user")
    users.create_user(name, email, age, password)

    logger.info("Verifying user exists in table")
    assert users.verify_user_exists(name, email)

    logger.info("Test completed successfully")