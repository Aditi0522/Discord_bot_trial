import discord
import os
from dotenv import load_dotenv
import logging 
import links
from discord.ext import commands

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#load environment variables from .env file
load_dotenv()

#declaring intents
intents = discord.Intents.default()
intents.message_content = True
intents.members=True
bot = commands.Bot(command_prefix='!', intents=intents)

#client--our_bot
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Hello!') 

  channel_id = links.resources.get(message.content.lower())   

  await message.channel.send(channel_id)      

@bot.event
async def on_message(message):
    for word in message.content.lower().split(" "):
        if word in list(links.resources.keys()):
            await message.channel.send(links.resources[word])            

#run the client on the server
client.run(os.environ['TOKEN'],log_handler=handler, log_level=logging.DEBUG)