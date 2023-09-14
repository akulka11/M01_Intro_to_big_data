import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


faculty_directory_url = "https://cs.illinois.edu/about/people/all-faculty"

webdriver_path = "/opt/homebrew/bin/chromedriver"  # Replace with your actual path


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_service = ChromeService(webdriver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


driver.get(faculty_directory_url)
time.sleep(5) 


while True:
    try:
        load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
        if load_more_button.is_displayed():
            load_more_button.click()
            time.sleep(5) 
        else:
            break
    except Exception as e:
        break


soup = BeautifulSoup(driver.page_source, 'html.parser')


faculty_listings = soup.find_all(class_="faculty-listing") 


faculty_homepage_urls = []
faculty_bios = []
courses_taught = []


for faculty_listing in faculty_listings:
    # Extract faculty homepage URL
    faculty_homepage_url = faculty_listing.find('a')['href']
    faculty_homepage_urls.append(faculty_homepage_url)


    driver.get(faculty_homepage_url)
    time.sleep(5)  


    faculty_homepage_soup = BeautifulSoup(driver.page_source, 'html.parser')


    faculty_bio = faculty_homepage_soup.find(class_="faculty-bio")  
    if faculty_bio:
        faculty_bios.append(faculty_bio.get_text())


    courses_taught_element = faculty_homepage_soup.find(class_="courses-taught")  
    if courses_taught_element:
        courses_taught.append(courses_taught_element.get_text())


with open("bio_urls.txt", "w") as bio_urls_file:
    bio_urls_file.write("\n".join(faculty_homepage_urls))

with open("bios.txt", "w") as bios_file:
    bios_file.write("\n".join(faculty_bios))

with open("courses_taught.txt", "w") as courses_taught_file:
    courses_taught_file.write("\n".join(courses_taught))


driver.quit()
