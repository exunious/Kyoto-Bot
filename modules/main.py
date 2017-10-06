import discord
import asyncio
import random
import json
from discord.ext import commands

# this specifies what extensions to load when the bot starts up
startup_extensions = ["core", "members"]

bot = discord.Client()
bot_prefix = "-" #default prefix
embed_color = 13454262 #default embed color
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print("Name: {}".format(bot.user.name))
    print("Prefix: {}".format(bot_prefix))
    print("ID: {}".format(bot.user.id))
    print('------')

#########################################
############## Load/Unload ##############
#########################################

### Load Command ###
@bot.command(pass_context = True)
async def load(ctx, *, extension_name : str = None):

    if extension_name == None:
        embed = discord.Embed(description = "**"+ ctx.message.author.name +"** you need to tell me what to load!", color = embed_color)
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)

    else:
        try:
            bot.load_extension(extension_name)
            embed = discord.Embed(description = "**"+ ctx.message.author.name +" **the module** {} **was successfully loaded.".format(extension_name), color = embed_color)
            await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
        except (ImportError) as e:
            embed = discord.Embed(description = "**"+ ctx.message.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color)
            await bot.say(embed=embed)
            await bot.delete_message(ctx.message)

### Unload Command ###
@bot.command(pass_context = True)
async def unload(ctx, *, extension_name : str = None):

    if extension_name == None:
        embed = discord.Embed(description = "**"+ ctx.message.author.name +"** you need to tell me what to unload!", color = embed_color)
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)

    else:
        try:
            bot.unload_extension(extension_name)
            embed = discord.Embed(description = "**"+ ctx.message.author.name +" **the module** {} **was successfully unloaded.".format(extension_name), color = embed_color)
            await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
        except (ImportError) as e:
            embed = discord.Embed(description = "**"+ ctx.message.author.name +" {}:** *{}*".format(type(e).__name__, str(e)), color = embed_color)
            await bot.say(embed=embed)
            await bot.delete_message(ctx.message)

#########################################

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run('MzY1MjQwNjQ1NDE5MjcwMTQ1.DLbgxg.1YZ1I8mqliOBd8ESKh_0iBiU_cc')