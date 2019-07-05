import asyncio
import traceback

import asyncpg
from discord.ext import commands

import config

bot = commands.Bot(command_prefix="em!", description="DMing you mentions in embeds.")
bot.load_extension("jishaku")
bot.config = config

for ext in config.startup_exts:
    try:
        bot.load_extension(ext)
    except Exception:
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
