import os
import datetime

from discord.ext import commands
from dotenv import load_dotenv

import stocks.API as api

# Load environment variable with discord API key
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

#----------------------------------------------------------------#
#   NAME: sanitizeMessage
#   DESCRIPTION: Ensure message is safe to send
#   PARAMS: message - string to sanitize
#   RETURN: Sanitized string
#----------------------------------------------------------------#
def sanitizeMessage(message):
    return message[0:1999]

@bot.command(name='stock', help='Returns Stock information')
async def cmd_stock(ctx,arg):
    await ctx.send("Let me get that for you..")
    #arg=str(arg)
    ticker=api.getTicker(arg)
    tickerInfo=api.getInfo(ticker)
    
    price="${:,.2f}".format(tickerInfo['regularMarketPrice'])
    prevClose="${:,.2f}".format(tickerInfo['previousClose'])
    open="${:,.2f}".format(tickerInfo['open'])
    
    response = f"Ticker: {arg}"
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

#----------------------------------------------------------------#
#   NAME: cmd_option
#   DESCRIPTION: Placeholder text
#   PARAMS: ctx
#           arg
#           arg2
#   RETURN: None
#----------------------------------------------------------------#
@bot.command(name='option', help='Returns info about options')
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