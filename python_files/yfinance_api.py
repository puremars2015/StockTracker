import yfinance as yf


stock = yf.Ticker("2330.TW")

hist = stock.history(period="1m")