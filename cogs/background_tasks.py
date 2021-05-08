from cogs.commands import Commands
import discord
from discord.ext import tasks, commands
import random

class BackgroundTasks(commands.Cog):
    # Initializes class by creating client variable
    def __init__(self, client):
        self.client = client

    
def setup(client): # Adds cog to bot.py
    client.add_cog(BackgroundTasks(client))
