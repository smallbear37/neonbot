import discord
import asyncio
import youtube_dl
import re

class normal:
    def normal():
        @client.event
        async def on_message(message):
	        if message.author == client.user: # Ignore bot's say
		        return
	        if message.content == "%ahi" % prefix:
	        if message.content == "%aping" % prefix:
		        await message.channel.send(message.channel, 'pong!')
            if message.content == "%aeasteregg" % prefix:
				await message.channel.send(message.channel, '이이잉 앗살라말라이쿰~')