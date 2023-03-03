import os
from os.path import join, dirname
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.utils import *
from commands.chatgpt import ChatGPT


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
OPENAI_API_KEY = os.environ.get('PERSONAL_OPENAI_API_KEY')
OPENAI_ORG = os.environ.get('PERSONAL_OPENAI_ORG')

print(OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot_description = """
Doraemon Discord bot is a multi-purpose bot for Discord.
It can provide `-chat` function with OpenAI ChatGPT.
Other functions like music playing are still under development, stay tuned!
"""
bot = commands.Bot(command_prefix='-', intents=intents, description=bot_description)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('-'):
        await bot.process_commands(message)
        return

async def set_presence():
    await bot.wait_until_ready()
    listening = discord.Activity(type=discord.ActivityType.listening, name="-help")
    await bot.change_presence(activity=listening)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.add_cog(ChatGPT(key=OPENAI_API_KEY, org=OPENAI_ORG))
    await set_presence()


bot.run(DISCORD_TOKEN)
