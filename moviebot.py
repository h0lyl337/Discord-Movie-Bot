import discord
from discord.ext.commands import Bot
import os
import re

movielist = []
premusers = ['239357844573388800']
tvlist = []

bot = Bot(command_prefix='$')
#insert your token here
TOKEN = 'TOKEN HERE'

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
	for movie in os.listdir('/mnt/4f510889-32ca-4946-8d2c-09e9570d7cff/discordbot/static/Movies'):
		movielist.append(movie)

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

	if message.content == '$help':
		embed = discord.Embed(title="A wild pokemon appeared", description="capture the pokemon before it leaves.",color=int(0xFF0000))
		embed.set_image(url='https://projectpokemon.org/images/normal-sprite/bulbasaur.gif')
		embed.add_field(name="Bulbasaur", value="Grass/Normal")
		embed.add_field(name="Lvl:", value="99")
		embed.add_field(name="HP:", value="100/100")
		embed.add_field(name="Skills:", value="""razor leaf\n vine whip\n None\n None""")
		embed.add_field(name="Held Item:", value="Premium Stone")
		
		await message.channel.send(embed=embed)
		userid = message.author.id
		user = message.author.name
		await message.author.send('''command list: \n
			$getmovielist\n
			$gettvlist\n
			$getmovie "movie number here"\n
			$gettv "tv number here"\n
			$help\n
			''')
		print(userid)

	if message.content == '$getmovielist':
		i = 0
		for movie in movielist:
			await message.author.send('{0}) {1}'.format(i, movie))
			i+=1

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
