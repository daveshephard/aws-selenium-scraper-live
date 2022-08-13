import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#AUTONATION_START_LINK = 'https://www.pro-football-reference.com/players/'
AUTONATION_START_LINK = 'https://www.autonation.com/cars-for-sale?cnd=new&pagesize=72&dst=100&zip=98155'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_listings(driver):
  driver.get(AUTONATION_START_LINK)
  driver.implicitly_wait(30)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
  
  print('Fetching listings')
  listings = get_listings(driver)
  
  print(f'Found {len(listings)} listings')
  print('Parsing the links on the first page')
  listings_data = [parse_listing(listing) for listing in listings]
  
  
  print('Save the data to a CSV')
  listings_df = pd.DataFrame(listings_data)
  print(listings_df)
  listings_df.to_csv('listings.csv')




  


##srp-tile-vehiclename-0
#find_element(By.ID, "id")
#find_element(By.NAME, "name")
#find_element(By.XPATH, "xpath")
#find_element(By.LINK_TEXT, "link text")
#find_element(By.PARTIAL_LINK_TEXT, "partial link text")
#find_element(By.TAG_NAME, "tag name")
#find_element(By.CLASS_NAME, "class name")
#find_element(By.CSS_SELECTOR, "css selector")