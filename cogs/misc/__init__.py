import discord
from discord.ext import commands


class Misc:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Ping!"""
        await ctx.send(
            f"Tracking mentions in embeds with a latency of **{round(self.bot.latency * 1000)}ms**."
        )

    @commands.command()
    async def invite(self, ctx):
        """Invite me!"""
        await ctx.send(
            "<https://discordapp.com/oauth2/authorize?client_id=467659662402125824&permissions=66560&scope=bot>"
        )


def setup(bot):
    bot.add_cog(Misc(bot))
