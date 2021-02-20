#!Python 3.9.1

# Importing the required modules!
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

import keep_alive

# Loading the environment variables from ".env"
load_dotenv("../")

# Retriving the required environment variables from ".env"
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_PREFIX = os.getenv('PREFIX')

# Declaring the command prefix for the discord bot
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())


# On Ready
bot.load_extension("cogs.ready")


# Guiding the user
bot.load_extension("cogs.guideonping")

# What is Splendid
bot.load_extension("cogs.splendid")

# Get News
bot.load_extension("cogs.news")

# Play Tic-Tac-Toe
bot.load_extension("cogs.tic-tac-toe")

# Keep the bot alive
keep_alive.keep_alive()

# This command starts the bot!
bot.run(TOKEN)
