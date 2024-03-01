import asyncio
import os

import discord
from discord.ext import commands

bot_token = os.environ["Discord_Bot_Token"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
   slash = await bot.tree.sync()
   print(f"目前登入身份 --> {bot.user}")
   print(f"載入 {len(slash)} 個斜線指令")

@bot.event
async def on_member_join(member: discord.Member):
    print(f"歡迎{member.display_name}」假訊息糾察員的加入！在RPG遊戲頻道輸入`/tourguide`與小蘑菇互動吧！")

@bot.command()
async def load(ctx, extension):
   await bot.load_extension(f"cogs.{extension}")
   await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
   await bot.unload_extension(f"cogs.{extension}")
   await ctx.send(f"UnLoaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
   await bot.reload_extension(f"cogs.{extension}")
   await ctx.send(f"ReLoaded {extension} done.")

async def load_extensions():
   for filename in os.listdir("./cogs"):
       if filename.endswith(".py"):
           await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
   async with bot:
       await load_extensions()
       await bot.start(bot_token)

if __name__ == "__main__":
    asyncio.run(main())
