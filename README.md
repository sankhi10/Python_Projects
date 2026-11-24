# Playwright Python Test Automation Framework
---
This test automation framework built with **Playwright** and **Python**, implementing industry best practices including Page Object Model, parallel execution, and CI/CD integration.


### Key Features
---

| Feature | Description |
|---------|-------------|
| Page Object Model	| Clean separation of test logic and page interactions |
| Multi-Browser |	Chromium, Firefox, WebKit support |
|Parallel Execution	| pytest-xdist for faster test runs |
| CI/CD Ready |	GitHub Actions workflow included |
| Rich Reporting |	Allure reports, HTML reports, screenshots, videos |
| Data-Driven |	JSON, YAML test data support |
| Type Hints |	Full annotations for IDE support |


### Project Structure
---



### Quick Start
---


### Running Tests
---
> #Run all test
'''pytest
'''

>#Run specific markers
pytest -m smoke
pytest -m regression

>Run specific test
pytest test_login.py
pytest est/test_login.py
pytest -k test_add_item

>Run in specific browser
pytest --browser webkit

>Run in headed mode
pytest --headed

>Run tests in parallel
pytest --numprocesses 2 
(assuming pytest-xdist is installed)


### Configuration
---



### Writing Tests
---



### Reports
---
| Report Type | Location |
|-------------|----------|
| HTML Report | reports/html/report.html |
| Allure Report | reports/allure-results/ |
| Logs | logs/test_execution.log |


### CI/CD
---
