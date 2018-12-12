import discord
from discord.ext import commands


class Owner:
    def __init__(self, bot):
        self.bot = bot

    def __local_check(self, ctx):
        return self.bot.is_owner(ctx.author)

    @commands.command(hidden=True)
    async def die(self, ctx):
        """Kill me!"""
        await ctx.send("Dying!")
        await self.bot.logout()

    @commands.command(name="list", hidden=True)
    async def _list(self, ctx):
        """Lists all registered users."""
        await ctx.send(
            "\n".join([str(self.bot.get_user(id)) for id in self.bot.registered])
        )

    @commands.command(hidden=True)
    async def update(self, ctx):
        a = [i for i in self.bot.registered if self.bot.get_user(i) is None]
        a = await self.bot.pool.execute(
            'DELETE FROM registered WHERE "user"=ANY($1);', a
        )
        await ctx.send(a)


def setup(bot):
    bot.add_cog(Owner(bot))
