from discord.ext import commands

class general(commands.Cog, name='General',description="Just some basic commands"):
    def __init__(self, bot):
        self.bot = bot
  

    @commands.command(pass_context=True,brief='Gives the ping of the bot', description='Returns the ping in ms.')
    async def ping(self,ctx):
        await ctx.send(f'My ping is {self.bot.latency*1000}ms !')

def setup(bot):
    bot.add_cog(general(bot))
