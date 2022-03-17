import os
from re import M
import discord
import requests
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
BASE_URL = os.getenv('BASE_URL')
PLEX_API_TOKEN = os.getenv('PLEX_API_TOKEN')
SONARR_API_TOKEN = os.getenv('SONARR_API_TOKEN')
DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')
QUERY_RECENTS = "/library/recentlyAdded"

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
        await message.channel.send("Hi, I'm PlexBot! \n\
            I'm a statistics bot, and I can do a few things! Commands are: \n \
                !ping - to get my status \n \
                !help - to get this message \n \
                !recentlyadded - to get the latest additions to Plex \n \
            ")
    if message.content.startswith('!recentlyadded'):
        res = get_recently_added()
        print("got response \n")
        # pretty_output = ""
        output = discord.Embed(title="Recently Added")
        # for i in range(len(res)):
        #     for key, value in res[i].items():
        #         # await message.channel.send(f"{key}: **{value}")
        #         pretty_output += str(key) + ": **" + str(value) + "\n"
        #         # if len(pretty_output) > 1800:
        #         # pretty_output = ""

        print(res, type(res))
        for i in range(len(res)):
            for k, v in res[i].items():
                print(k, v)
                if k == "Poster" or k == "Thumb":
                    output.set_image(url=v)
                else:
                    output.add_field(name=k, value=v, inline=False)
            await message.channel.send(embed=output)
            output = discord.Embed(title="Recently Added")
        # message_fields = discord.Embed.from_dict(res)
        # print(message_fields)
        # for item in res.keys():
        #     output.add_field(name=item, value=item.value, inline=False)
        # print(output)
        # newMessage = discord.Embed(title="Recently Added", fields=output)

        # if len(pretty_output) > 2000:
        #     await message.channel.send(f"{pretty_output[:2000]}
        # else:
        #     await message.channel.send(f"{pretty_output}")
        # await message.channel.send(embed=output)

            # pretty_output = ""
            # pretty_output += "\n"
        # for item in res:
        #     for k,v in item.items():
        #         pretty_output += f"{k}: {v}\n"

def get_recently_added():
    response = requests.get(f"{BASE_URL}{QUERY_RECENTS}", headers={'Accept': 'application/json', 'X-Plex-Token': PLEX_API_TOKEN})
    json_data = response.json()
    # print(json_data)

    results = []
    desired_number_results = 3
    uniques = list()

    while len(results) < desired_number_results:
        for item in json_data['MediaContainer']['Metadata']:
            if len(results) >= desired_number_results:
                break
            # if item['type'] != "movie":
                # if item['parentTitle'] in uniques:
                #     continue
                # else:
                #     print("going into weird loop")
            else:
                if 'parentTitle' in item.keys():
                    if item['parentTitle'] in uniques:
                        continue
                    uniques.append(item['parentTitle'])
                    print(f"added {item['parentTitle']} to uniques")
                    results += [{
                        'Poster': BASE_URL+item['parentThumb']+'?X-Plex-Token='+PLEX_API_TOKEN,
                        'Title': item['parentTitle'] + " - " + str(item['parentYear']),
                        'Summary': item['parentSummary'] + "\n",
                    }]
                    print(f"added {item['parentTitle']} to results from tv")

                else:
                    results += [{
                        'Thumb': BASE_URL+item['thumb']+'?X-Plex-Token='+PLEX_API_TOKEN,
                        'Title': item['title'] + " - " + str(item['year']),
                        'Summary': item['summary'] + "\n",

                    }]
                    print(f"added {item['title']} to results from movies")

                # uniques.append([item['parentTitle']])
                    # results.append({k: v for k, v in item.items() if k in desired_fields or k == 'parentTitle'} or k == 'parentSummary')
                    # uniques.append(item['parentTitle'])

                    #     results.append(f"{json_data['MediaContainer']['Metadata'][i]['parentTitle']} - {json_data['MediaContainer']['Metadata'][i]['title']}")

            # results.append({k: v for k, v in item.items() if k in desired_fields})

    # single_item = json_data['MediaContainer']['Metadata'][0]
    # for child in parsed.iter('*'):
    #     print(child.tag, child.attrib)

    # print(results[0])
    # print(type(results))
    # print(results)
    return results


client.run(DISCORD_API_TOKEN)
