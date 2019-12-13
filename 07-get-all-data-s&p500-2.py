import bs4 as bs
import pickle
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import requests
from multiprocessing import Pool, freeze_support


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []

    for row in table.findAll('tr')[1:]:
        
        ticker = row.findAll('td')[0].text.replace('\n', "")
        tickers.append(ticker)

    with open('sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    
    print(tickers)
    return tickers


def worker(ticker):
    
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)    
    if not os.path.exists(f'stock_dfs/{ticker}.csv'):        
        df = web.DataReader(ticker, 'yahoo', start, end)
        df.to_csv(f'stock_dfs/{ticker}')
    else:
        print(f'Already have {ticker}')


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", 'rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    with Pool(8) as pool:
        pool.map(worker, tickers)
        
    print('the end')


def compile_data():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        if '.B' not in ticker:
            df = pd.read_csv(f'stock_dfs/{ticker}.csv')
            df.set_index('Date', inplace=True)

            df.rename(columns={'Adj Close': ticker}, inplace=True)
            df.drop(['Open', 'High', "Low", "Close", "Volume"], 1, inplace=True)

            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
            if count % 10 == 0:
                print(count)
        
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')


if __name__ == '__main__':
    freeze_support()
    # get_data_from_yahoo()
    compile_data()