import discord
import random
from discord.ext import commands
from discord.ext.commands.core import has_permissions

default_channel_id = ''

class Commands(commands.Cog):
     # Initializes class by creating client variable
    def __init__(self, client):
        self.client = client

    # Command prefix for all commands defined in bot.py under client variable

    # Returns latency of the bot (in milliseconds) in the same channel as the command was invoked
    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f'Latency is: {round(self.client.latency * 1000)}ms')

    # 50/50 chance of returning a positive or negative 
    @commands.command()
    async def capofax(self, ctx):
        responses = [
        "Cap", "Factual Information", "Fax", "Nossir", "Yessir", "Le Mao No", "yes", "Infactual Information", "Fattest Cap I've Ever Seen"
        ]
        await ctx.send(random.choice(responses)) # Sends in same channel as command invoked

    # Sets default channel for background tasks like sending random messages, variable stored in bot.py
    @commands.command()
    async def schedule(self, ctx, channel: discord.TextChannel, seconds):
        default_channel_id = channel.id # This takes the specified channel in the command and sets it to the default channel variable in bot.py

    # Used to clean up a discord channel, will delete messages
    @commands.command()
    @has_permissions(manage_messages=True) # Only works if the invoker has capabilities to manage messages 
    async def clear(self, ctx, amount=0): # Specification of the number of messages to be deleted
        amount+=1 # So it deletes the sent message as well
        await ctx.channel.purge(limit=amount)
 

def setup(client): # Adds cog to bot.py
    client.add_cog(Commands(client))