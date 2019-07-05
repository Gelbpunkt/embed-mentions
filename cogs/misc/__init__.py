from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Ping!"""
        lat = round(self.bot.latency * 1000, 2)
        await ctx.send(f"Tracking mentions in embeds with a latency of **{lat}ms**.")

    @commands.command()
    async def invite(self, ctx):
        """Invite me!"""
        await ctx.send(
            "<https://discordapp.com/oauth2/authorize?client_id=467659662402125824&permissions=66560&scope=bot>"  # noqa
        )


def setup(bot):
    bot.add_cog(Misc(bot))
