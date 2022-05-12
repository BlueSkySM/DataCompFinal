from ast import operator
from selenium import webdriver
from operator import itemgetter
from pprint import pprint


#opens a headless chrome browser to get html elements
chromedrive_path = './chromedriver'
driver = webdriver.Chrome(chromedrive_path)

url = "https://www.google.com/maps/search/gas/@43.0316191,-88.0216753,15z/data=!3m1!4b1"

driver.get(url)

content = driver.page_source

#these three variables are the classes that house the google map results
result_gas_station_name = driver.find_elements_by_class_name("NrDZNb")

result_address = driver.find_elements_by_class_name("W4Efsd")

#this was test code to try to get the exact span the address was in, in the interest of time I chose to just extract the text from the greater class instead

#result_address = driver.find_elements_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/span[2]/jsl/span[2]')
#print(result_address)
#//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]
#//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/span[2]/jsl/span[2]

result_gas_prices = driver.find_elements_by_class_name("ah5Ghc")

#this extracts the text contained within divs/spans inside of the classes 

name = [a.text for a in result_gas_station_name]
#print(name)

#as i mentioned before i had to extract the address from the class because it wouldn't let me extract the specific span. believe me. i tried. 
fulladdress = [a.text for a in result_address]
address = []
for i in fulladdress:

    if "Gas station ·" in i and "\n" not in i:
        address.append(i)

#print(address)

gas = [a.text for a in result_gas_prices]
#print(gas)

stations = {}

#dictionary, key is name of gas station + its address, value is price

for i, j, k in zip(name, address, gas):
    key = i + " " + j
    value = k
    stations[key] = value

#print(stations)

#sort gas prices

sortedprices = sorted(stations.values())

#print(sortedprices)

#create new dictionary of sorted gas prices

sortedstations = sorted(stations.items(), key = lambda x: x[1])

#pretty print output of final result

pprint(sortedstations)

driver.quit()
