import discord
import asyncio
import youtube_dl
import re
import json
from discord.ext import commands
from manager import *
from music import *
from normal import *

#Json part
with open('config/main.json') as json_file:
    json_data = json.load(json_file)

token = json_data["bot_token"]
prefix = json_data["prefix"]

bot = commands.Bot(command_prefix='%a' % prefix)
ver = "1.0.0-alpha" # Ver

songs = asyncio.Queue()
play_next_song = asyncio.Event()

client = discord.Client()

# FIXME: invalid syntax (<unknown>, line 26)
manage = new manager()
manage.manager()

# Run
@client.event 
async def on_ready():
	print("Thanks for run this program. The version of this program is %s." % ver)
	print(client.user.name)
	print(client.user.id)



client.run(token)