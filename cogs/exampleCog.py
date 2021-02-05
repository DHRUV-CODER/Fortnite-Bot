import discord
from discord.ext import commands


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example(self,ctx):
      await ctx.send("You Have Accidentally Hit Up Example Cog")    

def setup(bot):
    bot.add_cog(Stats(bot))
