import discord
import datetime
from discord.ext import commands
from config import *

# this specifies what extensions to load when the bot starts up
startup_extensions = ["extra.errorhandler", "owner", "admin", "core", "kawaii", "fun"]
bot_prefix = "-" #default prefix
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
        embed = discord.Embed(title="Command List for Kyoto!", colour = embed_color, description="By default all commands have the - prefix. \nIf your server admin changed the prefix, then stick to that prefix!\n**Don't include the example brackets when using the commands!**⠀\n⠀")
        embed.set_thumbnail(url = bot.user.avatar_url)
        embed.add_field(name="Core Commands", value="-h or -help \n-invite \n-ls or -listservers \n-si or -serverinfo \n-about \n", inline=True)
        embed.add_field(name="⠀", value="To get help and commands per PM \nTo get a PM with the Bot Invite \nTo get a list of server with Kyoto \nTo see server information \nTo see information about Kyoto \n", inline=True)
        embed.add_field(name="Kawaii Commands", value="-hug [@mention]⠀\n-poke [@mention]⠀\n-wave [@mention]⠀\n-hide [@mention]⠀\n-blush⠀\n-shine⠀\n-happy \n", inline=True)
        embed.add_field(name="⠀", value="To hug Kyoto or someone else! \nTo poke Kyoto or someone else! \nTo wave at Kyoto or someone else! \nTo hide for Kyoto or someone else! \nTo express that you're blushing! \nTo express you're shining! \nTo express you're happy! \n", inline=True)
        embed.add_field(name="Fun Commands", value="-8ball [question]⠀\n", inline=True)
        embed.add_field(name="⠀", value="Ask all you want, to the holy 8Ball!\n", inline=True)
        embed.add_field(name="Voice Commands", value="-connect⠀\n-disconnect\n", inline=True)
        embed.add_field(name="⠀", value="Connect Kyoto [voice-channel]\nDisconnect Kyoto [voice-channel]\n", inline=True)
        embed.add_field(name="Administrator Commands", value="-clear [amount]⠀-ban [@mention]⠀-getbans⠀-kick [@mention]", inline=False)
        await ctx.author.send(embed = embed),

        embed = discord.Embed(description = "**"+ctx.author.name +" a personal message with all my commands is on the way!** :heart:", color = embed_color)
        await ctx.send(embed = embed)
        await ctx.message.delete()

#    @bot.command(pass_context = True, no_pm = True, aliases = ['p'])
#    async def prefix(ctx):
#
#        embed = discord.Embed(description = "**"+ ctx.author.name +"** the prefix to use **Kyoto** is: `{}`".format(bot_prefix), color = embed_color)
#        await ctx.send(embed = embed)
#        await ctx.message.delete()

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
            embed = discord.Embed(title = "Invite to {} discord server!".format(ctx.guild), colour = embed_color, url = "{}".format(invite.url), description = "**Feedback:** {}".format(pmessage), timestamp = datetime.datetime.utcfromtimestamp(1507439238))
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