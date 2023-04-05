from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import openpyxl
import random
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(activity=discord.Game("'레나야' 라고 부르시면 언제든 대답해 드려요!"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

        if message.content.startswith(f'{PREFIX} 도움말'):
        embed = discord.Embed(
            title = '명령어 목록',
            description = '아직 공부하는 중이에요! 더 완벽해질 수 있도록 노력할게요!.',
            colour = discord.Colour.blue()
        )
        embed.add_field(name = '디맥선곡기', value = '오늘 플레이할 디맥 곡을 추천해드릴게요!', inline = False)

        await message.channel.send(embed=embed)
        
    if message.content.startswith(f'{PREFIX}'):
        rp = random.('네!', '레나에요!', '부르셨나요?')
        await message.channel.send(f'rp')

    if message.content.startswith(f'{PREFIX} 심심해'):
        simsim = random.randrange(1,10)
        file = openpyxl.load_workbook("반응.xlsx")
        sheet = file.active
        for i in range(1,8):
            if i == simsim:
                if sheet["B" + str(i)].value == "심심해":
                    res = sheet["A" + str(i)].value
                    await message.channel.send(f"{res}")

    if message.content.startswith(f'{PREFIX} 디맥선곡기'):
        Dpick = random.randrange(1,10)
        file = openpyxl.load_workbook("디맥.xlsx")
        sheet = file.active
        for i in range(1,10):
            if i == Dpick:
                ser = sheet["C" + str(i)].value
                com = sheet["B" + str(i)].value
                tit = sheet["A" + str(i)].value
                await message.channel.send(f"{ser}에 수록된 {com}님의 {tit}은(는) 어떠신가요?")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
