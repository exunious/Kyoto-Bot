#########################################
############# Core Commands #############
#########################################

from extra.config import *
from discord.ext import commands
from collections import Counter
from utils import checks, formats
from utils.paginator import HelpPaginator, CannotPaginate
from collections import OrderedDict, deque, Counter

#from .utils import checks, db

import utils.checks
import utils.db
import logging
import discord
import asyncio
import datetime
import traceback
import copy
import unicodedata
import inspect
import psutil
import os

class Core:
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()

#invite command (-invite)
    @commands.command(pass_context = True, no_pm = True)
    async def invite(self, ctx):
        embed = discord.Embed(title = "**Invite Noëlla to your server!**", description = "You want to invite **Noëlla** to your server?\nThen you can use this link to invite him!\n\n[Click here to invite **Noëlla**](https://discordapp.com/oauth2/authorize?client_id=357852849029513216&scope=bot&permissions=527952983)", color = embed_color)
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

#        embed = discord.Embed(description = "**"+ctx.author.name +" a personal message with the bot invite is on the way!** :heart:", color = embed_color)
#        await ctx.send(embed = embed)
#        await ctx.message.delete()

### List Servers Command ###
    @commands.command(aliases = ['ls'])
    async def listservers(self, ctx, number : int = 10):

        e = discord.Embed(colour = embed_color)
        if number > 50:
            number = 50
        if number < 1:
            await ctx.channel.send('Oookay - look!  No servers!  Just like you wanted!')
            return
        i = 1
        for guild in self.bot.guilds:
            if i > number:
                break
            tmembers = guild.member_count
            vchannels = guild.voice_channels
            tchannels = guild.text_channels
            omembers = sum(m.status is discord.Status.online for m in guild.members)
            e.add_field(name = guild.name, value = f"Server Owner: **{guild.owner.name}#{guild.owner.discriminator}**\nOnline Members: **{omembers}** - Total Members: **{tmembers}**\nText Channels: **"+ str(len(tchannels)) +"** - Voice Channels: **"+ str(len(vchannels)) +"**", inline = False)
            i += 1
        await ctx.channel.send(embed = e)
        await ctx.message.delete()

### Server Information Command ###
    @commands.command(pass_context = True, no_pm = True, aliases=['si'])
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

    """@commands.command(hidden=True)
    async def socketstats(self, ctx):
        delta = datetime.datetime.utcnow() - self.bot.uptime
        minutes = delta.total_seconds() / 60
        total = sum(self.bot.socket_stats.values())
        cpm = total / minutes
        await ctx.send(f'{total} socket events observed ({cpm:.2f}/minute):\n{self.bot.socket_stats}')

    def get_bot_uptime(self, *, brief=False):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command()
    async def uptime(self, ctx):

        await ctx.send(f'Uptime: **{self.get_bot_uptime()}**')"""

    @commands.command()
    async def about(self, ctx):
        """Tells you information about the bot itself."""
        cmd = r'git show -s HEAD~3..HEAD --format="[{}](https://github.com/exunious/Kyoto-Bot/commit/%H) %s (%cr)"'
        if os.name == 'posix':
            cmd = cmd.format(r'\`%h\`')
        else:
            cmd = cmd.format(r'`%h`')

        revision = os.popen(cmd).read().strip()
        embed = discord.Embed(description='⠀\n**Latest Changes**\n' + revision + '\n⠀')
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

        embed.add_field(name='Members in Guilds', value=f'Total Users: **{total_members}**\nTotal Unique: **{total_unique}**\nTotal Online: **{total_online}**')
        embed.add_field(name='Channels in Guilds', value=f'Total Channels: **{text + voice}**\nText Channels: **{text}**\nVoice Channels: **{voice}**')

        memory_usage = self.process.memory_full_info().uss / 1024**2
        cpu_usage = self.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU')


        embed.add_field(name='Active in Guilds', value = len(self.bot.guilds))
#        embed.add_field(name='Commands Run', value=sum(self.bot.command_stats.values()))
#        embed.add_field(name='Uptime', value=self.get_bot_uptime(brief=True))
        embed.set_footer(text='writen in discord.py', icon_url='http://i.imgur.com/5BFecvA.png')
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Core(bot))