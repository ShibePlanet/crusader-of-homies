import discord
from discord.ext import commands


class Admin(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # Status commands.
    @commands.command()
    async def playing(self, ctx, *, status = 'a game.'):
        if ctx.message.author.id == 466303359343656973:
            await self.client.change_presence(activity = discord.Game(name = status))
            await ctx.send(f'Status changed to: `Playing {status}`')
        else:
            await ctx.send('Sorry, you\'re not a bot admin!')

    @commands.command()
    async def listening(self, ctx, *, status = 'a song.'):
        if ctx.message.author.id == 466303359343656973:
            await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = status))
            await ctx.send(f'Status changed to: `Listening to {status}`')
        else:
            await ctx.send('Sorry, you\'re not a bot admin!')

    @commands.command()
    async def watching(self, ctx, *, status = 'you.'):
        if ctx.message.author.id == 466303359343656973:
            await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = status))
            await ctx.send(f'Status changed to: `Watching {status}`')
        else:
            await ctx.send('Sorry, you\'re not a bot admin!')


# Setup
def setup(client):
    client.add_cog(Admin(client))
