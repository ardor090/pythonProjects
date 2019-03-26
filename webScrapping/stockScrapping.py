import pandas as pd
import pandas_datareader as pdr
import datetime as dt

download_source = r"C:\Users\Kenny\Desktop\download.xlsx"
start = dt.datetime(2000,1,1)
end = dt.datetime.today()

df = pdr.get_data_yahoo('AAPL', start, end)
# print(df.head())
print(df)
# df.to_excel(download_source)
