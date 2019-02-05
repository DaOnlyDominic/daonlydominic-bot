import discord
import os
import random

links = ['', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.dailydot.com%2Fwp-content%2Fuploads%2F2018%2F12%2FBig-Chungus-Meme.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fstayhipp.com%2Fwp-content%2Fuploads%2F2018%2F12%2Fchunkus.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fp8RzYUeXrzM%2Fhqdefault.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Forig14.deviantart.net%2Fae8b%2Ff%2F2015%2F148%2F0%2F5%2Fsad_pepe__feels_bad_man__vector_by_hirussai-d8uq43y.png&f=1', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.ukrBqoJWneek-iP_0Zh3UQHaE8%26pid%3D15.1&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-0nIYq5XweXM%2FUNU9XfV48zI%2FAAAAAAAAAN4%2Fk-aOKxDqVcE%2Fs1600%2FAre%2Byou%2Bready.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.blogcdn.com%2Fslideshows%2Fimages%2Fslides%2F367%2F261%2F4%2FS3672614%2Fslug%2Fl%2Fscreen-shot-2015-10-21-at-7-51-12-pm-1.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.picshunger.com%2Fwp-content%2Fuploads%2F2014%2F04%2Fdeath-once-had-photo-u1.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fc3.thejournal.ie%2Fmedia%2F2013%2F04%2Fchuck-norris-vs-nokia-3310_1-495x375.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F000%2F232%2F787%2F4aa.jpg&f=1', 'https://lh3.googleusercontent.com/-Otb9Jmjsr5c/XEXmpsUqfYI/AAAAAAAAAKU/QDQwGQ13r0UIvGZqzxu5YBZtSeZ9rGt5gCK8BGAs/s490/2019-01-21.png']

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('I\'m ready')
  print('------')
  await client.change_presence(game=discord.Game(name="Python 3.6.7")
  )
    
#bot.hello
@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.hello'):
      msg = 'Hello {0.author.mention}'.format(message)
      await client.send_message(message.channel, msg)

#bot.zalgo
@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.zalgo'):
      msg = 'ă̆̆̆̆̆̆̆̆̆̆̆̆̆'.format(message)
      await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.meme'):
      num = random.randint(0,10)
      msg = links[num]
      await client.send_message(message.channel, msg)
      
@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.spam'):
      def bb:
        aa()
      def aa:
        async client.send_message(message.channel, "SPAM!!")
        bb()
      

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
