import pytest
import os
from datetime import datetime

from core.driver_factory import DriverFactory
from config.config import BASE_URL


@pytest.fixture
def driver():

    driver = DriverFactory.create_driver()

    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"{screenshots_dir}/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_name)