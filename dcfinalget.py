#Sam Meyer

import requests as req
from bs4 import BeautifulSoup

resp = req.get("https://www.google.com/maps/search/gas/@43.0316191,-88.0216753,15z/data=!3m1!4b1")

#print(resp.content)

soup = BeautifulSoup(resp.text, 'html.parser')

print(soup.prettify())
