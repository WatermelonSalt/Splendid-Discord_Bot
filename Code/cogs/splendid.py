import os

from discord.ext import commands

from dotenv import load_dotenv

# Loading the environment variables from ".env"
load_dotenv("../../")

# Getting the required environment variables
NAME = os.getenv('BOT_NAME')


class splendid(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    # Declaration of a command "whatissplendid" and a function "sendhelp" which shows what splendid is
    @commands.command(name=f"whatis{NAME.lower()}", help=f'Shows what "{NAME}" is')
    async def sendhelp(self, ctx):
        await ctx.send(f'`"{NAME}" is a "Cool Discord Bot"`')

    # Declartion of a command "howdoessplendidgetnews" and a function "tellthemhow" which shows how splendid gets the news

    @commands.command(name=f"howdoes{NAME.lower()}getnews", help=f'Shows how "{NAME} gets the news"')
    async def tellthemhow(self, ctx):
        await ctx.send(f'`{NAME} gets the news from NEWS API at newsapi.org using the get(<url>) from the python requests module and the returned information is decoded and formatted and sent as a message to the user. The <url> which should be provided to the get() method is encoded based on the options the user passes to the $#top-headlines/$#everything command`')


def setup(bot):

    bot.add_cog(splendid(bot))
