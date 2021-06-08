import discord
from discord.ext import commands


class Help(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # Help
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = 'Help has arrived!', color = discord.Color.green())

        embed.add_field(name = 'Bot commands', value = '`c!help` - displays this page. \n`c!info` - display some info. \n`c!ping` - displays the client latency.', inline = False)
        embed.add_field(name = 'Fun commands', value = '`c!dice` - roll a six-sided die. \n`c!coinflip` - flip a coin. \n`c!choose [fields]` - choose from a few inputs.', inline = False)
        embed.add_field(name = 'Miscellaneous commands', value = '`c!avatar <@user>` - get someone\'s avatar', inline = False)
        embed.set_footer(text = '(one) [one or more] {two or more} <optional>')

        await ctx.send(embed = embed)


# Setup
def setup(client):
    client.add_cog(Help(client))