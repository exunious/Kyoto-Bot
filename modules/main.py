import discord
import datetime
from time import time
from discord.ext import commands
from extra.config import *

# this specifies what extensions to load when the bot starts up
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print("Name: {}".format(bot.user.name))
    print("Prefix: {}".format(bot_prefix))
    print("ID: {}".format(bot.user.id))
    print('------')

##########################################
############## Help Command ##############
##########################################

#help command (-help)
    @bot.command(pass_context = True, aliases=['h'])
    async def help(ctx):
        embed = discord.Embed(title=f"Command List for {bot.user.name}!", colour = embed_color, description=f"Prefix for {ctx.guild}: **{bot_prefix}**\nIf a command is not working, or something goes wrong?\nUse the this command `{bot_prefix}ctdev [question/feedback]`!\n**Don't include the example brackets when using the commands!**⠀\n⠀")
        embed.set_thumbnail(url = bot.user.avatar_url)
        embed.add_field(name="Core Commands", value=f"{bot_prefix}h or {bot_prefix}help \n{bot_prefix}invite \n{bot_prefix}ls or {bot_prefix}listservers \n{bot_prefix}si or {bot_prefix}serverinfo \n{bot_prefix}about \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value=f"To get help and commands per PM \nTo get a PM with the Bot Invite \nTo get a list of server with {bot.user.name} \nTo see server information \nTo see information about {bot.user.name} \n", inline=True)
        embed.add_field(name="Kawaii Commands", value=f"{bot_prefix}hug [@mention]⠀\n{bot_prefix}poke [@mention]⠀\n{bot_prefix}wave [@mention]⠀\n{bot_prefix}hide [@mention]⠀\n{bot_prefix}blush⠀\n{bot_prefix}shine⠀\n{bot_prefix}happy \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value=f"To hug {bot.user.name} or someone else! \nTo poke {bot.user.name} or someone else! \nTo wave at {bot.user.name} or someone else! \nTo hide for {bot.user.name} or someone else! \nTo express that you're blushing! \nTo express you're shining! \nTo express you're happy! \n", inline=True)
        embed.add_field(name="Fun Commands", value=f"{bot_prefix}8ball [question]⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value="Ask all you want, to the holy 8Ball!\n", inline=True)
        embed.add_field(name="Voice Commands", value=f"{bot_prefix}connect⠀\n{bot_prefix}disconnect \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value=f"Connect {bot.user.name} [voice-channel]\nDisconnect {bot.user.name} [voice-channel]\n", inline=True)
        embed.add_field(name="Administrator Commands", value=f"{bot_prefix}sr [@mention] [rolename]\n{bot_prefix}rr [@mention] [rolename] \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", inline=True)
        embed.add_field(name="⠀", value="Give/set a role to someone!\nRemove a role from someone!\n", inline=True)
        await ctx.author.send(embed = embed),

        embed = discord.Embed(description = "**"+ctx.author.name +" a personal message with all my commands is on the way!** :heart:", color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @bot.command(pass_context = True, no_pm = True, aliases = ['p'])
    async def prefix(ctx):

        embed = discord.Embed(description = "**"+ ctx.author.name +f"** the prefix to use **{bot.user.name}** is: `{bot_prefix}`", color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

#################################################
############## Contact Dev Command ##############
#################################################

    @bot.command(pass_context = True)
    async def ctdev(ctx, *, pmessage : str = None):
        invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
        dev = bot.get_user(bot_owner)

        if pmessage == None:
            embed = discord.Embed(description = "**"+ ctx.author.name +"** my developers need to know something right? Type a feedback!", color = embed_color_error)
            await ctx.send(embed = embed)
            await ctx.message.delete()
        else:
#            msg = "User: {}\nServer: {}\nFeedBack: {}\nServer Invite: {}".format(ctx.author, ctx.guild, pmessage, invite.url)
            embed = discord.Embed(title = "Invite to {} discord server!".format(ctx.guild), colour = embed_color, url = "{}".format(invite.url), description = "**Feedback:** {}".format(pmessage))
            embed.set_thumbnail(url = "{}".format(ctx.author.avatar_url))
            embed.set_author(name = "{} sent:".format(ctx.author), icon_url = "{}".format(ctx.author.avatar_url))
            await dev.send(embed = embed)
#            await dev.send(msg)
            embed = discord.Embed(description = "I have PMed **{}#{}** with your feedback! Thank you for your help!".format(dev.name, dev.discriminator), color = embed_color_succes)
            await ctx.send(embed = embed)
            await ctx.message.delete()
#            return await ctx.send(ctx.author.mention + " I have PMed my creator your feedback! Thank you for the help!")
            

#################################################

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot_token)