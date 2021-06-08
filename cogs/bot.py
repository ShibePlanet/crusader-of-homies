import discord
from discord.ext import commands


class Bot(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # Ping
    @commands.command()
    async def ping(self, ctx):
        ping = round(self.client.latency * 1000)

        if ping < 100:
            embed = discord.Embed(title = 'Pong!', color = discord.Color.green(), description = f'Client latency: {ping}ms')
        elif ping > 100 and ping < 300:
            embed = discord.Embed(title = 'Pong!', color = discord.Color.gold(), description = f'Client latency: {ping}ms')
        else:
            embed = discord.Embed(title = 'Pong!', color = discord.Color.red(), description = f'Client latency: {ping}ms')

        await ctx.send(embed=embed)
    

    # Info
    @commands.command()
    async def info(aelf, ctx):
        embed = discord.Embed(title = 'Info!', color = discord.Color.green())
        
        embed.add_field(name = 'Created on', value = 'June 6th, 2021', inline = False)
        embed.add_field(name = 'Created by', value = '<@466303359343656973>', inline = False)
        embed.add_field(name = 'Want your own bot?', value = 'DM me and we can talk!', inline = False)

        await ctx.send(embed=embed)



# Setup
def setup(client):
    client.add_cog(Bot(client))