from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.quantity_dropdown = (By.ID, "quantity")
        self.add_to_cart_button = (By.ID, "add-to-cart-button")
        self.no_coverage_button = (By.ID, "attachSiNoCoverage")

    def select_color(self, color_name):
        xpath = f"//img[@alt='{color_name}']"
        color_element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        # Using JavaScript to bypass 'ElementClickInterceptedException'
        self.driver.execute_script("arguments[0].click();", color_element)
        print(f"Successfully selected color: {color_name}")

    def select_quantity(self, value):
        dropdown = Select(self.driver.find_element(*self.quantity_dropdown))
        dropdown.select_by_value(value)

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        # Handle the 'No Thanks' pop up
        try:
            self.wait.until(EC.element_to_be_clickable(self.no_coverage_button)).click()
        except:
            pass # pop up might not always appear