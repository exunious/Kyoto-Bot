###########################################
############## Error Handler ##############
###########################################

import discord
from discord.ext import commands

class ErrorHandler:
	def __init__(self, bot):
		self.bot = bot

	async def on_command_error(self, ctx, error):
			if isinstance (error, commands.CommandNotFound):
				embed = discord.Embed(title = "Command not found!", description = "**" + ctx.author.name + "** for a list with all my commands please use: `-help` or `-h`", color = 13434880)
				embed.add_field(name="Command Used: ", value = ctx.message.content)
				await ctx.send(embed = embed)
			try:
				await ctx.message.delete()
			except:
				pass

				if isinstance (error, commands.BotMissingPermissions):
					pass

def setup(bot):
	bot.add_cog(ErrorHandler(bot))