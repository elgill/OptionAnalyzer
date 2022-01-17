import os
import random


from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='stock', help='Stonks?')
async def cmd_stock(ctx,arg):
    arg=str(arg)
    response = f"Stonks: {arg}"
    await ctx.send(response)

bot.run(TOKEN)