import imp
from selenium import webdriver

#from parsel import Selector

chromedrive_path = './chromedriver' # use the path to the driver you downloaded from previous steps
driver = webdriver.Chrome(chromedrive_path)

url = "https://www.google.com/maps/search/gas/@43.0316191,-88.0216753,15z/data=!3m1!4b1"

driver.get(url)

content = driver.page_source

gas_prices = driver.find_elements_by_class_name("ah5Ghc")

gas = [a.text for a in gas_prices]
print(gas)

driver.quit()
