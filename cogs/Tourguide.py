import asyncio
import discord
from discord.ext import commands
from discord import app_commands


class Intorduce(commands.Cog):
    def __init__(
      self, bot: commands.Bot
    ):
        self.bot = bot

    @app_commands.command(
        name="tourguide", 
        description="歡迎新客人~讓小蘑菇帶你參觀一下吧!"
    )
    async def tourguide(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "歡迎新客人~讓小蘑菇帶你參觀一下吧!"
        )
        await asyncio.sleep(2)

    @commands.Cog.listener()
    async def on_message(
        self, 
        message: discord.Message
    ):
        if message.content == "歡迎新客人~讓小蘑菇帶你參觀一下吧!":
            await message.channel.send(
              "### 序章"
            )
            await asyncio.sleep(2)
            await message.reply(
                "在未來，人們嚮往的虛擬世界已被開發到了近乎飽和的階段，但仍然存在漏洞，而人們也常利用這樣的弱點，散播謠言「病毒」。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "在這新的世代，人們總戴著通往虛擬遊戲的「頭盔」，他們稱之為「01」。雖說是頭盔，但其實並不像我們想像中的戴在頭上的、很笨重的那種，它只是一個小掛件，只要配戴耳朵上，按下開關便能連結到虛擬世界。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "人們將這樣的虛擬世界稱為「MF」。在這裡，可以找到所有你想要的答案，有點像現在的瀏覽器，但功能更為全面。每個人都可以在上面發文，回答問題，不過也確實存在著假訊息。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "近年來興起了享用下午茶的風潮，小鎮裡，人們每天下午都會自發性的舉辦下午茶會，一邊享用甜品，一邊聊著自己有興趣的話題。"
            )
            await message.reply(
              "如果你還在聽，請輸入!tourguide continue以繼續。"
            )


class Tuturial(commands.Cog):
  def __init__(
    self, bot: commands.Bot
  ):
      self.bot = bot

  @commands.Cog.listener()
  async def on_message(
      self, 
      message: discord.Message
  ):
      if message.content == "!tourguide continue":
          await message.channel.send(
            "### 功能教學"
          )

async def setup(bot: commands.Bot):
    await bot.add_cog(Intorduce(bot))
    await bot.add_cog(Tuturial(bot))