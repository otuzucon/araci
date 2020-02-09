#!usr/bin/python3.7
# 09.01.2020 - lId@

import datetime
from os import environ as env

import discord
from discord.ext import commands


description = """
İki şey arasında, bağlantı kuran kimse, vasıta.
"""

extensions = [
    "cogs.admin",
    "cogs.meta",
]


def get_prefix(bot, msg):
    user_id = bot.user.id
    return [f"<@!{user_id}> ", f"<@{user_id}> ", "a."]


class Araci(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=get_prefix, description=description)

        self.embed_color = 0x36393F
        self.owner_ids = set([428273380844765185])

        for cog in extensions:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print(f"{cog} {exc.__class__.__name__}: {exc}")

        if not hasattr(self, "uptime"):
            self.uptime = datetime.datetime.utcnow()

    @property
    def owners(self):
        return [self.get_user(i) for i in self.owner_ids]

    def run(self):
        super().run(env.get("TOKEN"), reconnect=True)


bot = Araci()


@bot.event
async def on_ready():
    print(f"{bot.user} (ID: {bot.user.id})")
    print(f"discord.py version: {discord.__version__}")


if __name__ == "__main__":
    bot.run()
