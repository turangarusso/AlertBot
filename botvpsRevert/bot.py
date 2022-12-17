import asyncio

import discord

from discord.ext import commands
from discord import client, Client
from discord.ext.commands import Bot

print("avvio")
client = commands.Bot(command_prefix=("t!"))
token = "your Discord Developer Token"


@client.event
async def on_ready():
    print(client.user, client.user.id)
    channel = client.get_channel(968628680559575043)
    await channel.send('vps libera')
    #await client.close()


client.run(token)
