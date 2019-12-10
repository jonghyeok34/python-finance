import matplotlib.pyplot as plt
from matplotlib import style
# date open high low close
from mpl_finance import candlestick_ohlc 
import matplotlib.dates as mdates
import pandas as pd

'''

'''
style.use('ggplot')

# visualizing data
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


# resample - average value - open high low close
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

# map date to mdate number()
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc.head())

# price 
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
# ax2 - volume
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.xaxis_date()
# axis - ax1/ data: df_ohlc.values, width=2(thickness of cadnel), 
# colorup='g' - green=up/ red=down
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
# x: date ,y: volume
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()