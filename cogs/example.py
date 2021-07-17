from discord.ext import commands

class example(commands.Cog, name='My Cog'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def expcmd(self, ctx, argument):
       await self.bot.say("example cog")        



def setup(bot):
    bot.add_cog(example(bot))
