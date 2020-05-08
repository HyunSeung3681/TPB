import asyncio
import discord
import time
import random
import os

app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=============")

    await app.change_presence(activity=discord.Game(name="욕(채팅) 필터링", type=0))
@app.event
async def on_message(message) :
    if message.author.bot:
        return None
    if "ㅅ"in message.content and "ㅂ" in message.content:
        await message.delete()
        await message.channel.send(f'{message.author.mention}님은 욕설(비속어)를 사용하여 메세지가 삭제되었습니다.')
        embed = discord.Embed(title=f'비속어 감지',description=f'메세지 작성인 : {message.author.mention}\n감지된 비속어 : {message.content}\n메세지 감지 채널 : {message.channel.mention}',colour=message.author.colour)
        embed.set_footer(text=f'{message.author}', icon_url=message.author.avatar_url)
    	channel = discord.utils.get(message.guild.text_channels, name="tpb-로그")
    	await channel.send(embed = embed)
    if "ㅁ" in message.content and "ㅊ" in message.content:
    	await message.delete()
    	await message.channel.send(message.author.mention + " 착한말^^")
    	channel = discord.utils.get(message.guild.text_channels, name="tpb-로그")
    	await channel.send(message.author.mention+" 님이 욕설을 사용하셨습니다.")
access_token=os.environ["BOT_TOKEN"]
app.run(access_token)
