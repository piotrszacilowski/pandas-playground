import datetime

import pandas as pd

from electricity_price import get_electricity_price_mock
import exceptions as exc

# spreadsheet = pd.read_csv("../data/photovoltaics-2021.xls", engine='python')
df = pd.read_excel(
    io='../data/photovoltaics-2021.xls',

)

electricity_price = get_electricity_price_mock()['value']
# 16:3 to 16:14

print(df)
df = df.drop(df.columns[[0, 1, 2]], axis=1)  # df.columns is zero-based pd.Index
print(df)
df = df.loc[15:16, :]

# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )
#
# print(df)
# print('-' * 9)
# print(df['Age'].max())
# print(df['Age'][0])
# print(type(df['Age']))


def determine_month_from_number(month_integer: int) -> str:
    if month_integer in range(1, 12):
        return datetime.date(1900, month_integer, 1).strftime('%B')
    raise exc.IncorrectMonthValue('Incorrect value of the month. It should be between 1 and 12')
