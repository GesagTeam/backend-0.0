from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def scrape_university_majors(url):
    # Setup Chrome options for guest mode
    chrome_options = Options()
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    chrome_options.add_argument("--guest")  # Open Chrome in guest mode
    chrome_options.add_argument("--disable-extensions")  # Disable extensions for a clean session

    # Initialize the WebDriver with ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the university programs page
    driver.get(url)
    time.sleep(2)  # Politeness: Add a 2-second delay after loading the page

    # Get the page source and close the browser
    page_source = driver.page_source
    driver.quit()

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the list of majors/programs
    majors = []

    # Example: Assuming majors are listed within <li> tags inside a <ul> or <div> with a specific class or id
    for li in soup.find_all('li'):
        major = li.text.strip()
        if major:
            majors.append(major)

    # Print the extracted majors
    print("List of Majors Offered:")
    for major in majors:
        print(f"- {major}")

    return majors

# URL of the page listing the majors at the University of Freiburg
majors_url = "http://www.uni-freiburg.de/study-programs"  # Replace with the actual URL where majors are listed

# Perform the scraping
majors_list = scrape_university_majors(majors_url)

# The scraped majors are printed to the terminal. You can also save them if needed.
