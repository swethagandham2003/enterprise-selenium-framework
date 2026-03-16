from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_login_user(driver):

    login = LoginPage(driver)

    login.login("john@example.com", "User@123")

    assert "Dashboard" in driver.title

def test_login_admin(driver):

    login = LoginPage(driver)

    login.login("admin@example.com", "Admin@123")

    assert "Dashboard" in driver.title

