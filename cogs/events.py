import discord
from discord import client 
from discord.ext import commands
from cogs.background_tasks import BackgroundTasks
import emoji

dlient = discord.Client


class Events(commands.Cog):
    # Initializes class by creating client variable
    def __init__(self, client):
        self.client = client

    # All events triggered when certain action occurs

    # Called when bot connects to discord server, prints in terminal to let developer it's online
    @commands.Cog.listener()
    async def on_ready(self):
        print("Connected to server")

    # Triggered when member joins a server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the sever') 
        await member.create_dm() # Creates DM channel with member
        await member.dm_channel.send(
            f'Hi {member.name} thanks for joining the test server to aid development'
    ) # Prints changeable message, uses member's name

    @commands.Cog.listener()
    # Triggered when member leaves server
    async def on_member_remove(self, member):
        print(f'{member} has left the server') # Just lets developer know in terminal

    @commands.Cog.listener('on_message')
    # Called whenever a message is sent
    async def on_message(self, message):
        bruh_count = 0
        message_words = message.content.split(' ') # Creates a list of the words in a message sent
        for word in message_words:
            if 'BRUH' == word.upper():
                await message.channel.send(emoji.emojize(":b:ruh Moment")) # Send "bruh moment" every single time someone sends a message with bruh in it
                if 'F' == word.upper() or 'Fs' == word.upper():
                    await message.channel.send(emoji.emojize(":regional_indicator_f:")) # Send "F" if anyone puts Fs in chat bois
                break
            if 'F' == word.upper() or 'FS' == word.upper() or 'FF' == word.upper():
                await message.channel.send(emoji.emojize(":regional_indicator_f:")) # Send "F" if anyone puts Fs in chat bois
                break


# Adds cog to bot.py
def setup(client):
    client.add_cog(Events(client))