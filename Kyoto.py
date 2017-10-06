import discord
import asyncio
import random
import json
from discord.ext.commands import Bot
from discord.ext import commands


Client = discord.Client()
#Server = discord.Server(discord.Server.id)
bot_prefix= "-"
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")


@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("Prefix: {}".format(bot_prefix))
    print("ID: {}".format(client.user.id))
#    await client.change_presence(game=discord.Game(name='type -help for help.'))

#info command (-info)
#@client.command(pass_context = True)
#async def info(ctx):
#    await client.say("")

#########################################
############# Core Commands #############
#########################################

#help command (-help)
@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title="Command List for Kyoto!", colour=discord.Colour(0xcd4bb6), description="By default all commands have the ``-`` prefix. \nIf your server admin changed the prefix, then stick to that prefix!\n**Don't include the example brackets when using the commands!**⠀\n⠀")
    embed.add_field(name="Core Commands", value="`-help`⠀`-invite`⠀`-ls` or `-listservers`⠀`-si` or `-serverinfo`\n", inline=False)
    embed.add_field(name="Kawaii Commands", value="`-hug [@mention]`⠀`-poke [@mention]`⠀`-wave [@mention]`⠀`-hide [@mention]`⠀\n`-blush`⠀`-shine`⠀`-happy`\n", inline=False)
    embed.add_field(name="Voice Commands", value="`-connect`⠀`-disconnect`\n", inline=False)
    embed.add_field(name="Administrator Commands", value="`-clear [amount]`⠀`-ban [@mention]`⠀`-getbans`⠀`-kick [@mention]`", inline=False)
    await client.send_message(ctx.message.author, embed = embed),

    embed = discord.Embed(description = "**"+ctx.message.author.mention +" a personal message with all my commands is on the way!** :heart:", color = 13454262)
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#invite command (-invite)
@client.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(title = "**Invite Kyoto to your server!**", description = "You want to invite **Kyoto** to your server?\nThen you can use this link to invite him!\n\n[Click here to invite **Kyoto**](https://discordapp.com/oauth2/authorize?client_id=365240645419270145&scope=bot&permissions=527952983)", color = 13454262)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/365240645419270145/3f6527890a2b55b1eb864dd0113e0589.png")
    await client.send_message(ctx.message.author, embed = embed)

    embed = discord.Embed(description = "**"+ctx.message.author.mention +" a personal message with the bot invite is on the way!** :heart:", color = 13454262)
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#listservers command (-listservers)
@client.command(pass_context = True, aliases=['ls'])
async def listservers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 13454262)
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#server command (-server)
@client.command(pass_context = True, aliases=['si'])
async def serverinfo(ctx):
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

    await client.say(embed = embed)
    await client.delete_message(ctx.message)

##########################################
############# Voice Commands #############
##########################################

#connect command (-connect)
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
 
#disconnect command (-disconnect)
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()


#@client.command(pass_context = True)
#async def invite(ctx):
#    x = await client.invites_from(ctx.message.server)
#    x = ["<" + y.url + ">" for y in x]
#    print(x)
#    embed = discord.Embed(title = "Invite Links", description = x, color = 13454262)
#    return await client.say(embed = embed)
 
##########################################
############# Admin Commands #############
##########################################

@client.command(pass_context=True)
async def game(ctx, *, game=None):
        """Sets bot's playing status

        Leaving this empty will clear it."""

        server = ctx.message.server

        current_status = server.me.status if server is not None else None

        if ctx.message.author.id == "139191103625625600":
            await client.change_presence(game=discord.Game(name=game),status=current_status)
            
        else:
            await bot.change_presence(game=None, status=current_status)
        await client.say("Done.")

#getbans command (-getbans)
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 13454262)
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#clear command (-clear [amount])
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    
    embed = discord.Embed(title = "Messages Deleted", description = number, color = 13454262)
    return client.say(embed = embed)

#ban command (-ban)
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")


    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 13454262)
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#kick command (-kick)
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 13454262)
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

######################################
############ Fun Commands ############
######################################

@client.command(pass_context = True, aliases=['8ball'])
async def eightball(ctx):
    result = ["Neko", "Loli", "Kitsune"]
    choice = random.choice(result)
    await client.say(choice)

#########################################
############ Kawaii Commands ############
#########################################


#hug command (-hug [@mention])
@client.command(pass_context = True)
async def hug(ctx, *, member : discord.Member = None):

    if not member:
        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** you got hugged by **<@!365240645419270145>**", color = 13454262)
        embed.set_image(url="https://media.tenor.com/images/08de7ad3dcac4e10d27b2c203841a99f/tenor.gif")
        await client.say(embed = embed)
        await client.delete_message(ctx.message)

    embed = discord.Embed(description = "**%s** you got hugged by **"%member.mention + ctx.message.author.mention +"**", color = 13454262)
    embed.set_image(url="http://i.imgur.com/cLHRyeB.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#poke command (-poke [@mention])
@client.command(pass_context = True)
async def poke(ctx, *, member : discord.Member = None):

    if not member:
        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** pokes **<@!365240645419270145>**", color = 13454262)
        embed.set_image(url="https://i.imgur.com/kXBD83W.gif")
        await client.say(embed = embed)
        await client.delete_message(ctx.message)

    embed = discord.Embed(description = "**%s** you got poked by **"%member.mention + ctx.message.author.mention +"**", color = 13454262)
    embed.set_image(url="https://i.imgur.com/kXBD83W.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)
  
#wave command (-wave [@mention])
@client.command(pass_context = True)
async def wave(ctx, *, member : discord.Member = None):

    if not member:
        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** waves to **<@!365240645419270145>**", color = 13454262)
        embed.set_image(url="https://i.imgur.com/w5kTICt.gif")
        await client.say(embed = embed)
        await client.delete_message(ctx.message)

    embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** waves at you **%s**"%member.mention, color = 13454262)
    embed.set_image(url="https://i.imgur.com/w5kTICt.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#hide command (-hide [@mention])
@client.command(pass_context = True)
async def hide(ctx, *, member : discord.Member = None):

    if not member:
        embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** hides for **<@!365240645419270145>**", color = 13454262)
        embed.set_image(url="https://i.imgur.com/BZQwbid.gif")
        await client.say(embed = embed)
        await client.delete_message(ctx.message)

    embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** hides for **%s**"%member.mention, color = 13454262)
    embed.set_image(url="https://i.imgur.com/BZQwbid.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#blush command (-blush)
@client.command(pass_context = True)
async def blush(ctx):

    embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** blushes", color = 13454262)
    embed.set_image(url="https://i.imgur.com/DGhgJ1R.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#shine command (-shine)
@client.command(pass_context = True)
async def shine(ctx):

    embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** shines", color = 13454262)
    embed.set_image(url="https://i.imgur.com/VUuoZfa.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

#happy command (-happy)
@client.command(pass_context = True)
async def happy(ctx):

    embed = discord.Embed(description = "**"+ ctx.message.author.mention +"** is super happy!", color = 13454262)
    embed.set_image(url="https://i.imgur.com/4xSrwsj.gif")
    await client.say(embed = embed)
    await client.delete_message(ctx.message)

client.run("MzY1MjQwNjQ1NDE5MjcwMTQ1.DLbgxg.1YZ1I8mqliOBd8ESKh_0iBiU_cc")
