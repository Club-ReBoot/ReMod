import discord
from discord.ext import commands
import os
import asyncio

import subprocess
subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout

try:
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
except:
    import config
    TOKEN=config.TOKEN


#test

bot = commands.Bot(command_prefix='>', description="ReMod Bot")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Moderating ReBoot server"))
    print("Logged in & ready to use")


@bot.command()
async def mute(ctx, user: discord.Member, duration=600000, *, unit=None):
    roleobject = discord.utils.get(
        ctx.message.guild.roles,
        id=865254696259551233)
    await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
    await user.add_roles(roleobject)

bot.run(TOKEN)


