#this make bot work yes
from http.client import responses

import discord
import random
import os
import asyncio
from discord import app_commands
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('kill it!')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.streaming, name="banshee up", url='https://www.twitch.tv/champii'))
    try:
        synced_commands = await bot.tree.sync()
        print(f"synced {len(synced_commands)} commands.")
    except Exception as e:
        print('error w syncing app commands :( ', e)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(token)

#Token :D
with open("token.txt") as file:
    token = file.read()

asyncio.run(main())
