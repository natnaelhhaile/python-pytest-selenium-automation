from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def is_model_present_in_results(self, model_name):
        # Instead of page_source, this method waits for a result item to appear
        xpath = f"//*[contains(text(), '{model_name}')]" 
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False
    
    def click_product_by_text(self, partial_text):
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_text)
        link.click()