#########################################
############ Kawaii Commands ############
#########################################

import discord
import random
from discord.ext import commands
from config import embed_color

class Kawaii():
    def __init__(self, bot):
        self.bot = bot

#hug command (-hug [@mention])
    @commands.command(pass_context = True)
    async def hug(self, ctx, *, member : discord.Member = None):

        if not member:
            embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** you got hugged by **<@!365240645419270145>**", color = embed_color)
            embed.set_image(url="https://media.tenor.com/images/08de7ad3dcac4e10d27b2c203841a99f/tenor.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)

        else:    
            embed = discord.Embed(description = "**%s** you got hugged by **"%member.mention + ctx.message.author.mention +"**", color = embed_color)
            embed.set_image(url="http://i.imgur.com/cLHRyeB.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)

#poke command (-poke [@mention])
    @commands.command(pass_context = True)
    async def poke(self, ctx, *, member : discord.Member = None):

        if not member:
            embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** pokes **<@!365240645419270145>**", color = embed_color)
            embed.set_image(url="https://i.imgur.com/kXBD83W.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)
        
        else:
            embed = discord.Embed(description = "**%s** you got poked by **"%member.mention + ctx.message.author.mention +"**", color = embed_color)
            embed.set_image(url="https://i.imgur.com/kXBD83W.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)
  
#wave command (-wave [@mention])
    @commands.command(pass_context = True)
    async def wave(self, ctx, *, member : discord.Member = None):

        if not member:
            embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** waves to **<@!365240645419270145>**", color = embed_color)
            embed.set_image(url="https://i.imgur.com/w5kTICt.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)

        else:
            embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** waves at you **%s**"%member.mention, color = embed_color)
            embed.set_image(url="https://i.imgur.com/w5kTICt.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)

#hide command (-hide [@mention])
    @commands.command(pass_context = True)
    async def hide(self, ctx, *, member : discord.Member = None):

        if not member:
            embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** hides for **<@!365240645419270145>**", color = embed_color)
            embed.set_image(url="https://i.imgur.com/BZQwbid.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)

        else:
            embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** hides for **%s**"%member.mention, color = embed_color)
            embed.set_image(url="https://i.imgur.com/BZQwbid.gif")
            await self.bot.say(embed = embed)
            await self.bot.delete_message(ctx.message)

#blush command (-blush)
    @commands.command(pass_context = True)
    async def blush(self, ctx):

        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** blushes", color = embed_color)
        embed.set_image(url="https://i.imgur.com/DGhgJ1R.gif")
        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

#shine command (-shine)
    @commands.command(pass_context = True)
    async def shine(self, ctx):

        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** shines", color = embed_color)
        embed.set_image(url="https://i.imgur.com/VUuoZfa.gif")
        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

#happy command (-happy)
    @commands.command(pass_context = True)
    async def happy(self, ctx):

        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** is super happy!", color = embed_color)
        embed.set_image(url="https://i.imgur.com/4xSrwsj.gif")
        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Kawaii(bot))