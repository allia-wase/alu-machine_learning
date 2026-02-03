#!/usr/bin/env python3
"""Fill missing data points in a pandas DataFrame.

- The column Weighted_Price is removed.
- Missing values in Close are set to the previous row value.
- Missing values in High, Low, Open are set to the same row's Close value.
- Missing values in Volume_(BTC) and Volume_(Currency) are set to 0.
"""

import pandas as pd


from_file = __import__("2-from_file").from_file

df = from_file("coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv", ",")

df = df.drop(columns=['Weighted_Price'])

df['Close'] = df['Close'].fillna(method='ffill')

df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])

df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

print(df.head())
print(df.tail())
