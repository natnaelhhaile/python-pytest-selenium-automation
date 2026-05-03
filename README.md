# Amazon Web Automation Framework - Python | Pytest | Selenium

A professional-grade web automation framework built with **Python**, **Pytest**, and **Selenium**. This project implements an industry-standard **Page Object Model (POM)** to automate complex e-commerce workflows, including product searching, variant selection, and cart management.

## 🚀 Key Features

- **Page Object Model (POM):** Architected for high maintainability by separating test scripts from UI locators and page-specific logic.
- **Interactive Allure Reporting:** Generates rich, web-based reports featuring:
    - Step-by-step execution logs.
    - Embedded failure screenshots directly in the report UI.
    - Test severity levels (Critical, Normal, Minor).
    - Historical trend analysis and suite execution dashboards.
- **Resilient Bot Bypass:** Custom logic to detect and interact with "Continue shopping" challenge pages, utilizing **Explicit Waits** and **XPath strategies** to ensure test continuity.
- **Data-Driven Testing:** Integrated with **Pandas** and **Openpyxl** to execute scenarios based on external data sources (e.g., `data/data.xlsx`).
- **Headless Mode Support:** Optimized for CI/CD pipelines with a custom command-line toggle (`--headless`) for GUI-less execution.
- **Automated WebDriver Management:** Utilizes **Selenium Manager** to automatically handle browser driver compatibility (Chrome v147+).
- **Automated Failure Reporting:** Custom Pytest hooks capture timestamped screenshots of the browser state at the exact moment of a test failure.
- **Advanced UI Interaction:** Employs JavaScript execution strategies and **WebDriverWait** to handle dynamic elements and prevent `ElementClickInterceptedException`.

## 🛠️ Tech Stack

- **Core:** Python 3.11
- **Test Runner:** Pytest
- **Automation:** Selenium WebDriver
- **Reporting:** Allure Framework
- **Data Management:** Pandas, Openpyxl

## 📂 Project Structure

```text
.
├── allure-results/     # Raw JSON/XML report data (generated at runtime)
├── data/               # External test data (Excel files)
├── pages/              # Page Object classes (SearchPage, ResultsPage, ProductPage)
├── screenshots/        # Auto-generated failure and progress snapshots
├── tests/              # Test suite (test_amazon.py)
├── utils.py            # Reusable utilities for data reading and screenshots
├── conftest.py         # Global fixtures and driver configuration
├── pytest.ini          # Test runner configuration and discovery rules
├── .gitignore          # Prevents pushing node_modules, .env, and local caches
└── requirements.txt    # Project dependencies
```

