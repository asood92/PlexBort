import os
import discord
import requests
import xml.etree.ElementTree as ET

client = discord.Client();

BASE_URL = os.getenv('BASE_URL')
PLEX_API_TOKEN = os.getenv('PLEX_API_TOKEN')
SONARR_API_TOKEN = os.getenv('SONARR_API_TOKEN')
DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')
QUERY_PATH = "/library/recentlyAdded"

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
        res = get_recently_added()
        print("got response \n")
        await message.channel.send(res)

def get_recently_added():
    response = requests.get(f"{BASE_URL}{QUERY_PATH}", headers={'X-Plex-Token': PLEX_API_TOKEN})
    parsed = ET.fromstring(response)
    print(parsed)
    return parsed

client.run(os.getenv('TOKEN'))
