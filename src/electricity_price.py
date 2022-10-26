import typing as t

import requests as r
from bs4 import BeautifulSoup

from exceptions import ApiIsUnreachable, DataFetchingFailed

URL: str = 'https://www.globalpetrolprices.com/Poland/electricity_prices/'


def get_electricity_price() -> t.Dict:
    resp = r.get(url=URL)

    if resp.status_code != 200:
        raise ApiIsUnreachable()

    soup = BeautifulSoup(resp.content, "html.parser")

    table = soup.find_all('table')[0]
    scraped_data = []
    for table_data in table.find_all('tr'):
        for data in table_data.find_all('td'):
            scraped_data.append(data.text.strip())

    try:
        price = float(scraped_data[2])
        unit = scraped_data[1][-3:]
    except ValueError:
        raise DataFetchingFailed()
    return {'value': price, 'unit': unit, 'currency': 'PLN'}


def get_electricity_price_mock() -> t.Dict:
    return {'value': 0.790, 'unit': 'kWh', 'currency': 'PLN'}
