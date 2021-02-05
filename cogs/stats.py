import random
import aiohttp
from discord.ext import commands
import discord

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fort(self, ctx, *, playername):
        try:
            async with ctx.channel.typing():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://fortnite-api.com/v1/stats/br/v2?name={playername}") as r:
                        data = await r.json(content_type=None)

                        embed = discord.Embed(title=f"Showing Stats For Player : __{playername}__ <a:noob:805793279978504193>",color=0x50e1ed)
                        embed.add_field(name='Level 🔼', value="`{}`".format(data['data']['battlePass']['level']), inline=True)
                        embed.add_field(name='Progress', value="`{}`".format(data['data']['battlePass']['progress']), inline=True)
                        embed.add_field(name='Matches Played', value="`{}`".format(data['data']['stats']['all']['overall']['matches']), inline=False)
                        embed.add_field(name='Wins', value="`{}`".format(data['data']['stats']['all']['overall']['wins']), inline=False)
                        embed.add_field(name=' ☠', value="`{}`".format(data['data']['stats']['all']['overall']['deaths']), inline=True)
                        embed.add_field(name='KDr <a:tenor:805793777197383721>', value="`{}`".format(data['data']['stats']['all']['overall']['kd']), inline=True)                    
                        embed.add_field(name='Score', value="`{}`".format(data['data']['stats']['all']['overall']['score']), inline=False)
                        embed.add_field(name='Score Per Min', value="`{}`".format(data['data']['stats']['all']['overall']['scorePerMin']), inline=True)
                        embed.add_field(name='/ Match', value="`{}`".format(data['data']['stats']['all']['overall']['scorePerMatch']), inline=True)
                        embed.add_field(name='Top 3️⃣', value="`{}`".format(data['data']['stats']['all']['overall']['top3']), inline=False)
                        embed.add_field(name='Top 5️⃣', value="`{}`".format(data['data']['stats']['all']['overall']['top5']), inline=True)
                        embed.add_field(name='Top 🔟', value="`{}`".format(data['data']['stats']['all']['overall']['top10']), inline=True)
                        embed.set_thumbnail(url="https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/1052/2019/08/13071156/fortnite-logo.jpg")
                        embed.add_field(name='Kills', value="`{}`".format(data['data']['stats']['all']['overall']['kills']), inline=False)
                        embed.add_field(name='Kills Per Min', value="`{}`".format(data['data']['stats']['all']['overall']['killsPerMin']), inline=True)
                        embed.add_field(name='/ Match', value="`{}`".format(data['data']['stats']['all']['overall']['killsPerMatch']), inline=True)
                        embed.add_field(name='Win Rate', value="`{}`".format(data['data']['stats']['all']['overall']['winRate']), inline=True)
                        embed.add_field(name='Mins Played', value="`{}`".format(data['data']['stats']['all']['overall']['minutesPlayed']), inline=True)
                        embed.add_field(name='Players Out Lived ', value="`{}`".format(data['data']['stats']['all']['overall']['playersOutlived']), inline=False)
                        embed.add_field(name='Played Game Last Time:', value="```css\n{} ```".format(data['data']['stats']['all']['overall']['lastModified']), inline=True)
                        await ctx.send(embed=embed)                               
        except:
            embed=discord.Embed(title="Currently We only Support Epic Accounts",description="In Near Future You will See More...",color=0xfb0000)
            embed.set_thumbnail(url="https://i.pinimg.com/originals/75/84/04/758404ebc522ce0beff7f02e59fdaf47.jpg")
            await ctx.send(embed=embed)         

def setup(bot):
    bot.add_cog(Stats(bot))
