from discord.ext import commands
import discord

class general(commands.Cog, name='Moderation',description="Some Moderation commands that can only be run by a mod."):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command(pass_context=True, aliases=["clear","purge"],brief='Purge message in a channel', description='This command will purge/clear message. This command can only be run by mods')
    async def clean(ctx, lim=10):
        role = discord.utils.find(
            lambda r: r.name == 'mods',
            ctx.message.guild.roles)
        if role in ctx.message.author.roles:
            await ctx.channel.purge(limit=int(lim)+1)
            await ctx.send(f"Cleared {lim} msg on the request of {ctx.author.mention}")
        else:
            await ctx.reply("You don't have permission to do that")

    @commands.command(brief='Unute a member', description='This command will unmute a member. This command can only be run by mods')
    async def unmute(ctx, user: discord.Member):
        role = discord.utils.find(
            lambda r: r.name == 'mods',
            ctx.message.guild.roles)
        if role in ctx.message.author.roles:
            roleobject = discord.utils.get(
                ctx.message.guild.roles,
                id=865254696259551233)
            await user.remove_roles(roleobject)
            await ctx.send(f":white_check_mark: Unmuted {user}")

        else:
            await ctx.reply("You don't have permission to do that")

    @commands.command(brief='Mute a member', description='This command will mute a member. This command can only be run by mods')
    async def mute(ctx, user: discord.Member):
        role = discord.utils.find(
            lambda r: r.name == 'mods',
            ctx.message.guild.roles)
        if role in ctx.message.author.roles:
            roleobject = discord.utils.get(
                ctx.message.guild.roles,
                id=865254696259551233)
            await user.add_roles(roleobject)
            await ctx.send(f":white_check_mark: Muted {user}")
        else:
            await ctx.reply("You don't have permission to do that")



def setup(bot):
    bot.add_cog(general(bot))
