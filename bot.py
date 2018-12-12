import discord
from discord.ext import commands
import asyncpg
import asyncio
import config

bot = commands.Bot(command_prefix="em!", description="DMing you mentions in embeds.")
bot.load_extension("jishaku")
bot.owners = [356_091_260_429_402_122, 244_508_568_517_083_136]
bot.config = config

for ext in config.startup_exts:
    try:
        bot.load_extension(ext)
    except:
        print(f"Failed to load {ext}")
        traceback.print_exc()


@bot.event
async def on_ready():
    print("Ready")


async def start_bot():
    bot.pool = await asyncpg.create_pool(**config.db)
    await bot.pool.execute('CREATE TABLE IF NOT EXISTS emregistered ("user" bigint);')
    bot.registered = [
        i["user"] for i in await bot.pool.fetch('SELECT "user" FROM emregistered;')
    ]
    await bot.start(config.token)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
