import json
import sys
import asyncio
import time
from discord.ext import commands


with open("setting.json", "r", encoding="utf8") as jfile:  # CHANGE THIS
    jdata = json.load(jfile)
RETRY = 5
DELAY = 4
CHANNEL_ID = "<CHANNEL_ID>"  # CHANGE THIS
TIME = int(time.time()) + int(sys.argv[2])

if int(sys.argv[2]) <= DELAY:
    TEXT = f"台北 {sys.argv[1]} 級搖起來 ~ 翔翔已經在 <t:{TIME}:R> 就一屁股摁你臉上了，請節哀！"
else:
    TEXT = f"台北 {sys.argv[1]} 級搖起來 ~ 翔翔大概會在 <t:{TIME}:R> 抵達！請做好翔擊準備！"

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    for _ in range(RETRY):
        channel = bot.get_channel(CHANNEL_ID)
        if channel is not None:
            await channel.send(TEXT)
            await bot.close()
            break
        else:
            await asyncio.sleep(1)
    await bot.close()


bot.run(jdata["Discord_Robot_Token"])
