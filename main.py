import os  #導入os模組
import discord  #導入discord.py模組
from discord.ext import commands  #導入指令模組
bot_token = os.environ['Discord_Bot_Token']  #定義bot token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents) #定義機器人實體

@client.event #機器人上線訊息
async def on_ready():
    print(f'登入身分為---> {client.user}')

@client.event
async def on_message(message): #發送hello訊息
  
    if message.author == client.user:
        return #防止機器人陷入迴圈

    if message.content.startswith('/hello'):
        await message.channel.send('你好~我是可愛的小蘑菇:)')

client.run(bot_token)