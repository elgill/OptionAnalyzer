import os
import random


from discord.ext import commands
from dotenv import load_dotenv

import stocks.API as api


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='stock', help='Stonks?')
async def cmd_stock(ctx,arg):
    arg=str(arg)
    ticker=api.getTicker(arg)
    tickerInfo=api.getInfo(ticker)
    response = f"Stonks: {arg}\n"
    response+= f"Market Price: {tickerInfo['regularMarketPrice']}"
    await ctx.send(response)

bot.run(TOKEN)