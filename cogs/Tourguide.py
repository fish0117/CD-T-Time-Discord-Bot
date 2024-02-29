import asyncio
import discord
from discord.ext import commands
from discord import app_commands


class Intorduce(commands.Cog):
    def __init__(
        self, 
        bot: commands.Bot
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
        if message.content == "歡迎新客人~讓小蘑菇帶你參觀一下吧!" and message.author.bot:
            await asyncio.sleep(2)
            await message.reply(
                "在未來，人們嚮往的虛擬世界已被開發到了近乎飽和的階段，雖然還是有些漏洞，而且人們也常利用這樣的弱點，散播謠言「病毒」。所以為了應付這種情況而誕生出來的，便是我們「假訊息糾察員」！ "
            )
            await asyncio.sleep(3)
            await message.reply(
                "身為一位專業的假訊息糾察員，我們的任務是抓出每一個惡意散佈的聳動流言，並為大眾提供正確的事實。我們以此為榮。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "我們的工作主要是處理一個名為「01」裝置的網路安全與真實性。在這新的世代，人們總戴著通往虛擬遊戲的「頭盔」，這就是「01」。雖說是頭盔，但其實並不像我們想像中的戴在頭上很大的那種，它只是一個小掛件，只要配戴耳朵上，按下開關便能去到與大家連結的虛擬世界。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "人們將這樣的虛擬世界稱為「MF」。在這裡，可以找到所有你想要的答案，有點像現在的瀏覽器，但功能更為全面。每個人都可以在上面發文，回答問題，不過也確實存在著假訊息。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "也因為虛擬與現實的界線更加模糊，對於假訊息攻擊的防護與真實訊息的查證變得更加重要。"
            )
            await asyncio.sleep(1)
            await message.reply(
                "（如果你還在聽，請點擊按鈕以繼續）"
            )
            view = Teaching()
            await message.reply(
                view=view
            )

        if message.content == "### 序章" and message.author.bot:
            await message.reply(
                "這天你一如往常的上去「MF」瀏覽資訊，隨著文字一行行閃過，偶然發現了一則關於遠方戰亂的陰謀論，看到這則莫名的訊息，你嘲笑這文章的荒謬，與作者的無知。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "近年來興起了享用下午茶的風潮，小鎮裡，人們每天下午都會自發性的舉辦下午茶會，就像文藝復興時期的沙龍那樣。一邊享用甜品，一邊閒聊，因此你和朋友們每一天都會進行一場下午茶會。你決定把這話題帶去讓朋友進行思辨。"
            )
            await asyncio.sleep(2)
            await message.reply(
                "（試著提出你第一個問題吧！使用`/question`進行提問。）  "
            )
            await asyncio.sleep(3)
            await message.reply(
                "你：**提問：「＿＿＿＿」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "很好！無論你說的話是否完美，至少你成功踏出第一步。當你完成「提問」，我們將為你的活躍度加2點。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "這點數代表了你在茶會上的發言有多活躍，它可以用來兌換身份，以及解鎖各式特別的權限，期待你的探索~"
            )
            await asyncio.sleep(3)
            await message.reply(
                "現在Alex對你發起**提問：「假設文章中的荒謬情節真的發生了，我們應該怎麼做？」**"
            )
            await asyncio.sleep(2)
            await message.reply(
                "（試著回答吧，使用`/answer`進行回答。）"
            )
            await asyncio.sleep(3)
            await message.reply(
                "你：**回答Alex：「＿＿＿＿」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "Jack：**回答Alex：「當然要做好民防呀～」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "看來Jack和你都同樣對Alex的問題提出「回答」了，這時你們都會獲得3點活躍度。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "你和Alex同時望向了Jack，此時Alex先向Jack提起回覆"
            )
            await asyncio.sleep(3)
            await message.reply(
                "Alex：**回覆Jack：「民防？聽都沒聽過……」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "是的，當你想針對某人的發言進行評論，卻又不是回答的時候，即可使用「回覆」(`/reply`)。同樣的，使用回覆能讓你獲得2點。"
            )
            await asyncio.sleep(3)
            await message.reply(
                "善用回覆和提問能更簡單的讓他人理解你的意圖，是很重要的小技巧~"
            )
            await asyncio.sleep(3)
            await message.reply(
               "Jack：**回覆Alex：「拜託……這東西超重要的好嗎……」**" 
            )
            await asyncio.sleep(3)
            await message.reply(
                "Jack：**回覆ALL：「讓我來為你們科普一下民防吧！民防就是當前線發生戰爭時，我們可以在後方做的事，小到學會緊急包紮、知道避難地點，大到能夠指揮大眾、拿起武器保護自己…… 」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "Alex：**回覆Jack：「講重點好嗎…… 」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "Jack：**回覆Alex：「……」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "這下大家徹底沉默了，你是否應該打破這段尷尬呢？"
            )
            await asyncio.sleep(3)
            await message.reply(
                "（來做總結吧！使用`/summary`進行總結） "
            )
            await asyncio.sleep(3)
            await message.reply(
                "你：**總結問題「假設文章中的荒謬情節真的發生了，我們應該怎麼做？」：「＿＿＿＿」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "Jack：**回覆了你：「終於有用腦袋在思考的人了！才不像某個傢伙，什麼都不思考」**"
            )
            await asyncio.sleep(3)
            await message.reply(
                "完美的一次對談，只要總結後的3天內，贊同這個結論的人超過投票的3/5，那麼結論將會成立，介時你會再獲得5點。至少現在讓我們先舉起茶杯品嚐一口，盡情享受這場下午茶吧~ 我們下次見~"
            )
            await asyncio.sleep(3)
            await message.reply(
                "（歡迎你隨時把我召喚出來，現在快和更多朋友一起去漫遊「民防下午茶」吧~）"
            )


class Teaching(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(
        label="繼續", 
        style=discord.ButtonStyle.green
    )
    async def teaching(
        self, 
        interaction: discord.Interaction, 
        button: discord.ui.Button
    ):
        button.disabled = True
        await interaction.response.send_message(
            "### 序章"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Intorduce(bot))
