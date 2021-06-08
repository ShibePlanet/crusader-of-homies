### Crusader of Homies ###
###     06/06/2021     ###

# Imports
import os
from discord.ext import commands


# Client setup + prefixes
client = commands.Bot(command_prefix=commands.when_mentioned_or('c! ', 'c!'))
client.remove_command('help')


# Load cog file
@client.command()
async def load(ctx, extension):
    ctx.load_extension(f'cogs.{extension}')


# Unload cog file
@client.command()
async def unload(ctx, extension):
    ctx.unload_extension(f'cogs.{extension}')


# Load cogs 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# Runs bot
client.run(os.getenv('TOKEN'))