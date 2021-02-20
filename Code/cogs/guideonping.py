import os

import dotenv
from discord.ext import commands

dotenv.load_dotenv("../../")

BOT_PREFIX = os.getenv('PREFIX')

class guideonping(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        ping = f"@!{self.bot.user.id}"

        if ping in message.content:

            await message.channel.send(f"What is it {message.author.mention}?\nPlease do `{BOT_PREFIX}help` if you want to know how to use me!\nYou can also DM me to use me!")


def setup(bot):

    bot.add_cog(guideonping(bot))
