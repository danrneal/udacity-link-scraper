import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# urls should be of the following form:
# "https://classroom.udacity.com/courses/XXX/lessons/XXX/concepts/
LESSON_URLS = []


def main(lesson_urls):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    login(driver)
    links = []

    i = 0
    for lesson_url in lesson_urls:
        i += 1
        print(f"Retrieving concepts for lesson {i} of {len(lesson_urls)}")
        concept_urls = get_concepts(driver, lesson_url)
        j = 0
        for concept_url in concept_urls:
            j += 1
            print(
                f"Getting Udacity links for concept {j} of {len(concept_urls)}"
            )
            links = get_links(driver, concept_url, links)

    print(f"Found {len(links)} Udacity links:")
    for link in links:
        print(link)


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


def get_concepts(driver, lesson_url):
    """Gets all the concept urls for a given lesson

    Args:
        driver: A webdriver object used to navigate to the lesson page and
            retrieve the concept urls
        lesson_url: A str that represent the target lesson url

    Returns:
        concept_urls: A list of strs representing the retrieved concept urls
    """
    driver.get(lesson_url)
    time.sleep(5)
    concept_urls = []
    anchors = driver.find_elements_by_xpath("//a[@href]")
    for anchor in anchors:
        href = anchor.get_attribute("href").split('#')[0]
        if (
            href.startswith("https://classroom.udacity.com/")
            and href not in concept_urls
        ):
            concept_urls.append(href)
    print(f"Retrieved {len(concept_urls)} concepts")
    return concept_urls


def get_links(driver, concept_url, links):
    """Gets all the Udacity links in a given lesson

    Args:
        driver: A webdriver object used to navigate to the concept page and
            retrieve all the Udacity links
        concept_url: A str that represents the target concept url
        links: A list of strs representing Udacity links that have already been
            collected in the current search

    Returns:
        links: A list of strs representing all the previous and new links that
            have been collected in the current search
    """
    driver.get(concept_url)
    time.sleep(5)
    anchors = driver.find_elements_by_xpath("//a[@href]")
    for anchor in anchors:
        href = anchor.get_attribute("href").split('#')[0]
        if (
            "udacity" in href
            and not href.startswith("https://classroom.udacity.com/")
            and not href.startswith("mailto")
            and href not in links
        ):
            links.append(href)
    return links


if __name__ == "__main__":
    main(LESSON_URLS)
