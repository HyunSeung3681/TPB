import discord
import asyncio
import os

app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=============")
    messages = ["욕(채팅) 필터링 하는 중","t-도움을 입력해보세요!", f"{len(app.guilds)}개의 서버와 {len(app.users)}명의 유저와 함께"]
    while True:
        await app.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[0], type=discord.ActivityType.playing))
        messages.append(messages.pop(0))
        await asyncio.sleep(5)
    
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
    if message.content == "t-도움":
        await message.channel.send("아직 만들고 있답니다")

access_token=os.environ["BOT_TOKEN"]
app.run(access_token)
