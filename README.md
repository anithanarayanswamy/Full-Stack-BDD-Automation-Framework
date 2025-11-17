# Full-Stack BDD Automation Framework

Production-grade test automation framework combining API and Web UI testing using BDD methodology.

##  Project Overview

This framework demonstrates advanced test automation skills covering:
- **API Testing**: REST API automation using Requests library
- **Web UI Testing**: Modern browser automation using Playwright
- **BDD Framework**: Behavior-Driven Development with Behave (Gherkin syntax)
- **CI/CD Integration**: GitHub Actions for continuous testing
- **Page Object Model**: Maintainable web automation architecture

##  Tech Stack

- **Python 3.9+**
- **Behave** (BDD framework)
- **Playwright** (Web automation)
- **Requests** (API testing)
- **Pytest** (Test runner)

## 📁 Project Structure

```text
├── features/
│   ├── api/              # API test scenarios
│   │   └── reqres_api.feature
│   └── web/              # Web UI test scenarios
│       └── saucedemo_login.feature
├── steps/
│   ├── api_steps.py      # API step definitions
│   └── web_steps.py      # Web step definitions
├── pages/
│   ├── base_page.py      # Base page object
│   └── login_page.py     # Login page object
├── utils/
│   ├── api_helper.py     # API utility functions
│   ├── config.py         # Configuration
│   └── logger.py         # Logging setup
├── reports/              # Test execution reports
└── .github/workflows/    # CI/CD configuration
```

-----

## ⚙️ Quick Start

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Full-Stack-BDD-Automation-Framework.git
    cd Full-Stack-BDD-Automation-Framework
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Playwright browsers (Chromium is essential):**

    ```bash
    playwright install chromium
    ```

### Running Tests

```bash
# Run all tests
behave

# Run API tests only
behave features/api/

# Run Web tests only
behave features/web/
```

## 📝 Status

🚧 **Work in Progress** - Week 1  
Currently building: Basic framework structure and API tests

## 👤 Author

**Anitha M** - SDET | Test Automation Engineer  
Building this project to demonstrate modern automation practices


