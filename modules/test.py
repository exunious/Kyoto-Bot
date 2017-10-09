    @checks.mod_or_permissions(administrator = True)
    @commands.command(name = "smute", no_pm = True)
    async def server_mute(self, ctx, user : discord.Member, *, reason: str = None):
        """Mutes user in the server"""
        author = ctx.message.author
        server = ctx.message.server

        if not self.is_allowed_by_hierarchy(server, author, user):
            await self.bot.say("I cannot let you do that. You are "
                               "not higher than the user in the role "
                               "hierarchy.")
            return

        register = {}
        for channel in server.channels:
            if channel.type != discord.ChannelType.text:
                continue
            overwrites = channel.overwrites_for(user)
            if overwrites.send_messages is False:
                continue
            register[channel.id] = overwrites.send_messages
            overwrites.send_messages = False
            try:
                await self.bot.edit_channel_permissions(channel, user,
                                                        overwrites)
            except discord.Forbidden:
                await self.bot.say("Failed to mute user. I need the manage roles "
                                   "permission and the user I'm muting must be "
                                   "lower than myself in the role hierarchy.")
                return
            else:
                await asyncio.sleep(0.1)
        if not register:
            await self.bot.say("That user is already muted in all channels.")
            return
        self._perms_cache[user.id] = register
        dataIO.save_json("data/mod/perms_cache.json", self._perms_cache)
        await self.new_case(server,
                            action="SMUTE",
                            mod=author,
                            user=user,
                            reason=reason)
        await self.bot.say("User has been muted in this server.")