
#########################################
############# Core Commands #############
#########################################

import discord
import asyncio
import random
import json
from discord.ext import commands

class Core():
    def __init__(self, bot):
        self.bot = bot

#help command (-help)
    @commands.command(pass_context = True, aliases=['h'])
    async def help(self, ctx):
        embed = discord.Embed(title="Command List for Kyoto!", colour=discord.Colour(0xcd4bb6), description="By default all commands have the ``-`` prefix. \nIf your server admin changed the prefix, then stick to that prefix!\n**Don't include the example brackets when using the commands!**⠀\n⠀")
        embed.add_field(name="Core Commands", value="`-help`⠀`-invite`⠀`-ls` or `-listservers`⠀`-si` or `-serverinfo`\n", inline=False)
        embed.add_field(name="Kawaii Commands", value="`-hug [@mention]`⠀`-poke [@mention]`⠀`-wave [@mention]`⠀`-hide [@mention]`⠀\n`-blush`⠀`-shine`⠀`-happy`\n", inline=False)
        embed.add_field(name="Voice Commands", value="`-connect`⠀`-disconnect`\n", inline=False)
        embed.add_field(name="Administrator Commands", value="`-clear [amount]`⠀`-ban [@mention]`⠀`-getbans`⠀`-kick [@mention]`", inline=False)
        await self.bot.send_message(ctx.message.author, embed = embed),

        embed = discord.Embed(description = "**"+ctx.message.author.mention +" a personal message with all my commands is on the way!** :heart:", color = 13454262)
        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

#invite command (-invite)
    @commands.command(pass_context = True)
    async def invite(self, ctx):
        embed = discord.Embed(title = "**Invite Kyoto to your server!**", description = "You want to invite **Kyoto** to your server?\nThen you can use this link to invite him!\n\n[Click here to invite **Kyoto**](https://discordapp.com/oauth2/authorize?client_id=365240645419270145&scope=bot&permissions=527952983)", color = 13454262)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/365240645419270145/3f6527890a2b55b1eb864dd0113e0589.png")
        await self.bot.send_message(ctx.message.author, embed = embed)

        embed = discord.Embed(description = "**"+ctx.message.author.mention +" a personal message with the bot invite is on the way!** :heart:", color = 13454262)
        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

#listservers command (-listservers)
    @commands.command(pass_context = True, aliases=['ls'])
    async def listservers(self, ctx):
        x = '\n'.join([str(server) for server in client.servers])
        print(x)
        embed = discord.Embed(title = "Servers", description = x, color = 13454262)
        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

#server command (-server)
    @commands.command(pass_context = True, aliases=['si'])
    async def serverinfo(self, ctx):
        server = ctx.message.server
        channelz = len(server.channels)
        time = str(server.created_at); time = time.split(' '); time= time[0];
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles);    

        embed = discord.Embed(colour = 13454262)
        embed.set_thumbnail(url = server.icon_url);
        embed.set_author(name = "Server Information", icon_url = "http://icons.iconarchive.com/icons/graphicloads/100-flat/128/information-icon.png")

        embed.add_field(name="Server Name:", value = str(server), inline=True)
        embed.add_field(name="Server ID:", value = str(server.id), inline=True)
        embed.add_field(name="Server Owner:", value = str(server.owner), inline=True)
        embed.add_field(name="Server Owner ID:", value = server.owner.id, inline=True)
        embed.add_field(name="Members:", value = str(server.member_count), inline=True)
        embed.add_field(name="Text & Voice Channels:", value = str(channelz), inline=True)
        embed.add_field(name="Server Region:", value = '%s'%str(server.region), inline=True)
        embed.add_field(name="Server Roles:", value = '%s'%str(role_length), inline=True)
        embed.set_footer(text ='Server Created: %s'%time);

        await self.bot.say(embed = embed)
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Core(bot))