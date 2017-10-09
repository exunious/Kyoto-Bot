#########################################
############ Kawaii Commands ############
#########################################

import discord
import random
from data.kawaii import *
from extra.config import *
from discord.ext import commands

class Kawaii():
    def __init__(self, bot):
        self.bot = bot

#hug command (-hug [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def hug(self, ctx, *, member : discord.Member = None):

        if not member:
            choice = random.choice(hugs)
            embed = discord.Embed(description = "**"+ ctx.author.mention +" you got hugged by" + self.bot.user.mention + "**", color = embed_color)
            embed.set_image(url = "{}".format(choice))
            await ctx.send(embed = embed)
            await ctx.message.delete()

        else:
            choice = random.choice(hugs) 
            embed = discord.Embed(description = "**%s you got hugged by "%member.mention + ctx.author.mention +"**", color = embed_color)
            embed.set_image(url = "{}".format(choice))
            await ctx.send(embed = embed)
            await ctx.message.delete()

#poke command (-poke [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def poke(self, ctx, *, member : discord.Member = None):

        if not member:
            choice = random.choice(pokes) 
            embed = discord.Embed(description = "**" + ctx.author.mention + " pokes " + self.bot.user.mention + "**", color = embed_color)
            embed.set_image(url = "{}".format(choice))
            await ctx.send(embed = embed)
            await ctx.message.delete()
        
        else:
            choice = random.choice(pokes) 
            embed = discord.Embed(description = "**%s you got poked by "%member.mention + ctx.author.mention + "**", color = embed_color)
            embed.set_image(url = "{}".format(choice))
            await ctx.send(embed = embed)
            await ctx.message.delete()
  
#wave command (-wave [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def wave(self, ctx, *, member : discord.Member = None):

        if not member:
            embed = discord.Embed(description = "**"+ ctx.author.mention +"** waves to **<@!365240645419270145>**", color = embed_color)
            embed.set_image(url="https://i.imgur.com/w5kTICt.gif")
            await ctx.send(embed = embed)
            await ctx.message.delete()

        else:
            embed = discord.Embed(description = "**"+ ctx.author.mention +"** waves at you **%s**"%member.mention, color = embed_color)
            embed.set_image(url="https://i.imgur.com/w5kTICt.gif")
            await ctx.send(embed = embed)
            await ctx.message.delete()

#hide command (-hide [@mention])
    @commands.command(pass_context = True, no_pm = True)
    async def hide(self, ctx, *, member : discord.Member = None):

        if not member:
            embed = discord.Embed(description = "**"+ ctx.author.mention +"** hides for **<@!365240645419270145>**", color = embed_color)
            embed.set_image(url="https://i.imgur.com/BZQwbid.gif")
            await ctx.send(embed = embed)
            await ctx.message.delete()

        else:
            embed = discord.Embed(description = "**"+ ctx.author.mention +"** hides for **%s**"%member.mention, color = embed_color)
            embed.set_image(url="https://i.imgur.com/BZQwbid.gif")
            await ctx.send(embed = embed)
            await ctx.message.delete()

#blush command (-blush)
    @commands.command(pass_context = True, no_pm = True)
    async def blush(self, ctx):

        embed = discord.Embed(description = "**"+ ctx.author.mention +"** blushes", color = embed_color)
        embed.set_image(url="https://i.imgur.com/DGhgJ1R.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()
        
#shine command (-shine)
    @commands.command(pass_context = True, no_pm = True)
    async def shine(self, ctx):

        embed = discord.Embed(description = "**"+ ctx.author.mention +"** shines", color = embed_color)
        embed.set_image(url="https://i.imgur.com/VUuoZfa.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#happy command (-happy)
    @commands.command(pass_context = True, no_pm = True)
    async def happy(self, ctx):

        embed = discord.Embed(description = "**"+ ctx.author.mention +"** is super happy!", color = embed_color)
        embed.set_image(url="https://i.imgur.com/4xSrwsj.gif")
        await ctx.send(embed = embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Kawaii(bot))