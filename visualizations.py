import plotly.graph_objects as go
import tkinter as tk

# Function to get screen width
def get_screen_width():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    root.destroy()
    return screen_width

# Function to create visualizations and save the plot to a file
def create_visualizations(stock_data):
    # Plotly: Interactive Candlestick Chart
    data = [go.Candlestick(
                x=stock_data.index,
                open=stock_data['1. open'],
                high=stock_data['2. high'],
                low=stock_data['3. low'],
                close=stock_data['4. close'])]
    
    # Get screen width
    screen_width = get_screen_width()
    
    padding = 50
    layout = go.Layout(
        autosize=False,
        width=screen_width - padding,  # Set width to screen width
        height=600,
        xaxis=go.layout.XAxis(linecolor="black", linewidth=1, mirror=True),
        yaxis=go.layout.YAxis(linecolor="black", linewidth=1, mirror=True),
        margin=go.layout.Margin(l=padding*2),
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(title="Interactive candlstick chart", xaxis_title='Date', yaxis_title='Stock Price')
    return fig.to_html(include_plotlyjs=False)
