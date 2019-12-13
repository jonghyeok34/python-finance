import bs4 as bs
import pickle
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import requests
from multiprocessing import Pool, freeze_support, cpu_count

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        
        ticker = row.findAll('td')[0].text.replace('\n', "")
        tickers.append(ticker)

    with open('sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    
    print(tickers)
    return tickers


def worker(ticker):
    try:
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2019, 12, 11)    
        print(1)
        if not os.path.exists(f'stock_dfs/{ticker}.csv'):
            print(ticker)        
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv(f'stock_dfs/{ticker}.csv')
        else:
            print(f'Already have {ticker}')
    except Exception as e:
        print(e)


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", 'rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    cpu = cpu_count()
    pool = Pool(cpu-1) 
    r = pool.map_async(worker, tickers)
    pool.close()
    pool.join()
    print('the end')

if __name__ =='__main__':
    freeze_support()
    get_data_from_yahoo()