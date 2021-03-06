import sys
import traceback

import discord
from discord.ext import commands

from utils.checks import AlreadyRegistered, NeedsRegistered


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.on_command_error = self._on_command_error

    async def has_mentions(self, msg: discord.Message, em: discord.Embed):
        texts = (
            f"{em.title}"
            f"{em.description}"
            f"{em.footer.text}"
            f"{''.join([f.value for f in em.fields])}"
        )
        users = [
            u
            for u in self.bot.registered
            if (f"<@{u}>" in texts or f"<@!{u}>" in texts)
        ]
        for u in users:
            try:
                await self.bot.get_user(u).send(
                    f"""\
You have been mentioned in an embed by **{msg.author}** in server **{msg.guild.name}**!
Jump to: {msg.jump_url}""",
                    embed=em,
                )
            except discord.Forbidden:
                pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot and not message.embeds:
            return

        if message.author.id == self.bot.user.id:
            return

        if message.embeds:
            await self.has_mentions(message, message.embeds[0])

    async def _on_command_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, discord.Forbidden):
            return
        elif isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.NotOwner):
            return await ctx.send("No u")
        elif isinstance(error, AlreadyRegistered):
            return await ctx.send("You're already registered.")
        elif isinstance(error, NeedsRegistered):
            return await ctx.send("You need to be registered to use this.")
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )


def setup(bot):
    bot.add_cog(Events(bot))
