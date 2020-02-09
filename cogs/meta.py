import json
import aiohttp
from os import environ as env

import discord
from discord.ext import tasks, commands

base_url = env.get("URL")
api_url = base_url + "/random_json.php"


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=30.0)
    async def printer(self):
        channel = self.bot.get_channel(676119546158907392)

        embed = discord.Embed()
        embed.color = self.bot.embed_color

        async with aiohttp.ClientSession() as cs:
            async with cs.get(api_url) as r:
                res = json.loads(await r.text())

                embed.set_image(url=base_url + res["src"])
                embed.set_footer(text=f"Score: {round(res['score'], 2)}")

                await channel.send(embed=embed)

    @printer.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Meta(bot))
