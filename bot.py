import discord
import os
import pyjokes


client = discord.Client()
what = "what"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Python 3.6.7"))
    
#bot.hello
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('bot.hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

#bot.joke
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('bot.joke'):
            msg = pyjokes.get_joke().format(message)
            await client.send_message(message.channel, msg)
            
            

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
