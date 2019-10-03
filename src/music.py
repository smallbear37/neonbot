import discord
import asyncio
import youtube_dl
import re

# TODO: Put content in the class
client = discord.Client()
que = {}
playerlist = {}
playlist = list() # Playlist

def queue(id): # The queue for play the music
	if que[id] != []:
		player = que[id].pop(0)
		playerlist[id] = player
		del playlist[0]
		player.start()

# FIXME: Undefined variable 'client'
@client.event
async def on_message(message):

	if message.author == client.user: # Ignore bot's say
		return

	if message.content.startswith("%aplay" % prefix): # Add bot to voice channel
		msg = message.content.split(" ")
		try:
			url = msg[1]
			# TODO: rewrite
			url1 = re.match('(https?://)?(www\.)?((youtube\.(com))/watch\?v=([-\w]+)|youtu\.be/([-\w]+))', url) # Check url
			if url1 == None:
				await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: url을 제대로 입력해주세요.",colour = 0x2EFEF7))
				return
		except IndexError:
			await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: url을 입력해주세요.",colour = 0x2EFEF7))
			return

		channel = message.author.voice.voice_channel 
		server = message.server
		voice_client = message.channel.voice_client_in(server)

		if client.is_voice_connected(server) and not playerlist[server.id].is_playing(): # If bot in the voice channel, but not playing music
			await message.channel.send(message.channel, embed=discord.Embed(title=":white_check_mark: 음악을 재생하지 않아 음성채널에서 나갑니다.",colour = 0x2EFEF7))
			await voice_client.disconnect()
		elif client.is_voice_connected(server) and playerlist[server.id].is_playing(): # When bot in the voice channel, playing music
			player = await voice_client.create_ytdl_player(url,after=lambda:queue(server.id),before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
			if server.id in que: # When a queue has a value
				que[server.id].append(player)
			else: # When a queue hasn't a value
				que[server.id] = [player]
			await message.channel.send(message.channel, embed=discord.Embed(title=":white_check_mark: 추가 완료!",colour = 0x2EFEF7))
			playlist.append(player.title) # Add title to playlist
			return

		try:
			voice_client = await client.join_voice_channel(channel)
		except discord.errors.InvalidArgument: # If user doesn't join in voice channel
			await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: 음성채널에 접속하고 사용해주세요.",colour = 0x2EFEF7))
			return

		try:
			player = await voice_client.create_ytdl_player(url,after=lambda:queue(server.id),before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
			playerlist[server.id] = player
			playlist.append(player.title)
		except youtube_dl.utils.DownloadError: # If user doesn't insert feasible link
			await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: 존재하지 않는 경로입니다.",colour = 0x2EFEF7))
			await voice_client.disconnect()
			return
		player.start()

	if message.content == "%aquit" % prefix: # 	Exit bots from voice channels
		server = message.server
		voice_client = client.voice_client_in(server)

		if voice_client == None: # When the bot is not connected to the voice channel
			await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: 봇이 음성채널에 없어요.",colour = 0x2EFEF7))
			return
		
		await message.channel.send(message.channel, embed=discord.Embed(title=":mute: 채널에서 나갑니다.",colour = 0x2EFEF7)) # When the bot is connected to the voice channel
		await voice_client.disconnect()

	if message.content == "%askip" % prefix: # Music skip
		id = message.server.id
		if not playerlist[id].is_playing(): # When no music is playing
			await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: 스킵할 음악이 없어요.",colour = 0x2EFEF7))
			return
		await message.channel.send(message.channel, embed=discord.Embed(title=":mute: 스킵했어요.",colour = 0x2EFEF7))
		playerlist[id].stop()
	
	if message.content == "%anp" % prefix: # Check the playlist

		if playlist == []:
			await message.channel.send(message.channel, embed=discord.Embed(title=":no_entry_sign: 재생목록이 없습니다.",colour = 0x2EFEF7))
			return

		playstr = "```css\n[재생목록]\n\n"
		for i in range(0, len(playlist)):
			playstr += str(i+1)+" : "+playlist[i]+"\n"
		await client.send_message(message.channel, playstr+"```")