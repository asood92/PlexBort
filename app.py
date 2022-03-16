import discord
import os

client = discord.Client()

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

client.run(os.getenv('TOKEN'))
