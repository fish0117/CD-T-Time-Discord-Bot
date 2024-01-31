import os  #導入os模組
import discord  #導入discord.py模組
from discord.ext import commands  #導入指令模組
bot_token = os.environ['Discord_Bot_Token']  #定義bot token

intents = discord.Intents.all() #要求機器人權限
bot = commands.Bot(command_prefix = "/", intents = intents) #定義機器人實體與指令前綴

@bot.event #機器人上線訊息
async def on_ready():
    print(f'登入身分為---> {bot.user}')

@bot.command()
async def hello(ctx): #發送hello訊息
  
    await ctx.send('你好~我是可愛的小蘑菇:)')

bot.run(bot_token)