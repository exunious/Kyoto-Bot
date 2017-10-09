########################################
############ Owner Commands ############
########################################

import discord
from discord.ext import commands
from config import *

class Owner:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'shutdown', hidden = True, no_pm = True, aliases = ['sd'])
	async def shutdown(self, ctx):
		if ctx.author.id == bot_owner:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** Bye bye, cry cry! ", color = embed_color_succes)
			await ctx.send(embed = embed)
			await self.bot.logout()

		elif ctx.author.id is not bot_owner:		
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you're not allowed to do this!", color = embed_color_error)
			await ctx.send(embed = embed)
			await ctx.message.delete()

### Load Module Command ###
	@commands.command(name = 'modload', hidden=True, no_pm = True, aliases = ['ml'])
	async def modload(self, ctx, *, extension_name : str = None):
		
		if ctx.author.id == bot_owner and extension_name is not None:
			try:
				self.bot.load_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully loaded.".format(extension_name), color = embed_color_succes)
				await ctx.send(embed = embed)
				await ctx.message.delete()
			except (AttributeError, ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color_error)
				await ctx.send(embed = embed)
				await ctx.message.delete()

		elif extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to load!", color = embed_color_attention)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		elif ctx.author.id is not bot_owner:		
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you're not allowed to do this!", color = embed_color_error)
			await ctx.send(embed = embed)
			await ctx.message.delete()
		else:
			pass
            
### Unload Module Command ###
	@commands.command(name = 'modunload', hidden=True, no_pm = True, aliases = ['mu'])
	async def modunload(self, ctx, *, extension_name : str = None):
		
		if ctx.author.id == bot_owner and extension_name is not None:
			try:
				self.bot.unload_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully unloaded.".format(extension_name), color = embed_color_succes)
				await ctx.send(embed = embed)
				await ctx.message.delete()
			except (AttributeError, ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color_error)
				await ctx.send(embed = embed)
				await ctx.message.delete()

		elif extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to unload!", color = embed_color_attention)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		elif ctx.author.id is not bot_owner:		
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you're not allowed to do this!", color = embed_color_error)
			await ctx.send(embed = embed)
			await ctx.message.delete()
		else:
			pass

### Reload Module Command ###
	@commands.command(name = 'modreload', hidden=True, no_pm = True, aliases = ['mr'])
	async def modreload(self, ctx, *, extension_name : str = None):
		
		if ctx.author.id == bot_owner and extension_name is not None:
			try:
				self.bot.unload_extension(extension_name)
				self.bot.load_extension(extension_name)
				embed = discord.Embed(description = "**"+ ctx.author.name +" **the module** {} **was successfully reloaded.".format(extension_name), color = embed_color_succes)
				await ctx.send(embed = embed)
				await ctx.message.delete()
			except (AttributeError, ImportError) as e:
				embed = discord.Embed(description = "**"+ ctx.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color_error)
				await ctx.send(embed = embed)
				await ctx.message.delete()

		elif extension_name == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me what to reload!", color = embed_color_attention)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		elif ctx.author.id is not bot_owner:		
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you're not allowed to do this!", color = embed_color_error)
			await ctx.send(embed = embed)
			await ctx.message.delete()
		else:
			pass

### Still busy with ###
#	@commands.command(name = 'setrole', hidden=True, no_pm = True, aliases = ['sr'])
#	async def setrole(self, ctx, *, member : discord.member = None, role : str = None):
#
#		if ctx.author.id ==  and extension_name is not None:
#
#role = discord.utils.get(server.roles, name="admin")
#await client.add_roles(member, role)

#########################################

	@commands.command(name = 'setgame', pass_context=True, no_pm = True, aliases = ['sg'])
	async def setgame(self, ctx, *, game = None):

		server = ctx.guild
		current_status = ctx.me.status if server is not None else None

		if ctx.message.author.id == bot_owner:
			await self.bot.change_presence(game=discord.Game(name=game),status=current_status)
			embed = discord.Embed(description = "**"+ctx.author.name +"** my **Now Playing** was succesfully changed!", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()
		
		else:
			embed = discord.Embed(description = "**"+ctx.author.name +"** you're not allowed to change my **Now Playing**", color = embed_color_error)
			await ctx.send(embed = embed)
			await ctx.message.delete()

def setup(bot):
    bot.add_cog(Owner(bot))