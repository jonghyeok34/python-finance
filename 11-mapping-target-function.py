from collections import Counter

import numpy as np
import pandas as pd
import pickle

def process_data_for_labels(ticker : str):
    hm_days : int = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    # print(tickers)
    df.fillna(0, inplace=True)

    for i in range(1, hm_days +1):
        # price change from i days ago
        df[f'{ticker}_{i}d'] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df


def buy_sell_hold(*args):
    '''buy if or sell by % change
    :param args:
    :return:
    '''
    cols = [c for c in args]
    requirements = 0.02
    for col in cols:
        # if change is more than 2%
        if col > requirements:
            return 1
        # if change is less than -2%
        if col < -requirements:
            return -1
    return 0


def extract_feature_sets(ticker):
    tickers, df = process_data_for_labels(ticker)
    hm_days = 7
    df[f'{ticker}_target'] = list(map(buy_sell_hold, *[df[f'{ticker}_{i}d'] for i in range(1, hm_days+1)]))
    vals = df[f'{ticker}_target'].values.tolist()
    str_vals = [str(i) for i in vals]

    # get counts by number
    print(f'Data spread:{Counter(str_vals)}')

    df.fillna(0, inplace=True)

    # replace infinity to NaN
    df = df.replace([np.inf, -np.inf], np.nan)
    # drop NaN
    df.dropna(inplace=True)

    # normalize get percentage changes from right before data
    df_vals = df[[ticker for ticker in tickers]].pct_change()

    # replace infinity to 0
    df_vals = df_vals.replace([np.inf, -np.inf], 0)

    x = df_vals.values

    y = df[f'{ticker}_target'].values

    return x, y, df

if __name__ == '__main__':
    extract_feature_sets("XOM")