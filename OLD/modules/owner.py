########################################
############ Owner Commands ############
########################################

import discord
import random
from discord.ext import commands
from config import bot_owner
from config import embed_color

class Owner():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def game(self, ctx, *, game = None):

		server = ctx.message.server
		current_status = server.me.status if server is not None else None

		if ctx.message.author.id == bot_owner:
			await self.bot.change_presence(game=discord.Game(name=game),status=current_status)
			embed = discord.Embed(description = "**"+ctx.message.author.name +"** my **Now Playing** was succesfully changed!", color = embed_color)
			await self.bot.say(embed = embed)
			await self.bot.delete_message(ctx.message)
		
		else:
			embed = discord.Embed(description = "**"+ctx.message.author.name +"** you're not allowed to change my **Now Playing**", color = embed_color)
			await self.bot.say(embed = embed)
			await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Owner(bot))