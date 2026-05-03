from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import capture_screenshot


class AmazonSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

        # Locators
        self.search_textbox = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def open(self):
        self.driver.get("https://www.amazon.com")

    def search_for_item(self, item_name):
        # Check if we are stuck on the bot challenge page
        if "button below to continue" in self.driver.page_source:
            try:
                # Look for that specific 'Continue shopping' button
                continue_btn = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Continue")
                continue_btn.click()
            except:
                print("Couldn't bypass captcha/bot challenge!")
        search_field = self.wait.until(EC.element_to_be_clickable(self.search_textbox))
        search_field.clear()
        search_field.send_keys(item_name)
        self.driver.find_element(*self.search_button).click()

        # Taking a screenshot
        capture_screenshot(self.driver, "after_search")