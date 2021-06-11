import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands.errors import MissingPermissions


class Mod(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # GBJ
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def gbj(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send('Please add a member. For more help, use `c!help`.')
            return 
        
        role = discord.utils.get(user.guild.roles, name='gay baby jail')
        channel = discord.utils.get(user.guild.channels, name = 'gay-baby-jail')

        if role in user.roles:
            await ctx.send('That person already has that role. Do you mean `c!ungbj (member)`?')
            return 
        else: 
            await user.add_roles(role)

            await ctx.send(f'{user.mention} was sent to gbj.')
            await channel.send(f'{user.mention}, you have been sent to Gay Baby Jail. Please use this format to return to society:\n`I am sorry for (reason).`')
    @gbj.error
    async def gbj_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('Sorry, you don\'t have the permissions to do that.')


    # UNGBJ
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def ungbj(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send('Please add a member. For more help, use `c!help`.')
            return 
        
        role = discord.utils.get(user.guild.roles, name='gay baby jail')
        channel = discord.utils.get(user.guild.channels, name = 'gay-baby-jail')

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f'{user.mention} was removed from gbj.')
        else: 
            await ctx.send('That person doesn\'t have that role. Do you mean `c!gbj (member)`?')
            return 
    @ungbj.error
    async def gbj_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('Sorry, you don\'t have the permissions to do that.')


    # FG
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def fg(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send('Please add a member. For more help, use `c!help`.')
            return 
        
        role = discord.utils.get(user.guild.roles, name='furry gulag')
        channel = discord.utils.get(user.guild.channels, name = 'furry-gulag')

        if role in user.roles:
            await ctx.send('That person already has that role. Do you mean `c!unfg (member)`?')
            return 
        else: 
            await user.add_roles(role)

            await ctx.send(f'{user.mention} was sent to the furry gulag.')
            await channel.send(f'{user.mention}, you\'re a furry. How does it feel? DM staff if you have an issue.')
    @fg.error
    async def gbj_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('Sorry, you don\'t have the permissions to do that.')


    # UNFG
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def unfg(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send('Please add a member. For more help, use `c!help`.')
            return 
        
        role = discord.utils.get(user.guild.roles, name='furry gulag')
        channel = discord.utils.get(user.guild.channels, name = 'furry-gulag')

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f'{user.mention} was removed from the furry gulag.')
        else: 
            await ctx.send('That person doesn\'t have that role. Do you mean `c!fg (member)`?')
            return 
    @unfg.error
    async def gbj_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('Sorry, you don\'t have the permissions to do that.')


# Setup
def setup(client):
    client.add_cog(Mod(client))