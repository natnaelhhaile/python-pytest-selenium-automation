# 🚀 Professional Selenium-Python Automation Framework

A modular, enterprise-grade test automation framework built with **Python**, **Pytest**, and **Selenium** designed to demonstrate advanced Page Object Model (POM) architecture, CI/CD integration, and Automated Quality Reporting.

### 📊 [View Live Allure Dashboard](https://natnaelhhaile.github.io/python-pytest-selenium-automation/12/index.html)

## 🚀 Key Features

- **Scalable Architecture:** Implemented a clean Page Object Model (POM) to decouple test logic from UI selectors, ensuring high maintainability and code reusability.
- **CI/CD Pipeline Orchestration:** Architected a GitHub Actions workflow that automatically triggers browser-based testing on every code push, ensuring continuous quality assurance.
- **Automated Reporting Dashboard:** Integrated Allure Reports to transform raw terminal output into a stakeholder-ready dashboard, featuring historical trend graphs and failure analytics.
- **Data-Driven Testing:** Integrated with **Pandas** and **Openpyxl** to execute scenarios based on external data sources (e.g., `data/data.xlsx`).
- **Dynamic Bot Bypass & Failure Capture:** Utilized Explicit Waits and XPath strategies to ensure test continuity and developed a custom Pytest hook in conftest.py that automatically captures and embeds browser screenshots directly into the Allure report upon test failure for rapid debugging.
- **Automated WebDriver Management:** Utilizes **Selenium Manager** to automatically handle browser driver compatibility (Chrome v147+).
- **Advanced UI Interaction:** Employs JavaScript execution strategies and **WebDriverWait** to handle dynamic elements and prevent `ElementClickInterceptedException`.

## 🛠️ Tech Stack

- **Core:** Python 3.11
- **Test Runner:** Pytest
- **Automation:** Selenium WebDriver
- **Reporting:** Allure Framework
- **Infrastructure:** GitHub Actions
- **Data Management:** Pandas, Openpyxl

## ⚙️ CI/CD Workflow Breakdown

1. **Environment Setup:** Runner initializes a headless Ubuntu environment and installs dependencies from `requirements.txt`.
2. **Execution:** Pytest executes the Selenium suite in Headless Chrome mode to optimize performance in the cloud.
3. **Reporting:** Raw results are processed by the Allure CLI to generate a static HTML site.
4. **Deployment** The framework automatically pushes the fresh report to the `gh-pages` branch, updating the live URL instantly.

## 📈 Key Technical Challenges Solved

- **Bot Detection & Stealth:** Faced and bypassed complex anti-bot measures (CAPTCHAs) by implementing Chrome Stealth arguments and User-Agent rotation, simulating authentic user behavior in a data-center environment.
- **Automated Deployment Permissions:** Resolved GitHub Actions "404" and deployment errors by fine-tuning repository write-permissions and architecting a clean-branch deployment strategy for GitHub Pages.

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
## 📝 How to Run Locally

1. Clone the repository:
```bash
    git clone https://github.com/natnaelhhaile/python-pytest-selenium-automation.git
```
2. Install dependencies:
```bash
    pip install -r requirements.txt
```
3. Execute tests:
```bash
    pytest --alluredir=allure-results
```
4. View reports:
```bash
    allure serve allure-results
```

### Developed by [Natnael Haile](https://github.com/natnaelhhaile)