import pandas as pd

from electricity_price import fetch_data

spreadsheet = pd.read_csv("data/photovoltaics-2021.xls")
price = fetch_data()

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)
print('-' * 9)
print(df['Age'].max())
print(df['Age'][0])
print(type(df['Age']))

