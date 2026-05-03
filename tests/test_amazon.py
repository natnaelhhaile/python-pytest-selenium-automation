from pages.search_page import AmazonSearchPage
from pages.results_page import AmazonResultsPage
from pages.product_page import AmazonProductPage
from utils import get_excel_data


def test_amazon_full_purchase_workflow(driver):
    # 1. Load your data
    data = get_excel_data()

    # 2. Initialize pages
    search_pg = AmazonSearchPage(driver)
    results_pg = AmazonResultsPage(driver)
    product_pg = AmazonProductPage(driver)

    # 3. Search logic
    search_pg.open()
    search_query = f"{data['itemName']} {data['model']}"
    search_pg.search_for_item(search_query)

    # 4. Results logic
    assert results_pg.is_model_present_in_results(data['model']), f"Could not find {data['model']}"
    results_pg.click_product_by_text("Flip 6 - Portable Bluetooth Speaker")

    # 5. Products logic
    product_pg.select_color(data['color'])
    product_pg.select_quantity("1")
    product_pg.add_to_cart()

    print("Test passed: Item added to cart successfully.")