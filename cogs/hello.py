import discord
from discord.ext import commands
from discord import app_commands

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # hello指令
    @app_commands.command(name = "hello", description = "讓小蘑菇出來打招呼~")
    async def tourguide(self, interaction: discord.Interaction):
        # 回覆使用者的訊息
        await interaction.response.send_message("你好~我是可愛的小蘑菇:)")

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "嘿蘑菇":
            await message.channel.send(f'{message.author.mention}老闆~今天的工資麻煩打我帳戶上:)')

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))