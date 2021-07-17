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


#test2


bot = commands.Bot(command_prefix='>', description="ReMod Bot")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Moderating ReBoot server"))
    print("Logged in & ready to use")


@bot.command()
async def mute(ctx, user: discord.Member):
    role = discord.utils.find(lambda r: r.name == 'mods',ctx.message.guild.roles)
    if ctx.message.author.has_role(role):
        roleobject = discord.utils.get(
            ctx.message.guild.roles,
            id=865254696259551233)
        await user.add_roles(roleobject)
        await ctx.send(f":white_check_mark: Muted {user}")
    else:
        await ctx.reply("You don't have permission to do that")

@bot.command()
async def unmute(ctx, user: discord.Member):
    role = discord.utils.find(lambda r: r.name == 'mods',ctx.message.guild.roles)
    if ctx.message.author.has_role(role):
        roleobject = discord.utils.get(
            ctx.message.guild.roles,
            id=865254696259551233)
        await user.remove_roles(roleobject)
        await ctx.send(f":white_check_mark: Unmuted {user}")
        
    else:
        await ctx.reply("You don't have permission to do that")

@bot.command()
async def gitpull(ctx):
    if ctx.message.author.id in [744224056966119565,686483505252925533]:
        subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout
        await ctx.reply("Executing `git pull`")
    else:
        await ctx.reply("Sorry you don't have permission to do that")


@bot.command()
async def restart(ctx):
    if ctx.message.author.id in [744224056966119565,686483505252925533]:
        await ctx.reply("Restarting...`")
        print("Restarting...")
        os.system("python main.py")
        exit()
    else:
        await ctx.reply("Sorry you don't have permission to do that")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {bot.latency*1000}ms !')    

bot.run(TOKEN)


