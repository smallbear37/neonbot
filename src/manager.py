import discord
import asyncio
import youtube_dl
import re

def manager():
    @client.event
    async def on_message(message):

	    if message.author == client.user: # Ignore bot's say
		    return