########################################
############ Admin Commands ############
########################################

import discord
import random
from discord.ext import commands
from config import *

class Admin():
	def __init__(self, bot):
		self.bot = bot

########################################
############ Role  Commands ############
########################################

	@commands.command(no_pm = True, aliases = ['rr'])
	async def removerole(self, ctx, user: discord.Member, *, role):
			if ctx.author.guild_permissions.manage_roles:
				await user.remove_roles(discord.utils.get(ctx.message.guild.roles, name=role))
				embed = discord.Embed(title = "Remove Role!", description = "**" + ctx.author.name + "** succesfully removed a role from **{}**".format(user), color = embed_color_succes)
				embed.add_field(name="Removed Role: ", value = "{}".format(role))
				await ctx.send(embed = embed)
			else:
				embed = discord.Embed(description = "**"+ ctx.author.name +"** you're not allowed to do this!", color = embed_color_error)
				await ctx.send(embed = embed)

	@commands.command(no_pm = True, aliases = ['sr'])
	async def setrole(self, ctx, user: discord.Member, *, role):
			if ctx.author.guild_permissions.manage_roles:
				await user.add_roles(discord.utils.get(ctx.message.guild.roles, name=role))
				embed = discord.Embed(title = "Set Role!", description = "**" + ctx.author.name + "** succesfully set a role to **{}**".format(user), color = embed_color_succes)
				embed.add_field(name="Set Role: ", value = "{}".format(role))
				await ctx.send(embed = embed)
			else:
				embed = discord.Embed(description = "**"+ ctx.author.name +"** you're not allowed to do this!", color = embed_color_error)
				await ctx.send(embed = embed)

########################################

def setup(bot):
    bot.add_cog(Admin(bot))