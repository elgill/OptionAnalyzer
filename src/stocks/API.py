# This file is temporary?(or maybe not now) to get a feel for the API, and see how to best structure this project
import yfinance as yf

#----------------------------------------------------------------#
#   NAME: getTicker
#   DESCRIPTION: Placeholder text
#   PARAMS: symbol - String representing Ticker symbol
#   RETURN: yfinance Ticker object
#----------------------------------------------------------------#
def getTicker(symbol):
    return yf.Ticker(symbol)

def getInfo(ticker):
    return ticker.info

def getOptionDates(ticker):
    return ticker.options

def getOptionChainByDate(ticker,date):
    # TODO: Manipulate data from DataFrame to more usable
    return ticker.option_chain(date)

def getNews(ticker):
    return ticker.news

def printStockInfo(ticker):
    info = ticker.info
    for item in info:
        print(f"{item}: {info[item]}")

def printOptionDates(ticker):
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