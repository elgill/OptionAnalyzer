# This file is temporary to get a feel for the API, and see how to best structure this project
import yfinance as yf

stock = yf.Ticker("DVAX")


def printStockInfo(ticker):
    info = ticker.info
    for item in info:
        print(f"{item}: {info[item]}")

def printOptionDates(ticker):
    # TODO: Manipulate data from DataFrame to more usable
    print(str())
    for date in ticker.options:
        chain=ticker.option_chain(date)
        print(chain.calls)
        #print(str(chain.puts))

def printNewsInfo(ticker):
    news=ticker.news
    for article in news:
        for attr in article:
            print(f"{attr}: {article[attr]}")
        print("")

printOptionDates(stock)