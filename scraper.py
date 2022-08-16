import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#AUTONATION_START_LINK = 'https://www.pro-football-reference.com/players/'
AUTONATION_START_LINK = 'https://www.autonation.com/cars-for-sale?cnd=new&pagesize=72&zip=30501&dst=200&mk=jeep'
#AUTONATION_START_LINK = 'https://www.autonation.com/cars-for-sale?cnd=new&pagesize=72&zip=30501'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def lazy_load_all_pages(driver):
  
  num_listings = 0  
  driver.get(AUTONATION_START_LINK)  
  driver.implicitly_wait(300)
  time.sleep(5)

  #//*[@id="cookieModal"]/div[3]/button
  if driver.find_element(By.XPATH, '//*[@id="cookieModal"]/div[3]/button'):
    print ('Element exists')
    driver.find_element(By.XPATH, '//*[@id="cookieModal"]/div[3]/button').click()
  
    
  try:
    element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//label[@id="lbl-srp-results-count-component"]')))
    print("Page is ready!")
  except TimeoutException:
    print("Loading took too much time!")
    
  num_listings = driver.find_element(By.XPATH, '//label[@id="lbl-srp-results-count-component"]').get_attribute("innerText")
  print(num_listings)
  
  num_listings = re.search('(([\d]+\,\d\d\d)|[\d]+)', num_listings).group()
  print('new listings: ',num_listings)

  if "," in num_listings:
    print('comma')
    num_listings = int(num_listings.replace(',', ''))
    print (num_listings)
  else:
    print('no comma')
    num_listings = int(num_listings)
    print(num_listings)
  
  loops = math.ceil(int(num_listings)/72)
  
  print("inside: ",num_listings)
  
  for x in range(1,loops):
    print("loop", x, " times")
    #click //button[@class="btn secondary-cta an-cta"]  
    
    try:
      WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="btn secondary-cta an-cta"]')))
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      print("Next button is ready!", x)
      submit_button = driver.find_element(By.XPATH, '//button[@class="btn secondary-cta an-cta"]')
      driver.execute_script("arguments[0].scrollIntoView();", submit_button)
      driver.execute_script("arguments[0].click();", submit_button)
      print('next button clicked', x)
    
    except TimeoutException:
      print("Loading took too much time!")
  
  return(num_listings)


def get_listings(driver):
  
  listings = driver.find_elements(By.XPATH, '//div[@class="tile-info"]')
  return listings

def parse_listing(listing):
  
  title =  listing.find_element(By.CLASS_NAME,"vehile-name")
  url = title.find_element(By.TAG_NAME,"a").get_attribute('href')
  
  return {
    'title': title.text,
    'url': url
  }
  

if __name__ == "__main__":
  
  print('Creating driver')
  driver = get_driver()
  lazy_load_all_pages(driver)
  
  print('Fetching listings')
  listings = get_listings(driver)
  print(f'Found {len(listings)} listings')
  print('Parsing the links on the first page')
  
  listings_data = [parse_listing(listing) for listing in listings]
  print('Save the data to a data frame')
  listings_df = pd.DataFrame(listings_data)
  print(listings_df)
 
# listings_df.to_csv('listings.csv')

  


##srp-tile-vehiclename-0
#find_element(By.ID, "id")
#find_element(By.NAME, "name")
#find_element(By.XPATH, "xpath")
#find_element(By.LINK_TEXT, "link text")
#find_element(By.PARTIAL_LINK_TEXT, "partial link text")
#find_element(By.TAG_NAME, "tag name")
#find_element(By.CLASS_NAME, "class name")
#find_element(By.CSS_SELECTOR, "css selector")