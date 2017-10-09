###########################################
############## Error Handler ##############
###########################################

import discord
from extra.config import *
from discord.ext import commands

class ErrorHandler:
	def __init__(self, bot):
		self.bot = bot

	async def on_command_error(self, ctx, error):
			if isinstance (error, commands.CommandNotFound):
				embed = discord.Embed(title = "Command not found!", description = "**" + ctx.author.name + "**, for a list with all my commands please use: `-help` or `-h`", color = embed_color_error)
				embed.add_field(name="Command Used: ", value = ctx.message.content)
				await ctx.send(embed = embed)

			elif isinstance (error, commands.MissingPermissions):
				embed = discord.Embed(description = "**"+ ctx.author.name +"**, you're not allowed to do this!", color = embed_color_error)
				await ctx.send(embed = embed)

			elif isinstance(error, commands.NotOwner):
				embed = discord.Embed(description = "**"+ ctx.author.name +"**, you think you're my boss?", color =embed_color_error)
				await ctx.send(embed = embed)

			try:
				await ctx.message.delete()
			except:
				pass

				if isinstance (error, commands.BotMissingPermissions):
					pass

#			else:
#				#  All other Errors not returned come here... And we can just print the default TraceBack.
#				print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
#				traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
	bot.add_cog(ErrorHandler(bot))