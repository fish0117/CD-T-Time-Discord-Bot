import discord
from discord.ext import commands
from discord import app_commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="help", 
        description="本功能目前還在開發中~"
    )
    async def question(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "本功能目前還在開發中~"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
