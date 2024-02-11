# app.py

from flask import Flask, render_template, request
from fetch_data import fetch_stock_data
from visualizations import create_visualizations

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # Default symbol
    default_symbol = 'AAPL'
    
    # Get symbol from form submission or use default
    symbol = request.form.get('symbol', default_symbol).upper() if request.method == 'POST' else default_symbol
    
    # Fetch stock data for the provided symbol
    stock_data = fetch_stock_data(symbol)
    
    # Check if stock_data is valid
    if stock_data is None:
        error_message = f"Failed to fetch data for symbol: {symbol}. Please try again with a different symbol."
        return render_template('index.html', error_message=error_message, symbol=symbol)
    
    # Create visualizations and save the plot to a file
    plot_html = create_visualizations(stock_data)
    
    # Render the template with the stock data and plot file
    return render_template('index.html', plot_html=plot_html, symbol=symbol)

if __name__ == '__main__':
    app.run(debug=True)
