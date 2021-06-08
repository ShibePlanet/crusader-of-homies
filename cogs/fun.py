import asyncio
import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # Dice
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per = commands.BucketType.channel, wait = False)
    async def dice(self, ctx):
        embed = discord.Embed(description = f'Rolling... :game_die:', color = discord.Color.green())
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)

        embed = discord.Embed(description = f'I rolled {random.randint(1,6)}! :game_die:', color = discord.Color.green())
        await msg.edit(embed=embed)


    # List picker
    @commands.command()
    async def choose(self, ctx, *list):
        print(list)
        if list == ():
            embed = discord.Embed(description = f'Please enter some fields to choose from! :x:', color = discord.Color.red())
        else:
            embed = discord.Embed(description = f'I chose `{random.choice(list)}`! :books:', color = discord.Color.green())

        await ctx.send(embed = embed)


    # Coin flip
    @commands.command(aliases=['flipcoin', 'flip', 'coin'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per = commands.BucketType.channel, wait = False)
    async def coinflip(self, ctx):
        coins = ['heads', 'tails']

        embed = discord.Embed(description = f'Flipping... :coin:', color = discord.Color.green())
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)

        embed = discord.Embed(description = f'I flipped {random.choice(coins)}! :coin:', color = discord.Color.green())
        await msg.edit(embed=embed)


# Setup
def setup(client):
    client.add_cog(Fun(client))