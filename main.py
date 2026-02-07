import os
import discord
import random
import logging 
from discord.ext import commands
from dotenv import load_dotenv

from keep_alive import keep_alive

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# load in the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user} (ID: {bot.user.id})')
    logger.info('------ Bot is Ready ------')

@bot.command()
async def joue(ctx):
    logger.info(f"{ctx.author} wants to play!")
    await ctx.send(f"{ctx.author.mention} veut jouer, des gens?")

@bot.command()
async def rand(ctx, *options):
    if not options:
        logger.warning(f"{ctx.author} tried to use !rand without providing options.")
        await ctx.send(f"{ctx.author.mention} veuillez fournir des options. Usage: `!rand option1 option2 option3`")
        return
    choice = random.choice(options)
    logger.info(f"{ctx.author} randomly chose {choice} from options: {options}")
    await ctx.send(f"{ctx.author.mention} a choisi -> **{choice}**")

# prepare a Flask request to keep the bot alive
keep_alive()
# Run the bot
bot.run(TOKEN)