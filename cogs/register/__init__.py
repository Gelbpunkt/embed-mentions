import discord
from discord.ext import commands
from utils.checks import *


class Register:
    def __init__(self, bot):
        self.bot = bot

    @not_registered()
    @commands.command()
    async def register(self, ctx):
        """Trigger notifications for mentions in embeds."""
        try:
            await ctx.author.send(
                "You have DMs turned on. Great! This message is a test if I can DM you when it happens."
            )
        except discord.Forbidden:
            return await ctx.send(
                "I can't DM you! Make sure to turn it on and use this command again!"
            )
        await self.bot.pool.execute(
            'INSERT INTO emregistered ("user") VALUES ($1);', ctx.author.id
        )
        self.bot.registered.append(ctx.author.id)
        await ctx.send(f"**{ctx.author}** has been registered.")

    @registered()
    @commands.command()
    async def unregister(self, ctx):
        """Unregisters you for mentions."""
        await self.bot.pool.execute(
            'DELETE FROM emregistered WHERE "user"=$1;', ctx.author.id
        )
        self.bot.registered.remove(ctx.author.id)
        await ctx.send(f"**{ctx.author}** has been unregistered.")


def setup(bot):
    bot.add_cog(Register(bot))
