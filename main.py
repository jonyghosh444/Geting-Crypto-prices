from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

t_body = doc.tbody
trs = t_body.contents

prices = {}

for tr in trs:
    name, price = tr.contents[2:4]
    currency_name = name.a.text
    currency_price = price.span.text

    prices[currency_name] = currency_price


print(prices)
