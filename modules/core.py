#########################################
############# Core Commands #############
#########################################

from config import embed_color
from config import bot_owner
from discord.ext import commands
from collections import Counter

#from .utils import checks, db

import utils.checks
import utils.db
import logging
import discord
import datetime
import traceback
import psutil
import os

class Core:
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()

#invite command (-invite)
    @commands.command(pass_context = True)
    async def invite(self, ctx):
        embed = discord.Embed(title = "**Invite Kyoto to your server!**", description = "You want to invite **Kyoto** to your server?\nThen you can use this link to invite him!\n\n[Click here to invite **Kyoto**](https://discordapp.com/oauth2/authorize?client_id=365240645419270145&scope=bot&permissions=527952983)", color = embed_color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/365240645419270145/3f6527890a2b55b1eb864dd0113e0589.png")
        await ctx.author.send(embed = embed)

        embed = discord.Embed(description = "**"+ctx.author.name +" a personal message with the bot invite is on the way!** :heart:", color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

#listservers command (-listservers)
    @commands.command(pass_context = True, aliases=['ls'])
    async def listservers(self, ctx):
        x = '\n'.join([str(server) for server in self.bot.guilds])
        print(x)
        embed = discord.Embed(title = "Servers", description = x, color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

#server command (-server)
    @commands.command(pass_context = True, aliases=['si'])
    async def serverinfo(self, ctx):
        vchannels = ctx.guild.voice_channels
        tchannels = ctx.guild.text_channels
        tmembers = ctx.guild.member_count
        omembers = sum(m.status is discord.Status.online for m in ctx.guild.members)
        time = str(ctx.guild.created_at); time = time.split(' '); time= time[0];
        roles = [x.name for x in ctx.guild.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles);    

        embed = discord.Embed(colour = embed_color)
        embed.set_thumbnail(url = ctx.guild.icon_url);
        embed.set_author(name = "Server Information", icon_url = "http://icons.iconarchive.com/icons/graphicloads/100-flat/128/information-icon.png")

        embed.add_field(name="Server Name:", value = str(ctx.guild), inline=True)
        embed.add_field(name="Server ID:", value = str(ctx.guild.id), inline=True)
        embed.add_field(name="Server Owner:", value = str(ctx.guild.owner), inline=True)
        embed.add_field(name="Server Owner ID:", value = ctx.guild.owner.id, inline=True)
        embed.add_field(name="Member Count:", value = f'Members Online: **{omembers}**\nMembers Total: **{tmembers}**', inline=True)
        embed.add_field(name="Channels Count:", value = "Text Channels: **"+ str(len(tchannels)) +"** \nVoice Channels: **"+ str(len(vchannels)) +"**", inline=True)
        embed.add_field(name="Server Region:", value = '%s'%str(ctx.guild.region), inline=True)
        embed.add_field(name="Server Roles:", value = '%s'%str(role_length), inline=True)
        embed.set_footer(text ='Server Created: %s'%time);

        await ctx.send(embed = embed)
        await ctx.message.delete()

    @commands.command()
    async def about(self, ctx):
        """Tells you information about the bot itself."""
        cmd = r'git show -s HEAD~3..HEAD --format="[{}](https://github.com/exunious/Kyoto-Bot/commit/%H) %s (%cr)"'
        if os.name == 'posix':
            cmd = cmd.format(r'\`%h\`')
        else:
            cmd = cmd.format(r'`%h`')

        revision = os.popen(cmd).read().strip()
        embed = discord.Embed(description='⠀\nLatest Changes:\n' + revision + '\n⠀')
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        embed.title = 'Official Bot Server Invite'
        embed.url = 'https://discord.gg/FaqVEMy'
        embed.colour = embed_color

        owner = self.bot.get_user(bot_owner)
        embed.set_author(name=str(owner), icon_url=owner.avatar_url)

        # statistics
        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)

        voice_channels = []
        text_channels = []
        for guild in self.bot.guilds:
            voice_channels.extend(guild.voice_channels)
            text_channels.extend(guild.text_channels)

        text = len(text_channels)
        voice = len(voice_channels)

        embed.add_field(name='Members in Guilds', value=f'{total_members} total\n{total_unique} unique\n{total_online} unique online')
        embed.add_field(name='Channels in Guilds', value=f'{text + voice} total\n{text} text\n{voice} voice')

        memory_usage = self.process.memory_full_info().uss / 1024**2
        cpu_usage = self.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU')


        embed.add_field(name='Active in Guilds', value = len(self.bot.guilds))
#        embed.add_field(name='Commands Run', value=sum(self.bot.command_stats.values()))
#        embed.add_field(name='Uptime', value=self.get_bot_uptime(brief=True))
        embed.set_footer(text='Made with discord.py', icon_url='http://i.imgur.com/5BFecvA.png')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))