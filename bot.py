# bot.py

import os

# discord things
import discord
from dotenv import load_dotenv

# gifs library 
from library import load

load_dotenv()
gifs = load()
TOKEN = os.getenv('DISCORD_TOKEN')

class Bototo(discord.Client):

    async def on_message(self, message):
        # თუ ბოტის მიერ არის მესიჯი დააიგნორე
        if message.author == self.user:
            return

        if message.content == "!gifs":
            await message.channel.send(list(gifs.keys()))
        else:
            if message.content in list(gifs.keys()):
                response = gifs[message.content]
                await message.channel.send(response)

    async def on_ready(self):
        print(f'{client.user.name} has connected to Discord!')



if __name__ == "__main__":
    client = Bototo()
    client.run(TOKEN)
