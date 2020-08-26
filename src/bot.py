import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

GUIDO_MOTTO = "I sit and I shit."


@client.event
async def on_ready():
    print(f'{client.user} has joined the Hive...')


@client.event
async def on_message(message):
    if 'guido' in message.content.lower():
        await message.channel.send(GUIDO_MOTTO)

client.run(TOKEN)

