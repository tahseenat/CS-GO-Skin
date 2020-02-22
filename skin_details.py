import json
from bs4 import BeautifulSoup
import requests

URL = "https://csgoempire.com/api/v2/inventory/site/10"
r = requests.get(URL).json()
print(r[0])

for i in range(len(r)):
    if r[i]["appid"]==570:
        print(r[i]["name"],"-------",r[i]["market_value"]/100)
