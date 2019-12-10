import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
'''
manipulate data
'''
style.use('ggplot')

# visualizing data
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['30ma'] = df['Adj Close'].rolling(window=30, min_periods=0).mean()
df.dropna(inplace=True)  # drop na(not a number)

# print(df.head())

# grid - six rows, 1 column, (start row,column)
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
# sharex --> when x1 is zoomed, x2 is also zoomed
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)


# x: date - index, y: Adj close
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax1.plot(df.index, df['30ma'])
ax2.bar(df.index, df['Volume'])

plt.show()