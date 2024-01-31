import os  #導入os模組
import asyncio  #導入asyncio模組
import discord  #導入discord.py模組
from discord.ext import commands  #導入指令模組

bot_token = os.environ['Discord_Bot_Token']  #定義bot token

intents = discord.Intents.all() #要求機器人權限
bot = commands.Bot(command_prefix = "/", intents = intents) #定義機器人實體與指令前綴

@bot.event #機器人上線訊息
async def on_ready():
    print(f'登入身分為---> {bot.user}')

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(bot_token)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())