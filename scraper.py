import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    login(driver)


def login(driver):
    """Logs a udacity user in with their email and password

    Args:
        driver: A webdriver object used to log the user in
    """
    email = os.environ['UDACITY_EMAIL']
    password = os.environ['UDACITY_PASSWORD']
    print(f"Attempting to log in as {email}...")
    driver.get("https://classroom.udacity.com/")
    login_form = driver.find_elements_by_xpath("//input[@data-cy]")
    login_form[0].send_keys(os.environ['UDACITY_EMAIL'])
    login_form[1].send_keys(password)
    login_form[1].send_keys(Keys.ENTER)
    while "Sign In" in driver.page_source:
        time.sleep(0.5)
    print("Logged in successfully!")


if __name__ == "__main__":
    main()
