from pandas_datareader.stooq import StooqDailyReader
from datetime import datetime

start = datetime(2020, 7, 1)
end = datetime(2022, 8, 1)
brand = '9984.JP'

stooq = StooqDailyReader(brand, start=start, end=end)
data = stooq.read()  # pandas.core.frame.DataFrame
data.to_csv(brand + ".csv", encoding="utf-8")
print('finish')