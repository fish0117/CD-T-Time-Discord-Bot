import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional


class Task(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="task", 
        description="接收每日任務資訊&進入RPG副本"
    )
    @app_commands.describe(
        task_num = "輸入任務編號"
    )
    async def task(
        self, 
        interaction: discord.Interaction, 
        task_num: Optional[str] = None
    ):
        if task_num is None:
            task_embed = discord.Embed(
                title="任務列表", 
                color=0xffcec7
            )
            task_embed.add_field(
                name="1.應對災難事件時的技巧／抵抗假訊息", 
                value="**花費行動點**：1點 **任務內容**：應對災難事件時的技巧／抵抗假訊息", 
                inline=False
            )
            task_embed.set_footer(
                text="使用/task <任務編號>來選擇進入任務"
            )
            await interaction.response.send_message(
                embed=task_embed
            )

        if task_num == "1":
            await interaction.response.send_message(
                "你選擇了任務1：應對災難事件時的技巧／抵抗假訊息"
            )

    @commands.Cog.listener()
    async def on_message(
        self, 
        message: discord.Message
    ):
        life_value = 3
        if message.content == "你選擇了任務1：應對災難事件時的技巧／抵抗假訊息" and message.author.bot:
            await asyncio.sleep(2)
            await message.reply(
               "和朋友結束下午茶後，回到家，一旁的01不斷響起提示音，一想到這可能是工作，你想也不想決定倒頭就睡。奈何你好奇得睡不著，便只打算偷瞄一眼……" 
            )
            await asyncio.sleep(3)
            await message.reply(
                "當你登入01後，令人意外的是，這不是來自你同事的訊息，而是Jack傳了一則邀請給了你，他邀請你加入一個關於民防的MF，希望你和Alex能在這裡和大家一起學習民防。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "（MF登入中）"
            )
            await asyncio.sleep(5)
            await message.reply(
                "（正在加入Jack的世界）"
            )
            await asyncio.sleep(3)
            await message.reply(
                "進入MF後，Alex和Jack跑來向你打招呼："
            )
            await asyncio.sleep(2)
            await message.reply(
                "Jack：**「歡迎你們來到我的世界，現在感覺如何？」**"
            )
            await asyncio.sleep(2)
            await message.reply(
                "Alex：**「什麼感覺如何？」**"
            )
            await asyncio.sleep(2)
            await message.reply(
                "Jack：**「難道不期待？」**"
            )
            await asyncio.sleep(2)
            await message.reply(
                "Alex：**「我……你在浪費我的睡眠時間。」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "Jack無視了還在起床氣的Alex，轉向你，接著開口說："
            )
            await asyncio.sleep(1)
            await message.reply(
                f"Jack：**「讓我們走吧～我能向你介紹這款遊戲。首先我們目前在的地點是{message.channel}～」**"
            )
            await asyncio.sleep(2)
            await message.reply(
                "只見Jack打開一個操作介面，點按了幾下，三個人就進入了另一個空間。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "（歡迎來到民防下午茶CD T-Time RPG遊戲系統！）"
            )
            await asyncio.sleep(2)
            await message.reply(
               "你：**「這是什麼鬼，什麼時候多了這樣一個遊戲？」**" 
            )
            await asyncio.sleep(2)
            await message.reply(
                "Jack：**「這是虛擬遊戲的世界，由民防下午茶基金會開發的新款遊戲，才剛發行沒多久，看見有興趣的主題我就買了！」**"  
            )
            await asyncio.sleep(2)
            await message.reply(
                "這時，Alex也從半夢半醒的狀態中醒來，有些不情願的說："
            )
            await asyncio.sleep(2)
            await message.reply(
                "Alex：**「既然都來了，那就玩一下吧。」**"
            )
            await asyncio.sleep(2)
            await message.reply(
                "Jack點點頭，微笑的按下了遊戲開始的按鈕。"
            )
            await asyncio.sleep(2)
            await message.reply(
              "（遊戲模式：戰爭模擬。任務內容：應對災難事件時的技巧／抵抗假訊息。目前生命值：3/3）"  
            )
            await asyncio.sleep(2)
            await message.reply(
                "接著，就出現了遊戲載入的畫面……"
            )
            await asyncio.sleep(2)
            await message.reply("**（正在載入副本）**")
            await asyncio.sleep(5)
            await message.reply("小蘑菇：「歡迎來到這個副本！我是指導員小蘑菇，今天就由我帶著你們解開謎底吧！」")
            await asyncio.sleep(3)
            Q1_embed = discord.Embed(
                title="第一題：", 
                description="空襲警報響起！敵軍的轟炸機已經近在咫尺。將家中的門窗關緊後，你應該選擇躲藏在？", 
                color=0xffcec7
            )
            Q1_embed.add_field(
                name="A.", 
                value="陽台落地窗旁邊的書桌後。", 
                inline=False
            )
            Q1_embed.add_field(
                name="B.", 
                value="離落地窗有一段距離，電視牆後面的餐桌旁。", 
                inline=False
            )
            view = AnsAorB()
            await message.reply(
                embed = Q1_embed, 
                view = view, 
            )
        if message.content == "你選擇了A" and message.author.bot:
            await message.reply(
                "小蘑菇：「炸彈爆炸導致落地窗碎裂！你被飛濺的玻璃炸傷了。生命值-1」"
           )
            self.life_value = life_value - 1
            await message.reply(
                f"生命值：{self.life_value}/3"
            )
        elif message.content == "你選擇了A" and message.author.bot:
            await message.reply(
                "小蘑菇：「雖然落地窗被炸彈的衝擊波給破壞了，但電視牆為你擋住了攻擊，你毫髮無傷！」"
            )


class AnsAorB(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(
        label="A", 
        style=discord.ButtonStyle.gray
    )
    async def button_A_click(
        self, 
        interaction: discord.Interaction, 
        button: discord.ui.Button
    ):
        button.disabled = True
        self.button_pressed = "A"
        await interaction.response.send_message(
            "你選擇了A"
        )

    @discord.ui.button(
        label="B", 
        style=discord.ButtonStyle.gray
    )
    async def button_B_click(
        self, 
        interaction: discord.Interaction, 
        button: discord.ui.Button
    ):
        button.disabled = True
        await interaction.response.send_message(
            "你選擇了B"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Task(bot))
