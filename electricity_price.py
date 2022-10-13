import requests as r

from bs4 import BeautifulSoup
import pandas as pd

# API to get current price for kWh
# https://www.globalpetrolprices.com/Poland/electricity_prices/
# https://www.globalpetrolprices.com/data_access.php


URL = "https://www.globalpetrolprices.com/Poland/electricity_prices/"
page = r.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find_all('table')[0]

n = 0
for i in table.children:
    print(i)
    n += 1
    print(f'---- {n} ----')


# print(table)

# dfs = pd.read_html(URL)

