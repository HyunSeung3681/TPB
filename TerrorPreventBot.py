import discord
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
    if "ㅁ" in message.content and "ㅊ" in message.content:
    	await message.delete()
    	await message.channel.send(f"{message.author.mention} 착한말^^")
    	channel = discord.utils.get(message.guild.text_channels, name="📃tpb-로그")
    	await channel.send(f"{message.author.mention}님이 욕설을 사용하셨습니다.\n사용 욕설 : ㅁㅊ\n메시지 내용 : {message.content}")
    if message.content == "t-핑":
        await message.channel.send(f":ping_pong: 퐁! 현재 핑은 {app.latency}초입니다!")

access_token=os.environ["BOT_TOKEN"]
app.run(access_token)
