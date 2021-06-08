import discord
from discord.ext import commands


class Misc(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # Vent
    @commands.command()
    @commands.cooldown(5, 3, commands.BucketType.user)
    async def vent(self, ctx, *, message = None):
        channel = self.client.get_channel(851320205829603329)

        if ctx.guild:
            await ctx.message.delete()
            await ctx.message.author.send(f'**CAREFUL {ctx.message.author.mention}!** You just sent that in the server! I have deleted your message and forwarded it to you, but next time PLEASE DM me instead!')
            await ctx.message.author.send(message)
            return

        if message == None:
            await ctx.send('No message to send.')
            return

        
        await channel.send(message)
        await ctx.send('Your message has been sent.')


    # Avatar
    @commands.command()
    async def avatar(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.message.author

        embed = discord.Embed(title = f'{user.display_name}\'s avatar', color = user.color)
        embed.set_image(url = user.avatar_url)

        await ctx.send(embed=embed)


# Setup
def setup(client):
    client.add_cog(Misc(client))