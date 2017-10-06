########################################
############ Owner Commands ############
########################################

import discord
from discord.ext import commands
from config import bot_owner
from config import embed_color

class Owner:
	def __init__(self, bot):
		self.bot = bot

### Load Command ###
	@commands.command(name = 'modload', pass_context = True, aliases = ['ml'])
	async def modload(self, ctx, *, extension_name : str = None):

		if extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.message.author.name +"** you need to tell me what to load!", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		else:
			try:
				self.bot.load_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully loaded.".format(extension_name), color = embed_color)
				await ctx.send(embed = embed)
				await ctx.message.delete()
			except (ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color)
				await ctx.send(embed = embed)
				await ctx.message.delete()
            
### Unload Command ###
	@commands.command(name = 'modunload', pass_context = True, aliases = ['mu'])
	async def modunload(self, ctx, *, extension_name : str = None):

		if extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to unload!", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		else:
			try:
				self.bot.unload_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully unloaded.".format(extension_name), color = embed_color)
				await ctx.send(embed = embed)
				await ctx.message.delete()
			except (ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color)
				await ctx.send(embed = embed)
				await ctx.message.delete()

#########################################

	@commands.command(name = 'setgame', pass_context=True, aliases = ['sg'])
	async def setgame(self, ctx, *, game = None):

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