from discord.ext import commands
import requests
import json
import discord
try:
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
except BaseException:
    import config
    TOKEN = config.TOKEN


class entertainment(commands.Cog, name='Entertainment',description="Having Fun is also important, right?"):
    def __init__(self, bot):
        self.bot = bot
        
  




    @commands.command(pass_context=True,aliases=['youtube','youtubetogether'],brief='Youtube together in VC', description='This commands enables Youtube Together in VC.')
    #@bot.command()
    async def yt(self,ctx):
            try:
                    channel = ctx.author.voice.channel
                    #await ctx.send(f"```{channel}```")
                    url = f"https://discord.com/api/v9/channels/{channel.id}/invites"
                    params = {
                                                                            'max_age': 86400,
                                                                            'max_uses': 0,
                                                                            'target_application_id': 755600276941176913, 
                                                                            'target_type': 2,
                                                                            'temporary': False,
                                                                            'validate': None
                                                                    }
                    headers={'content-type': 'application/json','Authorization': f"Bot {TOKEN}"}
                    r=requests.post(url, data=json.dumps(params), headers=headers)
                    embed=discord.Embed(title="Youtube Together", description="Click on the title to join",url=f"https://discord.com/invite/{r.json()['code']}")
                    embed = discord.Embed(title="Youtube Together")
                    embed.description = f"[Click Here to Join Youtube Together in the VC](https://discord.com/invite/{r.json()['code']})"
                    await ctx.send(embed=embed)
            #await ctx.send("Click the button join Youtube Together in VC",components = [Button(label = "Youtube Together", style=3, id="yt")]
                    #components=[Button(style=ButtonStyle.URL,label="Youtube Together", url=f"https://discord.com/invite/{r.json()['code']}"),
                    #]
            
                    #)
            #await ctx.send(f"<https://discord.com/invite/{r.json()['code']}>")
            except AttributeError:
                    await ctx.send("You Are not in a VC")
            except Exception as e:
                    await ctx.send("There is some error in starting Youtube Togther or I don't have permission to create invite in that channel")

    @commands.command(pass_context=True,aliases=['chessinthepark','discordchess'],brief='Chess in VC', description='This commands enables Chess in VC.')
    #@bot.command()
    async def chess(self,ctx):
            try:
                    channel = ctx.author.voice.channel
                    #await ctx.send(f"```{channel}```")
                    url = f"https://discord.com/api/v9/channels/{channel.id}/invites"
                    params = {
                                                                            'max_age': 86400,
                                                                            'max_uses': 0,
                                                                            'target_application_id': 832012774040141894, 
                                                                            'target_type': 2,
                                                                            'temporary': False,
                                                                            'validate': None
                                                                    }
                    headers={'content-type': 'application/json','Authorization': f"Bot {TOKEN}"}
                    r=requests.post(url, data=json.dumps(params), headers=headers)
                    embed=discord.Embed(title="Chess", description="Click on the title to join",url=f"https://discord.com/invite/{r.json()['code']}")
                    embed = discord.Embed(title="Chess")
                    embed.description = f"[Click Here to Join CHESS in the VC](https://discord.com/invite/{r.json()['code']})"
                    await ctx.send(embed=embed)

            except AttributeError:
                    await ctx.send("You Are not in a VC")
            except Exception as e:
                    await ctx.send("There is some error in starting Youtube Togther or I don't have permission to create invite in that channel")


def setup(bot):
    bot.add_cog(entertainment(bot))
