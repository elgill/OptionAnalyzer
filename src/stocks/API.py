# This file is temporary?(or maybe not now) to get a feel for the API, and see how to best structure this project
import yfinance as yf

#----------------------------------------------------------------#
#   NAME: getTicker
#   DESCRIPTION: Function to gather yfinance Object
#   PARAMS: symbol - String representing Ticker symbol
#   RETURN: yfinance Ticker object
#----------------------------------------------------------------#
def getTicker(symbol):
    return yf.Ticker(symbol)

#----------------------------------------------------------------#
#   NAME: getInfo
#   DESCRIPTION: Function to gather information about a yfinance Object
#   PARAMS: ticker - yfinance Ticker object
#   RETURN: Info about stock from API in a dictionary
#----------------------------------------------------------------#
def getInfo(ticker):
    return ticker.info

#----------------------------------------------------------------#
#   NAME: getOptionDates
#   DESCRIPTION: Function to gather list of option dates
#   PARAMS: ticker - yfinance Ticker object
#   RETURN: An array of option dates/symbols
#----------------------------------------------------------------#
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