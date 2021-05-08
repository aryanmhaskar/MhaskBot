import os
import random
import discord
import threading
from discord.ext import commands
import asyncio
from discord.ext.commands.core import has_permissions
from dotenv import load_dotenv

# Loads hidden environment variables from .env such as the token. 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initializes Discord client with specified intents
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
default_channel_id = '' # Used to store the channel in which the random messages should be sent

# Logs all python files in cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') # Splices last three characters to remove ".py" from filename

# Connects bot to Discord servers and bot becomes online
client.run(TOKEN)