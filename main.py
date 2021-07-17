import discord
from discord.ext import commands
from pretty_help import PrettyHelp
import os
import asyncio

import subprocess
subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout

try:
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
except BaseException:
    import config
    TOKEN = config.TOKEN


# test2


bot = commands.Bot(command_prefix='>', description="ReMod Bot", help_command=PrettyHelp())



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Moderating ReBoot server"))
    print("Logged in & ready to use")








bot.load_extension("cogs.general")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.admin")
bot.run(TOKEN)
