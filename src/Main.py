import yfinance as yf

stock = yf.Ticker("DVAX")

#print(str(tsla.info))
info = stock.info

for item in info:
    print(f"{item}: {info[item]}")

#tsla.actions

#tsla.splits

print(str(stock.options))

