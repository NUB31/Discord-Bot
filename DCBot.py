import discord
from discord.state import ConnectionState
import requests
import json

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        messageContent = message.content
        messageContentLower = messageContent.lower()
        if("vanylven" in messageContentLower and self.user != message.author or "fiskå" in messageContentLower and self.user != message.author):
            response = requests.get('https://api.giphy.com/v1/gifs/random?api_key=mz2Z5lXfYQZr7x5Hk8OCKKUyNyCctiBq&rating=unrated&tag=laugh')
            response = response.json()
            # print(response["data"])
            embed = discord.Embed(title="vanylven shit lol")
            embed.set_image(url=str(response["data"]['images']['downsized_large']["url"]))
            await message.channel.send(embed=embed)
        if message.content.startswith("!uwu "):
            print(message.content)
            word = []
            for i in range(len(message.content)):
                if (i > 4):
                    word.append(message.content[i])
            x = "".join(word)
            response = requests.get('http://localhost:3000/uwu?text=' + x)
            response = response.json()
            await message.channel.send(response["Text"])


client = MyClient()
client.run('')
