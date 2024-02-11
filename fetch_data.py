# fetch_data.py

import datetime
import requests
import pandas as pd

# Alpha Vantage API Key (replace with your own key)
API_KEY = 'ASHUTLCIZXEF9IRU'

# Function to fetch historical stock data
def fetch_stock_data(symbol, interval='daily', output_size='full'):
    base_url = 'https://www.alphavantage.co/query'
    
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': output_size,
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        time_series_key = 'Time Series (1min)' if interval == 'intraday' else 'Time Series (Daily)'
        try:
            stock_data = pd.DataFrame(data[time_series_key]).T
            stock_data.index = pd.to_datetime(stock_data.index)
            last_365_days = datetime.datetime.now() - datetime.timedelta(days=365)
            stock_data = stock_data[stock_data.index >= last_365_days]
            return stock_data
        except KeyError as e:
            print(f"Error: {e}. Check the structure of the returned data.")
            return None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
