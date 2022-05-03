import discord
from discord.ext.commands import Bot
import os
import re

movielist = []
premusers = ['239357844573388800']
tvlist = []

bot = Bot(command_prefix='$')
TOKEN = '< DISCORD BOT TOKEN HERE >'

def get_movie_token():
	f = open('keys', 'r+')
	for line in f.readlines(0):
		print(line)
	return line
	
def make_token():
	n = os.urandom(8).hex()
	print(n)
	f = open('keys', 'a')
	f.write('{0}\n'.format(n))
	f.close()
	print(n)
	return n

def get_movie_list():
	i = 0
	for movie in os.listdir('/mnt/4f510889-32ca-4946-8d2c-09e9570d7cff/discordbot/static/Movies'):
		i+=1
		movielist.append('\n({0}) '.format(i) + movie)

def get_tv_list():	
	for tv in os.listdir('/mnt/4f510889-32ca-4946-8d2c-09e9570d7cff/discordbot/static/TV'):
		tvlist.append(tv)

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
	if message.content == '$test':
		await message.channel.send('Testing 1 2 3!')


	if message.content == '$getmovielist':
		i = 0
		print(movielist)
		print(len(movielist))
		print(round(len(movielist)/10))
		
		embed = discord.Embed(title="`A wild pokemon appeared", description='```<br> diff -{0}```'.format(movielist[:13]))	
		await message.channel.send(embed=embed)
		await message.author.send("```diff -asdf ```")

	if message.content == '$gettvlist':
		i = 0
		for tv in tvlist:
			await message.author.send('{0}) {1}'.format(i, tv))
			i+=1

	if '$getmovie' in message.content:
		s = re.compile(r'\$getmovie.(\d*)')
		res = s.search(message.content)
		num = res.group(1)
		print(num)
		await message.author.send('http://74.88.95.5/movie/{0}/{1}'.format(num, make_token()))
		


get_movie_list()
get_tv_list()
bot.run(TOKEN)
