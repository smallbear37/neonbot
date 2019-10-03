import discord
import asyncio
import youtube_dl
import re

class normal:
    def manage():
        @client.event
        async def on_message(message):

	        if message.author == client.user: #봇이 채팅을 쳤을 때 명령어로 인식되지 않음
		        return

	        if message.content == "!n.hi":
				await message.channel.send(message.channel, '안녕하세요! :)')
	        if message.content.startswith('!n.ping'):
		        await message.channel.send(message.channel, 'pong!')