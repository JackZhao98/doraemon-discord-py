import os
from os.path import join, dirname
import discord
from discord.ext import commands
from dotenv import load_dotenv
# import ./utils/openai/ChatGPT.py OpenAIChat class
from utils.openai.ChatGPT import OpenAIChat

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
OPENAI_API_KEY = os.environ.get('PERSONAL_OPENAI_API_KEY')
OPENAI_ORG = os.environ.get('PERSONAL_OPENAI_ORG')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)
chatgpt = OpenAIChat(api_key=OPENAI_API_KEY, org=OPENAI_ORG);

def sanitize_message(message,  command_name,prefix='-'):
    return message.replace(prefix + command_name, '')

@bot.command()
async def clear(ctx):
    chatgpt.clear_message(ctx.message.author.id)
    await ctx.send(f"Cleared message for {ctx.message.author.name}")

@bot.command()
async def clearAll(ctx):
    chatgpt.clear_all()
    await ctx.send("Cleared all chat history")

@bot.command()
async def chat(ctx):
    # Remove command prefix and command name
    message = sanitize_message(ctx.message.content, 'greeting')
    ret = chatgpt.chat(message, ctx.message.author.id)
    await ctx.send(ret)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('-'):
        await bot.process_commands(message)
        return

bot.run(DISCORD_TOKEN)
