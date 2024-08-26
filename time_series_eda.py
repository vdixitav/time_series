# -*- coding: utf-8 -*-
"""Time Series EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p-P4H55eqTLUIK_OpiypwYvAv5Loyl44
"""

# INSTALL panda data reader

! pip install pandas-datareader
!pip install yfinance

import pandas_datareader as pdr
import pandas as pd
from datetime import datetime
import yfinance as yf

!pip install yfinance
import pandas_datareader as pdr
import pandas as pd
from datetime import datetime
import yfinance as yf

# Now try fetching the data again
df_tesla = yf.download('TSLA')  # No need for pdr_override()
print(df_tesla.head())

df_tesla.plot()

df_tesla['High'].plot(figsize=(12,4))

## xlimit and y limit

df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],figsize=(12,4))

df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,800],figsize=(12,4))

df_tesla['High'].plot(xlim=['2022-01-01','2024-08-01'],figsize=(12,4)) # date changes as letest

df_tesla['High'].plot(xlim=['2022-01-01','2024-08-01'],ylim=[0,800],figsize=(12,4))

df_tesla.index

df_tesla.head(4) # used for whole data,but we are considering timeline for that see nect line code

df_tesla.loc['2020-01-01':'2021-09-01'] # watch the time line// try for new time line

index=df_tesla.loc['2020-01-01':'2021-09-01'].index
share_open=df_tesla.loc['2020-01-01':'2021-09-01']['Open']

share_open

from io import IncrementalNewlineDecoder
import matplotlib.pyplot as plt

figure,axis=plt.subplots()
#plt.tight_layout()
figure.autofmt_xdate
axis.plot(index,share_open)

# Dtae time index

df_tesla.reset_index()

df_tesla.info()

#pd.to_datetime(df_tesla['Date']) if date in object format instead of int

## Datetime

from datetime import datetime

date=datetime(2021,11,21)

datetime.now()

def add_num(num1,num2):
  return num1+num2

num1=20
num2=30
for i in[1,2,3,4,5]:
  print(add_num(num1,num2))
start_time=datetime.now()
add_num(num1,num2)
end_time=datetime.now()
print(end_time-start_time)

date

date.day

date.weekday()

date.year



"""# Time Resampling"""

df_tesla.head()

# Year end
df_tesla.resample(rule='A')

df_tesla.resample(rule='A').min()

df_tesla.resample(rule='A').max()

df_tesla.resample(rule='A').max()['Open'].plot()

# Quaterly strt frequency
df_tesla.resample(rule='QS').max()['High'].plot()

##Business end frequncy

df_tesla.resample(rule='BA').max()

df_tesla.resample(rule='BA').max()['High'].plot()

df_tesla.resample(rule='BQS').max()

df_tesla.resample(rule='BA').mean().plot(kind='bar')

df_tesla['High'].rolling(10).mean().head(20)

df_tesla['Open:30 days rolling']=df_tesla['Open'].rolling(30).mean()

df_tesla.head(31)

df_tesla[['Open','Open:30 days rolling']].plot(figsize=(12,5))
plt.show()

