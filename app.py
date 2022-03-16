import os
import discord

client = discord.Client()

BASE_URL = os.getenv('BASE_URL')
QUERY_PATH = "/library/recentlyAdded"
PLEX_API_TOKEN = os.getenv('PLEX_API_TOKEN')
SONARR_API_TOKEN = os.getenv('SONARR_API_TOKEN')

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send("Pong!")

    if message.content.startswith('!help'):
        await message.channel.send("Hi, I'm PlexBort! \n\
            I'm a statistics bot, and I can do a few things! Commands are: \n \
                !ping - to get my status \n \
                !help - to get this message \n \
                !recentlyadded - to get the latest additions to Plex \n \
            ")
    if message.content.startswith('!recentlyadded'):
        await message.channel.send("{BASE_URL}{QUERY_PATH}")

client.run(os.getenv('TOKEN'))
