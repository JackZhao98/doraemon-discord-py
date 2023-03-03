from discord.ext import commands
from utils.utils import *

class Music(commands.Cog):
    """Music player"""
    
    @commands.command()
    async def play(self, ctx):
        """Play music"""
        await ctx.send("Playing music")
    
    @commands.command()
    async def stop(self, ctx):
        """Stop music"""
        await ctx.send("Stopping music")

    @commands.command()
    async def queue(self, ctx):
        """Show music queue"""
        await ctx.send("Showing music queue")
    
    @commands.command()
    async def skip(self, ctx):
        """Skip music"""
        await ctx.send("Skipping music")
    
    @commands.command()
    async def pause(self, ctx):
        """Pause music"""
        await ctx.send("Pausing music")

    @commands.command()
    async def resume(self, ctx):
        """Resume music"""
        await ctx.send("Resuming music")
    
    @commands.command()
    async def volume(self, ctx):
        """Change volume"""
        await ctx.send("Changing volume")
    
    @commands.command()
    async def shuffle(self, ctx):
        """Shuffle music queue"""
        await ctx.send("Shuffling music queue")
    
    @commands.command()
    async def remove(self, ctx):
        """Remove music from queue"""
        await ctx.send("Removing music from queue")
    
    @commands.command()
    async def clearQueue(self, ctx):
        """Clear music queue"""
        await ctx.send("Clearing music queue")
    