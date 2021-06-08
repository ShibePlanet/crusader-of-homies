import discord
from discord.ext import commands
from discord.ext import has_permissions


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
            await user.remove_roles(role)
            await ctx.send(f'{user.mention} was removed from gbj.')
        else: 
            await ctx.send('That person doesn\'t have that role. Do you mean `c!gbj (member)`?')
            return 


# Setup
def setup(client):
    client.add_cog(Mod(client))