#!/usr/bin/env python

"""
Script to scrape headlines from a news website using Selenium.

Requirements:
- ChromeDriver installed (https://sites.google.com/chromium.org/driver/)
- Selenium: pip install selenium
- BeautifulSoup: pip install beautifulsoup4
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def scrape_and_save_headlines(url, output_file='data/headlines.txt'):
    """
    Scrapes headlines from a given URL and saves them to a text file.

    Parameters:
    - url (str): The URL of the website containing headlines.
    - output_file (str): The path to the file to save headlines. Default is 'data/headlines.txt'.
    """
    # Get the absolute path of the current working directory
    current_directory = os.getcwd()

    # Create the full path to the desired output file
    output_path = os.path.join(current_directory, output_file)

    # Ensure to have ChromeDriver installed and provide the correct path
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Explicitly wait for the headlines to be present (adjust the timeout as needed)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//h3[contains(@class, "your-headline-class")]')))
    except Exception as e:
        print(f"Error waiting for headlines: {e}")

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    headlines = []

    # Extract all text from h3 elements on the page
    for headline in soup.find_all('h3'):
        headlines.append(headline.text.strip())

    driver.quit()

    # Ensure the 'media/data' folders exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save headlines to a text file within the 'media/data' folder
    with open(output_path, 'w', encoding='utf-8') as file:
        for headline in headlines:
            file.write(headline + '\n')

    print(f"Headlines saved to {output_path}")


# URL of the news website
news_url = 'https://www.wsj.com/politics/elections'

# Call the function to scrape headlines and save to 'media/data/headlines.txt'
scrape_and_save_headlines(news_url)
