import discord
from discord.ext import commands
from discord import app_commands


class Profile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="profile", description="顯示您的個人資料")
    async def profile(self, interaction: discord.Interaction):
        user = interaction.user
        embed = discord.Embed(title="個人資料", color=user.color)
        embed.set_thumbnail(url=user.avatar)
        embed.description = f"用戶名稱：{user.name}"
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Profile(bot))
