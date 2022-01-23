import os
import random
import datetime


from discord.ext import commands
from dotenv import load_dotenv

import stocks.API as api


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

#arg2 can serve as optionname
@bot.command(name='stock', help='Stonks?')
async def cmd_stock(ctx,arg,arg2):
    await ctx.send("Let me get that for you..")
    arg=str(arg)
    ticker=api.getTicker(arg)
    tickerInfo=api.getInfo(ticker)
    response = f"Stonks: {arg}\n"
    response+= f"Market Price: {tickerInfo['regularMarketPrice']}"
    await ctx.send(response)
    response=""
    maxArticles=4
    cnt=1
    for article in api.getNews(ticker):
        cnt+=1
        if (cnt>maxArticles):
            break
        response=f"`{article['title']}`"
        response+=f"\n{article['link']}"
        response+=f"\n{datetime.datetime.fromtimestamp(article['providerPublishTime'])}"
        
        await ctx.send(response)
    await ctx.send(str(arg2))

@bot.command(name='stop', help='Stops?')
async def cmd_stock(ctx,arg,arg2):
    exit()
    pass
bot.run(TOKEN)