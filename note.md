# ctx = context(上下文)

e.g.
A:/hello (上文)
B:Hello World (下文)

可以讀取例如使用者，id，所在伺服器，所在頻道

# discord api
server(伺服器) = guild(公會)
permission 權限

### coroutine 異步執行(協程)--->async
模擬電腦多執行緒
e.g. 現在有兩位使用者同時呼叫機器人--->
程式會交互完成兩個任務(但速度很快)，從而同時執行很多任務

# cog模組
將各個指令的檔案獨立並分門別類
- bot 主程式
負責執行載入(load)、卸載(unload)、重新載入(reload)程式檔案，可以讓 Discord Bot 上線期間就能更改指令。
- cogs 資料夾
放置分類過後的程式檔案，利用檔名就能知道此檔案的用途，增加撰寫程式碼的效率。

# 重要概念
- 程式中的“.”代表「的」的意思
  e.g.
  bot.commands ---> bot函式的command
- 程式中的“()”代表「動作」的意思
- e.g.
- variable = something()

# Class類別
物件導向 ---> 將程式內的所有東西以物件表示
class相當於將同一個類別的物件預先定義好某些屬性