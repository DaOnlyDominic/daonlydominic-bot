import discord
import os
import random

links = ['', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.dailydot.com%2Fwp-content%2Fuploads%2F2018%2F12%2FBig-Chungus-Meme.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fstayhipp.com%2Fwp-content%2Fuploads%2F2018%2F12%2Fchunkus.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fp8RzYUeXrzM%2Fhqdefault.jpg&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Forig14.deviantart.net%2Fae8b%2Ff%2F2015%2F148%2F0%2F5%2Fsad_pepe__feels_bad_man__vector_by_hirussai-d8uq43y.png&f=1', 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.ukrBqoJWneek-iP_0Zh3UQHaE8%26pid%3D15.1&f=1', 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-0nIYq5XweXM%2FUNU9XfV48zI%2FAAAAAAAAAN4%2Fk-aOKxDqVcE%2Fs1600%2FAre%2Byou%2Bready.jpg&f=1']

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
      msg = 'D̵̷̗̦̖̜̬͈͔̥͇̼̖͖̙̗̣̝̘̝̅ͤͨ̇ͣ̾̌̍͊̇͛͛ͨ̍͌͡a̸̿̆̏͒ͧ̾͂̈́͌̇̉͏̗̱̲̬̤͚̲̖͉̤͚̣̥̰̼͡O̷̠̜͙̟̒͋̈́ͣͫ̑ͣͨ̑͛͑̅̀̐̽́̀͞͝ͅn̓ͯ̈́̓ͩ̊͑̆̏̈́͏̶̵͕̹͙͓͎̩̻̭̥͕͉̗̬̭̥̜͈͘͢l̛͓̲͇͚̝̭̣̱̣̙͉̓͋̈́ͬ̏͡͡yͤ̍̀̾̓̓̓ͬ̅ͥ̐ͤͫ̋ͤ́̿͝͏̧̻̳͓̩͉̯̺̩͘͟D̡̞̰̪̼̼̠̓͋ͫͮͬͯ̽̊̆ͭ̑͛̓̈̂͆̕͟ŏ̸̢̲̠͎̠͍͈͉̖͓̫̫̑̾ͣ̌͑ͩͩ̾͋ͫͥ̐̚m̧͖͕̳̺̱̟̝̹͍͎̻̖̣̺̤̱̞̹̓ͦͦ͒́̕̕i̅͐̃̓҉͏̸̦̪͓͇̩͖͚͖̳̦͓̲̀͞n̊̄̎̊̓ͣ͆̄͠͞҉͚̲̰̖͉̙̪͕͓̞͉͟į̴̨͖̻̲̮̬͍͙͔̫̮̬͓̘͚̭̝͈̙͂̅̐̆͗ͤͫͧ̎̄̅ͦ́c̡̱͇̖͌̿͛̐ͩ̉̋́̈ͮͬ͜ͅ ̧̡̛̫̝̥̞̱̺̺̱̹̰͔̣͖ͦ͛͐ͤͤ͛ͧ̇ͧͮȉ̵̞̥̭͓̜͎̭̝̜̥̯̪̺͊̇̆ͅs̵͙̳͉̟̥͍̫͔̥̬͓̙̜͎͍̻ͦ́͒̀ ̵̦̯̮̲ͯͧ̂̔̀ͦ̅̂ͦ̏̈́͊̌ͬḨ̵̨̠͉̘̖͉͔̬̣͎̫͕̌̃̿̅ͦ͐̍͛̑ͬ̈͘͡A̴͈̟̣͚̪͎̱͖̜̯͍͍͇̤͎̳̜̜̲͂͊̑͗ͬ́ͩͭ͌̀̚͡C̡͖̪̪̱͈̥͈̼͔͚̮͚̙͖̼͈̞̮̉̂̅ͥͩ͂ͥ̊̋͌̽͐̓͋͑̈́ͮ̂͡K͊ͦ͑̅̊̅̊͒̃̒ͫ͂̈͏͉͎͈͈̠̫͔͍̯̺͍̭͕͠ͅͅȄ̡̧̡̛͚̯̤̱̼̩̣͈͎̳̥̪̩͎̗͕ͨ̾ͩ͑ͤ͂̑̚̚͠R͖̝̝̬̥̗̞͉̰̞̯̺̹͉̟̠̐̆̈́̈̃̓͗͋ͭ̓̈́͋ͤ͘͜͡ͅ'.format(message)
      await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.meme'):
      num = random.randint(0,5)
      msg = links[num]
      await client.send_message(message.channel, msg)

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
