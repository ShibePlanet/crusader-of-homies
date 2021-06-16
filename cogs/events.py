from discord.ext import commands


class Events(commands.Cog):

    # Init the client
    def __init__(self, client):
        self.client = client


    # On ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is online!')


    # Errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # Command not found
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found. Use `c!help` for a list of commands.')

        # Bot cooldown
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction('⌛')
        
        # Max concurrency
        elif isinstance(error, commands.MaxConcurrencyReached):
            await ctx.message.add_reaction('⏳')

        elif isinstance(error, commands.MissingPermissions):\
            await ctx.send('Sorry, you\'re missing the permissions to do that.')

        else:
            await ctx.send('An error occured with your command.')


# Setup
def setup(client):
    client.add_cog(Events(client))