import discord
from discord.ext import commands

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("你好~我是可愛的小蘑菇:)")

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "嘿蘑菇":
            await message.channel.send(f'{message.author.mention}找我有事？')

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))