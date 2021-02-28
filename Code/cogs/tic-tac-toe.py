# Importing required modules

import os

import asyncio

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv('../../')

X_EMOJI = os.getenv('X_EMOJI')
O_EMOJI = os.getenv('O_EMOJI')


event = asyncio.Event()


# Class "tictactoe" which is used as a cog to implement the Tic-Tac-Toe game in Discord
class tictactoe(commands.Cog):

    # Class constructor
    def __init__(self, bot):

        self.bot = bot

    # All the definitions which make up the game!

    # Function to listen to the choices the user makes

    @commands.Cog.listener()
    async def on_message(self, message):

        if (message.content.startswith("!choice")):

            if (message.author == self.player1):

                if (message.content[8:] in self.choices
                        and self.player == X_EMOJI):

                    self.choice = message.content[8:]

                    event.set()
                    event.clear()

        if (message.content.startswith("!choice")):

            if (message.author == self.player2):

                if (message.content[8:] in self.choices
                        and self.player == O_EMOJI):

                    self.choice = message.content[8:]

                    event.set()
                    event.clear()

    # Function to initiate the game and a bot command which initiates the game

    @commands.command(
        name="tic-tac-toe",
        aliases=["ttt"],
        help="Usage: $#tic-tac-toe/ttt @<user you want to play tic-tac-toe with on the current server>.\nAfter that, when the bot gives you the choices you should choose one from the choices using !choice <YOUR CHOICE>('<YOUR CHOICE>' must be replaced with your choice from the given choices and a single space is mandatory after '!choice'\n If you don't respond within 1 minute after the bot gives you the choices, the game session will be ended)"
    )
    async def playttt(self, ctx, playwith: discord.Member):

        self.player1 = ctx.author
        self.player2 = playwith

        grid = {
            "Top-Left": ":white_large_square:",
            "Top-Middle": ":white_large_square:",
            "Top-Right": ":white_large_square:",
            "Middle-Left": ":white_large_square:",
            "Middle-Middle": ":white_large_square:",
            "Middle-Right": ":white_large_square:",
            "Bottom-Left": ":white_large_square:",
            "Bottom-Middle": ":white_large_square:",
            "Bottom-Right": ":white_large_square:"
        }

        if(self.player2.status != discord.Status.offline and self.player2.status != discord.Status.dnd):

            await self.Play(grid, self.player1, self.player2)

        else:

            await self.player1.send(f"> {self.player2.name} is Offline/ in DnD at the moment and you can't play with them")

    # Function which draws the initializes the game with all the values

    async def Initialize(self, grid, player1, player2):

        print("\033[35mWelcome to the game of Tic-Tac-Toe!\033[0m\n")
        await player1.send("> Welcome to the game of Tic-Tac-Toe!")
        await player2.send("> Welcome to the game of Tic-Tac-Toe!")
        await self.InitialGridDraw(player1, player2)
        print()
        self.choices = [x for x in grid.keys()]
        self.player = X_EMOJI
        await player1.send(f"> You are {X_EMOJI}")
        await player2.send(f"> You are {O_EMOJI}")

    # Function which draws the initial board

    async def InitialGridDraw(self, player1, player2):

        await player1.send(
            ":white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:"
        )

        await player2.send(
            ":white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:"
        )

    # Function which draws updated boards as the game progresses

    async def GridDraw(self, grid, player1, player2):

        print("\033[36m             " + grid["Top-Left"] + "|" +
              grid["Top-Middle"] + "|" + grid["Top-Right"])
        await player1.send("             " + grid["Top-Left"] +
                           grid["Top-Middle"] + grid["Top-Right"])
        await player2.send("             " + grid["Top-Left"] +
                           grid["Top-Middle"] + grid["Top-Right"])
        print("             -|-|-")
        print("             " + grid["Middle-Left"] + "|" +
              grid["Middle-Middle"] + "|" + grid["Middle-Right"])
        await player1.send("             " + grid["Middle-Left"] +
                           grid["Middle-Middle"] + grid["Middle-Right"])
        await player2.send("             " + grid["Middle-Left"] +
                           grid["Middle-Middle"] + grid["Middle-Right"])
        print("             -|-|-")
        print("             " + grid["Bottom-Left"] + "|" +
              grid["Bottom-Middle"] + "|" + grid["Bottom-Right"] + "\033[0m")
        await player1.send("             " + grid["Bottom-Left"] +
                           grid["Bottom-Middle"] + grid["Bottom-Right"])
        await player2.send("             " + grid["Bottom-Left"] +
                           grid["Bottom-Middle"] + grid["Bottom-Right"])

    # Function which shifts the current player from "X to O" or "O to X"

    def PlayerShift(self, player):

        if self.player == X_EMOJI:
            return O_EMOJI

        if self.player == O_EMOJI:
            return X_EMOJI

    # Function which checks if the game is over

    def GameOver(self, player, grid):

        if (grid["Top-Left"] == self.player
                and grid["Top-Middle"] == self.player
                and grid["Top-Right"] == self.player):
            return True
        if (grid["Middle-Left"] == self.player
                and grid["Middle-Middle"] == self.player
                and grid["Middle-Right"] == self.player):
            return True
        if (grid["Bottom-Left"] == self.player
                and grid["Bottom-Middle"] == self.player
                and grid["Bottom-Right"] == self.player):
            return True
        if (grid["Top-Left"] == self.player
                and grid["Middle-Left"] == self.player
                and grid["Bottom-Left"] == self.player):
            return True
        if (grid["Top-Middle"] == self.player
                and grid["Middle-Middle"] == self.player
                and grid["Bottom-Middle"] == self.player):
            return True
        if (grid["Top-Right"] == self.player
                and grid["Middle-Right"] == self.player
                and grid["Bottom-Right"] == self.player):
            return True
        if (grid["Top-Left"] == self.player
                and grid["Middle-Middle"] == self.player
                and grid["Bottom-Right"] == self.player):
            return True
        if (grid["Top-Right"] == self.player
                and grid["Middle-Middle"] == self.player
                and grid["Bottom-Left"] == self.player):
            return True

    # Function which checks if the game ended in a tie

    def Tie(self, grid):

        valuesinthegrid = [x for x in grid.values()]
        for value in valuesinthegrid:
            if value == X_EMOJI or value == O_EMOJI:
                tieornot = True
            else:
                tieornot = False
                break
        return tieornot

    # Wait for user input

    async def waitforinput(self):

        await event.wait()

    # Main Function which calls the other functions and makes the game run correctly

    async def Play(self, grid, player1, player2):

        await self.Initialize(grid, player1, player2)

        while True:
            print(f"\033[32mThis is {self.player}'s turn\033[0m\n")
            if (self.player == X_EMOJI):

                await player1.send(f"**`Valid choices are {self.choices}`**")
                await player2.send("**`Waiting for player 'X'`**")
            if (self.player == O_EMOJI):

                await player2.send(f"**`Valid choices are {self.choices}`**")
                await player1.send("**`Waiting for player 'O'`**")
            print(f"\033[33mValid choices are {self.choices}\033[0m\n")
            print()

            print("Waiting...")

            try:

                await asyncio.wait_for(self.waitforinput(), timeout=60.0)

            except asyncio.TimeoutError:

                if(self.player == X_EMOJI):

                    await self.player1.send(f"{player2.mention} did not respond within 1 minute. Ended session!")
                    await self.player2.send(f"{player2.mention} did not respond within 1 minute. Ended session!")

                if(self.player == O_EMOJI):

                    await self.player1.send(f"{player1.mention} did not respond within 1 minute. Ended session!")
                    await self.player2.send(f"{player1.mention} did not mention within 1 minute. Ended session!")

                raise asyncio.TimeoutError

            print("Got it...")
            print(f"Choice of {self.player} is {self.choice}")

            grid[self.choice] = self.player
            self.choices.remove(self.choice)
            await self.GridDraw(grid, player1, player2)
            if (self.GameOver(X_EMOJI, grid) is True):
                print("\n\033[35mX has won the game!\033[0m")
                await player1.send(f"> {X_EMOJI} has won the game!")
                await player2.send(f"> {X_EMOJI} has won the game!")
                break
            if (self.GameOver(O_EMOJI, grid) is True):
                print("\n\033[35mO has won the game!\033[0m")
                await player1.send(f"> {O_EMOJI} has won the game!")
                await player2.send(f"> {O_EMOJI} has won the game!")
                break
            if (self.Tie(grid) is True):
                print(
                    "\n\033[35mNobody won the game. It ended in a Tie!\033[0m")
                await player1.send("> Nobody won the game. It ended in a Tie!")
                await player2.send("> Nobody won the game. It ended in a Tie!")
                break
            self.player = self.PlayerShift(self.player)


# Setup function which loads the cog into the bot if called
def setup(bot):

    bot.add_cog(tictactoe(bot))
