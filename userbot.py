import discord
import os
from dotenv import load_dotenv
from variables import *

#############################
#Replying Section
#############################

intents = discord.Intents.all()

load_dotenv(path + "//dc.env")

# TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

TOKEN = os.getenv('USER_TOKEN')

BOT_CHANNEL = int(os.getenv('DISCORD_BOTCHANNEL'))
CHANNEL101 = int(os.getenv('CHANNEL101'))
CHANNELFOREST = int(os.getenv('CHANNELFOREST'))
EMAIL = os.getenv('EMAIL')
PSWD = os.getenv('PSWD')


#Instaniate bot connection client
client = discord.Client(intents = intents)



@client.event
async def on_ready():

    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break
    # print(client.guilds) SequenceProxy(dict_values([<Guild id=890789267687764021 name='杀鸡' shard_id=0 chunked=False member_count=97>]))

    #discord.utils.get(iterable, /, **attrs)
    #A helper that returns the first element in the iterable that meets all the traits passed in attrs. This is an alternative for find().

#When multiple attributes are specified, they are checked using logical AND, not logical OR. Meaning they have to meet every attribute passed in and not one of them.
    guild = discord.utils.get(client.guilds, name = '杀鸡')

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

    channel = client.get_channel(BOT_CHANNEL)
    await channel.send('这是一条神奇的信息')


client.run(TOKEN)
