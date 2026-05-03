# Amazon Web Automation Framework -- Python | Pytest | Selenium

A professional-grade web automation framework built with **Python**, **Pytest**, and **Selenium**. This project implements an industry-standard **Page Object Model (POM)** to automate complex e-commerce workflows, including product searching, variant selection, and cart management.

## 🚀 Key Features

- **Page Object Model (POM):** Architected for high maintainability by separating test scripts from UI locators and page-specific logic.
- **Data-Driven Testing:** Integrated with **Pandas** and **Openpyxl** to execute scenarios based on external data sources (e.g., `data/data.xlsx`).
- **Headless Mode Support:** Optimized for CI/CD pipelines with a custom command-line toggle (`--headless`) for GUI-less execution.
- **Automated WebDriver Management:** Utilizes **Selenium Manager** to automatically handle browser driver compatibility, ensuring seamless runs on Chrome v147+.
- **Automated Failure Reporting:** Custom Pytest hooks capture timestamped screenshots of the browser state at the exact moment of a test failure.
- **Advanced UI Interaction:** Employs JavaScript execution strategies to handle complex web elements and prevent `ElementClickInterceptedException`.

## 🛠️ Tech Stack

- **Core:** Python 3.11
- **Test Runner:** Pytest
- **Automation:** Selenium WebDriver
- **Data Management:** Pandas, Openpyxl

## 📂 Project Structure
```text
.
├── data/               # External test data (Excel files)
├── pages/              # Page Object classes (SearchPage, ResultsPage, ProductPage)
├── screenshots/        # Auto-generated failure and progress snapshots
├── tests/              # Test suite (test_amazon.py)
├── utils.py            # Reusable utilities for data reading and screenshots
├── conftest.py         # Global fixtures and driver configuration
├── pytest.ini          # Test runner configuration and discovery rules
└── requirements.txt    # Project dependencies

## 🧪 Running the Tests

The framework is configured to run tests via the terminal. You can toggle between headed (visible) and headless (background) modes.

**Standard Execution:**
```bash
pytest -s
```
**Headless Execution (for CI/CD):**
```bash
pytest -s --headless
```