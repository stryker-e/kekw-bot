# bot.py
import os
import discord

from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = Bot(command_prefix='!')

#replace this id with the string returned
kekw_id = 'none'
bot_listen = True

@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Game(name='Waiting for emoji ping'))
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # command to toggle bot on and off
    if message.content == '!toggle':
        global bot_listen
        if bot_listen == True:
            await bot.change_presence(activity=discord.Game(name='Not waiting for emoji ping'))
        else:
            await bot.change_presence(activity=discord.Game(name='Waiting for emoji ping'))
        bot_listen = not bot_listen
        await message.channel.send('Listening status has been changed.')

    if bot_listen == True:
        # command to get commands
        if message.content == '!help':
            await message.channel.send('Send \"!change\" to change your emoji ping. Send \"!check\" and I\'ll tell you what your current emoji ping is.')

            # command to change emoji ping
        if message.content == '!change':
            global kekw_id
            await message.channel.send('Change emoji ping: Enter the custom emoji id in the format ```\n\:emoji_alias:\n``` Send \"!cancel\" to keep the current emoji ping.')
            
            # verify emoji id format
            def check(msg):
                return (msg.channel == message.channel and msg.content.endswith('>')) or (msg.channel == message.channel and msg.content == '!cancel')

            response = await bot.wait_for('message', check=check)
            # set kekw_id to emoji_id without the escape character
            if response.content == '!cancel':
                await message.channel.send('Ok, I won\'t change the emoji ping.')
            else: 
                kekw_id = str(response.content)[1:]
                await message.channel.send('You\'ve set the emoji ping to {.content}!'.format(response))

        if message.content == '!check':
            await message.channel.send('Your current emoji ping is ' + kekw_id)

        if message.author.id == bot.user.id:
            return

        if message.content.startswith(kekw_id) and kekw_id != '':
            if message.author.id == 508000673946927136:
                return
            await message.channel.send(kekw_id)

        if message.content.startswith(kekw_id) and kekw_id == 'none':
            await message.channel.send('You have to set the emoji ping using \'!change\' first.')
      

bot.run(TOKEN)