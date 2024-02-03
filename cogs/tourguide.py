import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional


class Tour(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="tourguide", description="歡迎新客人~讓小蘑菇帶你參觀一下吧!"
    )
    async def tourguide(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "歡迎新客人~讓小蘑菇帶你參觀一下吧!"
        )

    @app_commands.command(
        name="speaker", description="想說的話，讓小蘑菇替你大聲說出來:)"
    )
    @app_commands.describe(name="輸入人名", text="輸入要說的話")
    async def speaker(
        self, interaction: discord.Interaction, name: str, text: Optional[str] = None
    ):
        if text is None:
            text = "呱"
        await interaction.response.send_message(f"{name}說 「{text}」")


async def setup(bot: commands.Bot):
    await bot.add_cog(Tour(bot))
