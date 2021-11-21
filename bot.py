# bot.py
import os
import random
import time

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


gifs = {
    "!ussr": "https://tenor.com/bf7w3.gif",
    "!haha": "https://tenor.com/vzXt.gif",
    "!bro": "https://tenor.com/PJlo.gif",
    "!noted": "https://tenor.com/ugjg.gif",

    # nsfw
    "!mshia": "https://i.imgur.com/TOcr2B7.gif",
    "!saxe": "https://i.imgur.com/ZkPBnUk.gif",
    "!pirshi": "https://i.imgur.com/ScXP4Pw.mp4",
    "!dzmasvetitave": "https://imgur.com/gallery/XPLPf4A",
    "!lesboseli": "https://i.imgur.com/ZTMKi2c.gif"
}


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
                
    async def on_member_join(self, member):
        print('hiiii: '+member)

    async def on_ready(self):
        print(f'{client.user.name} has connected to Discord!')



if __name__ == "__main__":
    client = Bototo()
    client.run(TOKEN)
