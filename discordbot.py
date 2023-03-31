from cmath import log
import discord
import os
from discord.types.embed import Embed
from dotenv import load_dotenv
import random
load_dotenv()

TOKEN = os.environ['TOKEN']

client = discord.Bot()

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

@client.command(name="소라고등", description="제 인생은 어떻게 될까요?")
async def magic(ctx):
    sora = random.randint(0,1)
    embed = 0
    if(sora == 1):
        embed = discord.Embed(title="🐚", description=f'**응**', color=discord.Color.green())
    elif(sora == 0):
        embed = discord.Embed(title="🐚", description=f'**아니**', color=discord.Color.red())
    await ctx.respond(embed=embed)

    
@client.slash_command(description="니트로를 드립니다.")
async def disabledbutton(ctx):
        class Button(discord.ui.View):
                @discord.ui.button(label="눌러", style=discord.ButtonStyle.primary, disabled=True)
                async def primary(self, button: discord.ui.Button, interaction: discord.Interaction):
                        await ctx.respond(f"<@!{interaction.user.id}>님이 버튼 누름 <@!1073625669751291995>") # 버튼을 누를 수 없기 때문에 소용 없는 코드

        await ctx.respond("버튼을 누르세요.", view=Button())

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
