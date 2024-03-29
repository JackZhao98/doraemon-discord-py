from discord.ext import commands
from utils.openai.open_ai_chat import OpenAIChat
from utils.utils import *

class DoraemonChatBot(commands.Cog):
    """Chat with Doraemon Discord bot!"""
    def __init__(self, key, org, model):
        self.chatgpt = OpenAIChat(key, org, model)
        self.chatgpt.clear_all()
    
    @commands.command()
    async def gpt_info(self, ctx):
        """Display current Chat-GPT model"""
        await ctx.send(f"老子是哆啦A梦，现在正在使用：{self.chatgpt.model}")

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
            message = sanitize_message(ctx.message.content, 'chat', prefix='-', aliases=['c'])
            try:
                async def send_message(message):
                    return await ctx.send(message)
                print(message)
                # ret = self.chatgpt.chat(message, ctx.message.author.id)
                message_ctx = await ctx.send("正在思考中...")
                ret = await self.chatgpt.chat_v2(message, ctx.message.author.id, message_ctx)
                if ret != "" and ret != None:
                    await ctx.send(ret)
            except Exception as e:
                print (e)
                await ctx.send("结果超时，可能问题过长")
