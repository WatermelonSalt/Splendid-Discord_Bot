from discord.ext import commands


class ready(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        print(f'{self.bot.user.name} has connected to Discord!')
        print(f'{self.bot.user.id} is the id of {self.bot.user.name}')


def setup(bot):

    bot.add_cog(ready(bot))
