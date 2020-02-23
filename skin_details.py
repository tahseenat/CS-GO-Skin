import requests


def get_src(name):
    api_url = "https://csgoempire.com/api/v2/inventory/site/10"
    r = requests.get(api_url).json()
    details = []
    for i in range(len(r)):
        if r[i]["appid"] == 570:
            details.append(r[i])
    price = 10000000
    src = "na"
    name = name
    for i in range(len(details)):
        if details[i]["name"].lower() == name.lower():
            if details[i]["market_value"] < price:
                price = details[i]["market_value"]
                src = details[i]['icon_url']
    # print(price / 100, '\n', src)
    return src
