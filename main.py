import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

from keep_alive import keep_alive

# load in the .env file
load_dotenv()
# prepare a Flask request to keep the bot alive
keep_alive()

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def joue(ctx):
    await ctx.send(f"{ctx.author.mention} veut jouer, des gens?")

@bot.command()
async def rand(ctx, *options):
    if not options:
        return
    choice = random.choice(options)
    await ctx.send(f"{ctx.author.mention} a choisi -> **{choice}**")


# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))