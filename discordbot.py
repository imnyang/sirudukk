from cmath import log
import discord
import os
from discord.types.embed import Embed
from dotenv import load_dotenv
import random
load_dotenv()

TOKEN = os.environ['TOKEN']

client = discord.Bot()
godn = discord.SlashCommandGroup("마법의", "마법의 소라고등님")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.command(name="핑", description="봇의 반응속도를 보여줘요!") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    embed = discord.Embed(title="🏓 퐁!", description=f'**{round(client.latency*1000)}ms**', color=discord.Color.green())
    await ctx.respond(embed=embed)

@client.command(name="주사위", description="주사위 굴려")
async def dice(ctx):
    embed = discord.Embed(title="🎲 콩", description=f'**{random.randint(1,6)}**', color=discord.Color.green())
    await ctx.respond(embed=embed)

@godn.command(name="소라고등님", description="제 인생은 어떻게 될까요?")
async def magic(ctx):
    sora = random.randint(0,1)
    embed = 0
    if(sora == 1):
        embed = discord.Embed(title="🐚", description=f'**응**', color=discord.Color.green())
    elif(sora == 0):
        embed = discord.Embed(title="🐚", description=f'**아니**', color=discord.Color.red())
    await ctx.respond(embed=embed)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
