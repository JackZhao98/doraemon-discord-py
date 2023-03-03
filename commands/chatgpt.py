from discord.ext import commands
from utils.openai.ChatGPT import OpenAIChat
from utils.utils import *

class ChatGPT(commands.Cog):
    """Chat with Doraemon Discord bot!"""
    def __init__(self, key, org):
        self.chatgpt = OpenAIChat(key, org)
        self.chatgpt.clear_all()


    @commands.command()
    async def clear(self, ctx):
        """Clear your own chat history"""
        self.chatgpt.clear_message(ctx.message.author.id)
        await ctx.send(f"Cleared message for {ctx.message.author.name}")

    @commands.command()
    async def clearAll(self, ctx):
        """[DANGER] Clear all chat history"""
        self.chatgpt.clear_all()
        await ctx.send("Cleared all chat history")

    @commands.command(name='chat', aliases=['c'])
    async def chat(self, ctx):
        """Chat with ChatGPT. You can also use `c` as an alias."""
        # Remove command prefix and command name
        async with ctx.typing():
            message = sanitize_message(ctx.message.content, 'chat')
            ret = self.chatgpt.chat(message, ctx.message.author.id)
            await ctx.send(ret)