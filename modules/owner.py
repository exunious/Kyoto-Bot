########################################
############ Owner Commands ############
########################################

import discord
from discord.ext import commands
from config import bot_owner
from config import embed_color

class Owner():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def game(self, ctx, *, game = None):

		server = ctx.guild
		current_status = ctx.me.status if server is not None else None

		if ctx.author.id == bot_owner:
			await self.bot.change_presence(game=discord.Game(name=game),status=current_status)
			embed = discord.Embed(description = "**"+ctx.author.name +"** my **Now Playing** was succesfully changed!", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()
		
		else:
			embed = discord.Embed(description = "**"+ctx.author.name +"** you're not allowed to change my **Now Playing**", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()
            
def setup(bot):
    bot.add_cog(Owner(bot))