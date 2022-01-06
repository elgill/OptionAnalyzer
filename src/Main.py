import yfinance as yf

stock = yf.Ticker("DVAX")


def printStockInfo(ticker):
    info = ticker.info
    for item in info:
        print(f"{item}: {info[item]}")

def printOptionDates(ticker):
    print(str(ticker.options))

def printNewsInfo(ticker):
    news=ticker.news
    for article in news:
        for attr in article:
            print(f"{attr}: {article[attr]}")
        print("")