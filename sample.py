from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Run in headless mode
    service_log_path = "/tmp/geckodriver.log"
    driver = webdriver.Firefox(options=options, service_log_path=service_log_path)
    driver.get('http://www.google.com')
    print(driver.title)
    driver.quit()
except WebDriverException as e:
    print(f"WebDriverException: {e}")
    with open(service_log_path, 'r') as log_file:
        print(log_file.read())