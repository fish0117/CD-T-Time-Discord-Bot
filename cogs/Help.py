import discord
from discord.ext import commands
from discord import app_commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="help", 
        description="指令列表"
    )
    async def help(
        self, 
        interaction: discord.Interaction
    ):
        help_embed=discord.Embed(
            title="指令列表", 
            color=0xffcec7
        )
        help_embed.add_field(
            name="/tourguide", 
            value="基礎功能社群導覽與故事背景", 
            inline=False
        )
        help_embed.add_field(
            name="/help", 
            value="機器人使用方法與指令列表", 
            inline=False
        )
        help_embed.add_field(
            name="/profile", 
            value="查詢玩家個人檔案與積分(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/news", 
            value="機器人更新&新副本開放訊息(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/signin", 
            value="每日簽到獲得獎勵(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/shop", 
            value="小海豹商店(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/question", 
            value="在討論串中提出問題(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/answer", 
            value="在討論串中回答問題(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/reply", 
            value="在討論串中回覆問題(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/summary", 
            value="總結某個討論串的問題(開發中)", 
            inline=False
        )
        help_embed.add_field(
            name="/task", 
            value="進入RPG遊戲系統&選擇任務", 
            inline=False
        )
        help_embed.set_footer(
            text="使用/tourguide獲取社群指令使用教學"
        )

        info_view = discord.ui.View()
        info_view.add_item(
            discord.ui.Button(
                label="Github Repo", 
                url="https://github.com/fish0117/CD-T-Time-Discord-Bot"
            )
        )
        info_view.add_item(
            discord.ui.Button(
                label="HackMD 共筆", 
                url="https://hackmd.io/@ATM_R5IeQ8aBci8yu46Jjw/Bk1ag0_H6"
            )
        )
        await interaction.response.send_message(
            embed=help_embed, 
            view=info_view
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
