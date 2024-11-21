from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
from backend.webScraping import driver


def configure_driver():
    """
    Configures the Selenium WebDriver.
    """
    return driver


def search_businesses(search_term, max_scrolls):
    """
    Searches for businesses on Google Maps and returns a list of URLs.

    Args:
        search_term (str): The term to search for.
        max_scrolls (int): Maximum number of scrolls to load more results.

    Returns:
        list: List of business URLs.
    """
    try:
        driver.get("https://www.google.com/maps/")

        # Wait for the search field and perform the search
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#searchboxinput'))
        )
        search_field.send_keys(search_term)
        search_field.send_keys(Keys.ENTER)

        # Wait for the side panel to load
        side_panel = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                "div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd"
            ))
        )

        # Scroll down to load more results
        for _ in range(max_scrolls):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", side_panel)
            time.sleep(2)

        # Find all business elements
        business_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'Nv2PK')]")

        print(f"Businesses found: {len(business_elements)}")
        business_urls = []

        for element in business_elements:
            try:
                link = element.find_elements(By.TAG_NAME, 'a')[-1].get_attribute('href')
                business_urls.append(link)
            except Exception as e:
                print(f"Error processing a business: {e}")
                continue

        return business_urls

    except Exception as e:
        print(f"Error during search: {e}")
        return []


def scrape_business_details(urls):
    """
    Scrapes business details from Google Maps.

    Args:
        urls (list): List of URLs to scrape.

    Returns:
        list: List of dictionaries containing business details.
    """
    business_details = []

    for url in urls:
        try:
            print(f"Accessing URL: {url}")
            driver.get(url)

            # Wait for the page to load
            time.sleep(2)

            # Extract the business name
            try:
                business_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1'
                ).text
            except Exception as e:
                print(f"Error extracting business name: {e}")
                business_name = "Name not found"

            # Extract additional information
            try:
                info_elements = driver.find_elements(By.CLASS_NAME, 'CsEnBe')
                additional_info = [
                    element.get_attribute('href') if element.get_attribute('href') else element.text.split('\n')[1]
                    for element in info_elements
                ]
            except Exception as e:
                print(f"Error extracting additional info: {e}")
                additional_info = ["No information found"]

            business_details.append({
                "Name": business_name,
                "Details": additional_info
            })

        except Exception as e:
            print(f"Error processing URL {url}: {e}")

    return business_details


def fetch_business_data(search_term, max_scrolls):
    """
    Searches for businesses and fetches detailed information.

    Args:
        search_term (str): The term to search for.
        max_scrolls (int): Maximum number of scrolls to load more results.

    Returns:
        list: List of dictionaries containing business details.
    """
    try:
        urls = search_businesses(search_term, max_scrolls)
        return scrape_business_details(urls)
    except Exception as e:
        print(f"Error during data fetching: {e}")
        return []
