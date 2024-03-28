import yfinance as yf

# Get all ticker symbols from Yahoo Finance
ticker_list = yf.Tickers()

# Extract symbols as a list
ticker_symbols = ticker_list.tickers.keys()

print(list(ticker_list))