import discord
import asyncio
import youtube_dl
import re
import json
import manager
import music
import normal

with open('config/main.json') as json_file:
    json_data = json.load(json_file)

token = json_data["bot_token"]

client = discord.Client()
que = {}
playerlist = {}
playlist = list()

def queue(id):
	if que[id] != []:
		player = que[id].pop(0)
		playerlist[id] = player
		del playlist[0]
		player.start()

@client.event 
async def on_ready():
	print(client.user.name)
	print(client.user.id)

client.run(token)