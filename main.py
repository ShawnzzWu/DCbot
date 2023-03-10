# bot.py
import os
import ssl
import discord

import chat_exporter
# import pandas as pd
# import random
from dotenv import load_dotenv
from botcds import *
from variables import *
import variables as vr


#############################
#Replying Section
#############################

intents = discord.Intents.all()

load_dotenv(path + "//dc.env")

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')  
BOT_CHANNEL = int(os.getenv('DISCORD_BOTCHANNEL'))







#Instaniate bot connection client
client = discord.Client(intents = intents)



#############################
#Replying Section
#############################

#A function to detect if specific word is appearing in the context
async def embedded_feedback(message):
    for i, r in ef.iterrows():

        if r['include'] in message.content:
            if len(r['exclude']) > 0:
                if r['exclude'] not in message.content:
                    await message.channel.send(r['print'])
            else:
                await message.channel.send(r['print'])


#A function to detect if specific word is the context
async def feedback(message):
    # print(message.content, pf[['include']].values, message.content in pf[['include']].values)
    if message.content in vr.pf[['include']].values:
        index = vr.pf[vr.pf['include'] == message.content].index[0]
        await message.channel.send(vr.pf['print'].iloc[index])
    else:
        await embedded_feedback(message)




#A function to check the command and operate commands
async def command(message):
        temp = message.content[1:].split()

        for i in commandlst:
            if temp[0] == i[0]:
                await i[3](message)




#A function to detect command or chat to reply
async def reading(message):

    try:
        if message.content[0] != '[' or len(message.content) <= 1:
            await feedback(message)
        else:
            await command(message)
    except:
        pass



#############################
#Event Section
#############################

#detect message event sent by non-bot user
@client.event
async def on_message(message):

    if message.author.bot:
        return

    #Detect if the user is being targeted by a verbal abuse
    if str(message.author.id) == list(vr.target.keys())[0][2: -1]:
        await attack(message)
    else:
        await reading(message)



@client.event
async def on_ready():

    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break
    # print(client.guilds) SequenceProxy(dict_values([<Guild id=890789267687764021 name='??????' shard_id=0 chunked=False member_count=97>]))

    #discord.utils.get(iterable, /, **attrs)
    #A helper that returns the first element in the iterable that meets all the traits passed in attrs. This is an alternative for find().

#When multiple attributes are specified, they are checked using logical AND, not logical OR. Meaning they have to meet every attribute passed in and not one of them.
    guild = discord.utils.get(client.guilds, name = '??????')

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')


    # channel = client.get_channel(BOT_CHANNEL)  # Gets channel from internal cache
    #
    # await channel.send('?????? ??????!')

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

# async def on_disconnect():
#     channel = client.get_channel(BOT_CHANNEL)  # Gets channel from internal cache
#
#     await channel.send('????????????')


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, '
#     )



#############################
#Operating Section
#############################
client.run(TOKEN)
