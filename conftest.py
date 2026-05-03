import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # This adds a custom command line argument to pytest
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture
def driver(request):
    chrome_options = Options()

    # Check if '--headless' flag was passed in the trmnl
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        # Adding a common user-agent as it helps avoid bot detection in headless mode
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36")
    # your driver
    driver = webdriver.Chrome(options=chrome_options)
    # print(f"\nUsing driver at: {driver.service.path}")

    # driver.maximize_window()
    yield driver # The test runs here

    # Teardown
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This checks if the test failed during the 'call' phase
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Check if driver fixture is being used 
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            # Save screenshots with the name of the failed test function
            screenshot_path = f"screenshots/FAIL_{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n[FAILURE] Screenshot captured: {screenshot_path}")