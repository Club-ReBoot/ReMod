from discord.ext import commands

class general(commands.Cog, name='Administration',description="Some commands that can only be run by the owner"):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command(pass_context=True,brief='Execute git pull', description='This command will execute git pull request. This command can only be run by bot owners')
    async def gitpull(self,ctx):
        if ctx.message.author.id in [744224056966119565, 686483505252925533]:
            subprocess.run(["git", "pull"], check=True,
                           stdout=subprocess.PIPE).stdout
            await ctx.reply("Executing `git pull`")
        else:
            await ctx.reply("Sorry you don't have permission to do that")


    @commands.command(pass_context=True,brief='Restart the bot', description='This command will restart the bot. This command can only be run by bot owners')
    async def restart(self,ctx):
        if ctx.message.author.id in [744224056966119565, 686483505252925533]:
            await ctx.reply("Restarting...`")
            print("Restarting...")
            os.system("python main.py")
            exit()
        else:
            await ctx.reply("Sorry you don't have permission to do that")



def setup(bot):
    bot.add_cog(general(bot))
