# Sauce Demo Test Automation

This project is an automated test suite for the Sauce Demo web application using Selenium, Pytest, and the Page Object Model (POM) design pattern. It includes tests for login, sorting, adding items to the cart, checkout, and logout functionalities.

---

## Setup Instructions

### Prerequisites
Before starting, ensure you have the following installed:
1. **Python (3.7 or higher)**  
   Download from [python.org](https://www.python.org/).
2. **Google Chrome browser**  
   Download from [google.com/chrome](https://www.google.com/chrome/).
3. **ChromeDriver**  
   Ensure the version matches your Chrome browser. Download from [ChromeDriver](https://chromedriver.chromium.org/downloads).

---

### Steps to Set Up the Environment

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

Running the Tests
To Run All Tests:
Execute the following command to run all test cases:

pytest
To Run Tests in Parallel:
Use pytest-xdist to run tests in parallel (adjust the number of workers as needed):

pytest -n auto
To Generate HTML Reports:
Run tests with pytest-html to generate an HTML report:

pytest --html=reports/test_report.html --self-contained-html
To Run Specific Test Files:
Run a specific test file (e.g., test_login.py):

pytest tests/test_login.py
To Debug Failed Tests:
Re-run only the failed tests:


pytest --last-failed

Assumptions and Constraints
Assumptions
The Sauce Demo application is available at https://www.saucedemo.com/.
The valid login credentials are:
Username: standard_user
Password: secret_sauce

Constraints
This project uses ChromeDriver for testing. Ensure it matches the version of the Chrome browser installed.
Tests assume stable internet connectivity as they depend on an online application.
This project is designed for demonstration purposes and does not include advanced exception handling or CI/CD pipeline integration.
Test data (e.g., usernames, passwords, and zip codes) is hardcoded. In production, consider using environment variables or a configuration file.

Directory Structure

project/
│
├── base_pages/          # Page Object Model classes
│   ├── CartPage.py
│   ├── CheckoutPage.py
│   ├── LoginPage.py
│   ├── LogoutPage.py
│   ├── ProductsPage.py
│   └── SortingPage.py
│
├── tests/               # Test cases
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_products.py
│   └── test_sorting.py
│
├── reports/             # HTML reports
│   └── test_report.html
│
├── requirements.txt     # Dependencies
├── pytest.ini           # Pytest configuration
└── README.md            # Project documentation

Troubleshooting
Issue: ChromeDriver not found
Solution: Ensure ChromeDriver is installed and its path is added to the system's PATH variable.

Issue: Test fails due to stale elements
Solution: Increase the implicit wait time in your tests:


self.driver.implicitly_wait(10)
Issue: pytest command not recognized
Solution: Ensure the virtual environment is activated.


---

### Steps Explained

1. **Install Dependencies:** The `requirements.txt` file ensures all the required Python libraries are installed.
2. **Run Tests:** Users can run tests easily with a single command (`pytest`) or generate an HTML report with options.
3. **Parallel Execution:** `pytest-xdist` boosts efficiency by running tests in parallel.
4. **Assumptions:** Helps users understand the limitations and expected setup.

Let me know if you need further help!
