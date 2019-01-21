import discord
import os
import random


client = discord.Client()
jokes = ["What do you call a dull pencil?", "What do you call a cow with no legs?", "", "", ""]
answers = ["Pointless!", "Ground beef!", "", "", ""]
what = "what"

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
      await client.send_message(message.channel, 'Hello {0.author.mention}')

#bot.zalgo
@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.zalgo'):
      await client.send_message(message.channel, 'D̵̷̗̦̖̜̬͈͔̥͇̼̖͖̙̗̣̝̘̝̅ͤͨ̇ͣ̾̌̍͊̇͛͛ͨ̍͌͡a̸̿̆̏͒ͧ̾͂̈́͌̇̉͏̗̱̲̬̤͚̲̖͉̤͚̣̥̰̼͡O̷̠̜͙̟̒͋̈́ͣͫ̑ͣͨ̑͛͑̅̀̐̽́̀͞͝ͅn̓ͯ̈́̓ͩ̊͑̆̏̈́͏̶̵͕̹͙͓͎̩̻̭̥͕͉̗̬̭̥̜͈͘͢l̛͓̲͇͚̝̭̣̱̣̙͉̓͋̈́ͬ̏͡͡yͤ̍̀̾̓̓̓ͬ̅ͥ̐ͤͫ̋ͤ́̿͝͏̧̻̳͓̩͉̯̺̩͘͟D̡̞̰̪̼̼̠̓͋ͫͮͬͯ̽̊̆ͭ̑͛̓̈̂͆̕͟ŏ̸̢̲̠͎̠͍͈͉̖͓̫̫̑̾ͣ̌͑ͩͩ̾͋ͫͥ̐̚m̧͖͕̳̺̱̟̝̹͍͎̻̖̣̺̤̱̞̹̓ͦͦ͒́̕̕i̅͐̃̓҉͏̸̦̪͓͇̩͖͚͖̳̦͓̲̀͞n̊̄̎̊̓ͣ͆̄͠͞҉͚̲̰̖͉̙̪͕͓̞͉͟į̴̨͖̻̲̮̬͍͙͔̫̮̬͓̘͚̭̝͈̙͂̅̐̆͗ͤͫͧ̎̄̅ͦ́c̡̱͇̖͌̿͛̐ͩ̉̋́̈ͮͬ͜ͅ ̧̡̛̫̝̥̞̱̺̺̱̹̰͔̣͖ͦ͛͐ͤͤ͛ͧ̇ͧͮȉ̵̞̥̭͓̜͎̭̝̜̥̯̪̺͊̇̆ͅs̵͙̳͉̟̥͍̫͔̥̬͓̙̜͎͍̻ͦ́͒̀ ̵̦̯̮̲ͯͧ̂̔̀ͦ̅̂ͦ̏̈́͊̌ͬḨ̵̨̠͉̘̖͉͔̬̣͎̫͕̌̃̿̅ͦ͐̍͛̑ͬ̈͘͡A̴͈̟̣͚̪͎̱͖̜̯͍͍͇̤͎̳̜̜̲͂͊̑͗ͬ́ͩͭ͌̀̚͡C̡͖̪̪̱͈̥͈̼͔͚̮͚̙͖̼͈̞̮̉̂̅ͥͩ͂ͥ̊̋͌̽͐̓͋͑̈́ͮ̂͡K͊ͦ͑̅̊̅̊͒̃̒ͫ͂̈͏͉͎͈͈̠̫͔͍̯̺͍̭͕͠ͅͅȄ̡̧̡̛͚̯̤̱̼̩̣͈͎̳̥̪̩͎̗͕ͨ̾ͩ͑ͤ͂̑̚̚͠R͖̝̝̬̥̗̞͉̰̞̯̺̹͉̟̠̐̆̈́̈̃̓͗͋ͭ̓̈́͋ͤ͘͜͡ͅ')

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith('bot.chungus'):
      await client.send_message(message.channel, 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fstayhipp.com%2Fwp-content%2Fuploads%2F2018%2F12%2Fchunkus.jpg&f=1')

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
