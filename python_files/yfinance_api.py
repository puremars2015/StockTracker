import yfinance as yf


stock = yf.Ticker("2330.TW")

# hist = stock.history(start="2022-05-10", end="2022-05-13", interval="30m")

# print(hist)

hist = stock.history(period="1d", interval="1m")

print(hist)