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


        guild = gifs[str(message.guild.id)]
        
        if message.content == "!gifs":
            commands = ""
            for command in guild.keys():
                commands += command + '\n'
            await message.channel.send(commands)
        else:
            if message.content in list(guild.keys()) and message.channel.is_nsfw():
                response = guild[message.content]
                
                if(len(response) == 2):
                    await message.channel.send(file = discord.File(fp = response[1], filename = response[0]))
                else:
                    await message.channel.send(content = response)

    async def on_ready(self):
        print(f'{client.user.name} has connected to Discord!')


if __name__ == "__main__":
    client = Bototo()
    client.run(TOKEN)
