import os

import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv("../../")

BOT_STATUS = os.getenv('STATUS')
BOT_ACTIVITY = discord.Game(os.getenv('ACTIVITY'))


class ready(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        await self.bot.change_presence(
            status=BOT_STATUS, activity=BOT_ACTIVITY, afk=False)

        print(f'{self.bot.user.name} has connected to Discord!')
        print(f'{self.bot.user.id} is the id of {self.bot.user.name}')


def setup(bot):

    bot.add_cog(ready(bot))
