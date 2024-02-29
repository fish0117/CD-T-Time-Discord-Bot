import asyncio
import os

import discord
from discord.ext import commands
from discord import app_commands
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

dburi = "mongodb+srv://CDTTimeDiscordBot:" + os.environ["MongoDB_Password"] + "@cd-t-time.2g0xg5g.mongodb.net/?retryWrites=true&w=majority&appName=CD-T-Time"
db_client = MongoClient(dburi, server_api=ServerApi('1'))
db = db_client["CD-T-Time"]
db_col = db["User-Data"]


class Communicate(commands.Cog):
    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @app_commands.command(
        name="question", 
        description="本功能目前還在開發中~"
    )
    async def question(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "本功能目前還在開發中~"
        )

    @app_commands.command(
        name="reply", 
        description="本功能目前還在開發中~"
    )
    async def reply(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "本功能目前還在開發中~"
        )

    @app_commands.command(
        name="answer", 
        description="本功能目前還在開發中~"
    )
    async def answer(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "本功能目前還在開發中~"
        )

    @app_commands.command(
        name="summary", 
        description="本功能目前還在開發中~"
    )
    async def summary(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "本功能目前還在開發中~"
        )


class QuestionModal(
    discord.ui.Modal, 
    title="試著提出你第一個問題吧"
):
    question = discord.ui.TextInput(label="你的問題", required=True)

    async def question_submit(
        self, 
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            f"{self.question.value}"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Communicate(bot))