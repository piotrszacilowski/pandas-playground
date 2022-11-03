import datetime

import pandas as pd

from tabulate import tabulate

from electricity_price import get_electricity_price_mock
import exceptions as exc


def determine_month_from_number(month_integer: int) -> str:
    if month_integer in range(1, 12):
        return datetime.date(1900, month_integer, 1).strftime('%B')
    raise exc.IncorrectMonthValue('Incorrect value of the month. It should be between 1 and 12')


def set_first_row_as_header(data_frame: pd.DataFrame):
    new_header = data_frame.iloc[0]  # get the first row for the header
    data_frame = data_frame[1:]  # take the data less the header row
    data_frame.columns = new_header  # set the header row as the df header
    return data_frame


df = pd.read_excel(
    io='../data/photovoltaics-2021.xls',
)

electricity_price = get_electricity_price_mock()['value']

df = df.drop(df.columns[[0, 1, 2]], axis=1)  # df.columns is zero-based pd.Index
df = df.loc[15:16, :]
df = set_first_row_as_header(data_frame=df)

print(tabulate(df, headers='keys', tablefmt='psql'))
