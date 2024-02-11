# app.py

import yfinance as yf
from flask import Flask, render_template, request
from fetch_data import fetch_stock_data
from visualizations import create_visualizations
import pandas as pd

app = Flask(__name__, template_folder='../templates')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # Default symbol
    default_symbol = 'AAPL'
    
    # Fetch the list of S&P 500 companies from Wikipedia
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_data = pd.read_html(url)
    sp500_companies = sp500_data[0]

    # Extract the ticker symbols
    sp500_tickers = sp500_companies['Symbol'].tolist()

    # Get symbol from form submission or use default
    symbol = request.form.get('symbol', default_symbol).upper() if request.method == 'POST' else default_symbol
    
    # Fetch stock data for the provided symbol
    stock_data = fetch_stock_data(symbol)
    
    # Check if stock_data is valid
    if stock_data is None:
        error_message = f"Failed to fetch data for symbol: {symbol}. Please try again with a different symbol."
        return render_template('index.html', error_message=error_message, symbol=symbol, tickers=sp500_tickers)
    
    # Create visualizations and save the plot to a file
    plot_html = create_visualizations(stock_data)
    
    # Render the template with the stock data and plot file
    return render_template('index.html', plot_html=plot_html, symbol=symbol, tickers=sp500_tickers)

if __name__ == '__main__':
    app.run(debug=True)
