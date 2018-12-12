from discord.ext import commands


class AlreadyRegistered(commands.CheckFailure):
    pass


class NeedsRegistered(commands.CheckFailure):
    pass


def registered():
    def predicate(ctx):
        return ctx.author.id in ctx.bot.registered

    return commands.check(predicate)


def not_registered():
    def predicate(ctx):
        return not ctx.author.id in ctx.bot.registered

    return commands.check(predicate)
