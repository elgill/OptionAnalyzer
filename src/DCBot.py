import os
import datetime

from discord.ext import commands
from dotenv import load_dotenv

import stocks.API as api


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def sanitizeMessage(message):
    return message[0:1999]

@bot.command(name='stock', help='Stonks?')
async def cmd_stock(ctx,arg):
    await ctx.send("Let me get that for you..")
    arg=str(arg)
    ticker=api.getTicker(arg)
    tickerInfo=api.getInfo(ticker)
    response = f"Ticker: {arg}"
    price=tickerInfo['regularMarketPrice']
    price="${:,.2f}".format(price)
    prevClose=tickerInfo['previousClose']
    prevClose="${:,.2f}".format(prevClose)
    open=tickerInfo['open']
    open="${:,.2f}".format(open)
    response+= f"\nMarket Price: {price}"
    response+= f"\nPrevious Close: {prevClose}"
    response+= f"\nOpen: {open}"
    await ctx.send(sanitizeMessage(response))
    response=""
    maxArticles=4
    cnt=1
    for article in api.getNews(ticker):
        cnt+=1
        if (cnt>maxArticles):
            break
        response=f"`{article['title']}`"
        response+=f"\n<{article['link']}>"
        articleDate=datetime.datetime.fromtimestamp(article['providerPublishTime'])
        articleDate=articleDate.strftime('%A %b %d %I:%M %p')
        response+=f"\n{articleDate}"
        
        await ctx.send(sanitizeMessage(response))

#arg2 can serve as optionname
@bot.command(name='option', help='Stonks?')
async def cmd_option(ctx,arg,arg2):
    arg=str(arg)
    ticker=api.getTicker(arg)
    if arg2 == "?":
        options=api.getOptionDates(ticker)
    else:
        options=api.getOptionChainByDate(ticker,arg2)
    response=f"{str(arg)}: {str(options)}"
    await ctx.send(sanitizeMessage(response))

@bot.command(name='stop', help='Stops?')
async def cmd_stop(ctx):
    await ctx.send("Stopping.. ")
    exit()

bot.run(TOKEN)