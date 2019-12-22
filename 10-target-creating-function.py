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
        # price of 2days
        df[f'{ticker}_{i}d'] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df


def buy_sell_hold(*args):
    cols = [c for c in args]
    requirements = 0.02
    for col in cols:
        if col > requirements:
            return 1
        if col < -requirements:
            return -1
    return 0

if __name__ == '__main__':
    process_data_for_labels('AAPL')