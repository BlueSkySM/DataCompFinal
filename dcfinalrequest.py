import requests
import json
from pprint import pprint
r=requests.get("https://www.google.com/maps/search/gas/@43.0316191,-88.0216753,15z/data=!3m1!4b1")

txt = r.text

find1 = "window.APP_INITIALIZATION_STATE="
find2 = ";window.APP"

i1 = txt.find(find1)
i2 = txt.find(find2, i1+1 )
js = txt[i1+len(find1):i2]
data = json.loads(js)
pprint(data)