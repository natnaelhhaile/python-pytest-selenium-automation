import pandas as pd
import os
from datetime import datetime


def get_excel_data():
    # Read the first row of the file and convert it into a dictionary
    df = pd.read_excel("data/data.xlsx")
    return df.iloc[0].to_dict()

def capture_screenshot(driver, name):
    """
        Captures a screenshot and saves it to the screenshots/ directory.
    """
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    file_path = f"screenshots/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)
    print(f"Screenshot saved at: {file_path}")