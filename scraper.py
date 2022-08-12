from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#AUTONATION_START_LINK = 'https://www.pro-football-reference.com/players/'
AUTONATION_START_LINK = 'https://www.autonation.com/cars-for-sale?cnd=new&pagesize=72'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()
  
  print('Fetching the page')
  driver.get(AUTONATION_START_LINK)
  print('Page title',driver.title)

  print('Get the car links')
  LISTING_A_CLASS = 'vehile-name'
  listing_divs = driver.find_elements(By.CLASS_NAME, LISTING_A_CLASS)
  print(f'Found {len(listing_divs)} listings')

  listing_links = driver.find_elements(By.XPATH, '//a[contains(@href,"/cars/")]')
  print(f'Found {len(listing_links)} links')
  print(listing_links)



##srp-tile-vehiclename-0
#find_element(By.ID, "id")
#find_element(By.NAME, "name")
#find_element(By.XPATH, "xpath")
#find_element(By.LINK_TEXT, "link text")
#find_element(By.PARTIAL_LINK_TEXT, "partial link text")
#find_element(By.TAG_NAME, "tag name")
#find_element(By.CLASS_NAME, "class name")
#find_element(By.CSS_SELECTOR, "css selector")