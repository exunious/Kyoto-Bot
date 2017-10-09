######################################
############ Fun Commands ############
######################################

import discord
import random
from discord.ext import commands
from extra.config import embed_color

class Fun():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context = True, no_pm = True, aliases=['8ball'])
	async def eightball(self, ctx, *, question : str = None):

		if question == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you first need to ask me something! Duhh", color = embed_color)
			await ctx.send(embed=embed)
			await ctx.message.delete()

		else:
			result = ["Neko", "Loli", "Kitsune"]
			choice = random.choice(result)
			embed = discord.Embed(colour = embed_color)
			embed.set_thumbnail(url = ctx.author.avatar_url)
			embed.add_field(name="**"+ctx.author.name +"** asks:", inline=False, value="{}".format(question))
			embed.add_field(name="**Holy 8ball** answers:", inline=False, value="{}".format(choice))
			await ctx.send(embed=embed)
			await ctx.message.delete()

	@commands.command(pass_context = True, no_pm = True, aliases = ['hub'])
	async def discordhub(self, ctx, *, member : discord.Member = None):

		author = ctx.author

		if not member:
			member = author
		
		embed = discord.Embed(title="Click here to visit *%s* profile!"%member.name, colour = embed_color, url="https://discordhub.com/profile/%s"%member.id, description="DiscordHub aims to provide a centralized platform for Discord\nby providing features such as user accounts and a public server list.")
		embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/4.png")
		embed.set_author(name="%s Profile!"%member.name, icon_url="https://cdn.discordapp.com/embed/avatars/4.png")
		await ctx.send(embed=embed)
		await ctx.message.delete()

	@commands.command(no_pm = True, aliases=['osu'])
	async def osustats(self, ctx, *, osuplayer : str = None):

		if osuplayer == None:
			embed = discord.Embed(description = "**"+ ctx.author.name +"** you need to tell me a username!", color = embed_color)
			await ctx.send(embed = embed)
			await ctx.message.delete()

		else:
			#embed.set_thumbnail(url = ctx.author.avatar_url)
			embed = discord.Embed(color = embed_color)
			embed.set_author(name = f"{osuplayer}'s Stats", url = f"https://osu.ppy.sh/u/{osuplayer}", icon_url = "https://s.ppy.sh/images/head-logo.png")
			embed.set_footer(text = "Images provided by lemmmy.pw/osusig")
			embed.set_image(url = f"http://lemmmy.pw/osusig/sig.php?colour=hexff66aa&uname={osuplayer}&pp=1&countryrank&flagshadow&flagstroke&opaqueavatar&avatarrounding=5&onlineindicator=undefined&xpbar&xpbarhex")
			#embed.add_field(name="**"+ctx.author.name +"** asks:", inline=False, value="{}".format(question))
			#embed.add_field(name="**Holy 8ball** answers:", inline=False, value="{}".format(choice))
			await ctx.send(embed = embed)
			await ctx.message.delete()

def setup(bot):
    bot.add_cog(Fun(bot))