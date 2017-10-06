######################################
############ Fun Commands ############
######################################

import discord
import random
from discord.ext import commands
from config import embed_color

class Fun():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context = True, aliases=['8ball'])
	async def eightball(self, ctx, *, question : str = None):

		if question == None:
			embed = discord.Embed(description = "**"+ ctx.message.author.name +"** you first need to ask me something! Duhh", color = embed_color)
			await self.bot.say(embed=embed)
			await self.bot.delete_message(ctx.message)

		else:
			result = ["Neko", "Loli", "Kitsune"]
			choice = random.choice(result)
			embed = discord.Embed(colour = embed_color)
			embed.set_thumbnail(url = ctx.message.author.avatar_url)
			embed.add_field(name="**"+ctx.message.author.name +"** asks:", inline=False, value="{}".format(question))
			embed.add_field(name="**Holy 8ball** answers:", inline=False, value="{}".format(choice))
			await self.bot.say(embed=embed)
			await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Fun(bot))