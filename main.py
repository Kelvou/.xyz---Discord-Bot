import discord
from discord.ext import commands, tasks
from discord.errors import Forbidden
import youtube_dl

from random import choice
from flask import Flask
from threading import Thread

import os

from keep_alive import keep_alive

client = commands.Bot(command_prefix='!x ')


@tasks.loop(seconds=0)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Dream Team Server'), status=discord.Status.do_not_disturb)
  
  

@client.event
async def on_ready():
  change_status.start()
  print('{0.user} is online!'.format(client))

@client.command(name='ping', help=': Retorna la latencia.')
async def ping(ctx):
    await ctx.send(f'**¡Pong!** Latencia: {round(client.latency * 1000)}ms')

@client.command(name='hello', help=': Devuelve un saludo.')
async def hello(ctx):
    responses = ['* ***Bosteza*** * ¿Por qué tan de madrugada?', 'Lo mejor en este día para ti. :)', '¡Hola!', '¡Hola, ten un buen día!']
    await ctx.send(choice(responses))

client.remove_command('help')

@client.command(name='help')
async def help(ctx):
    await ctx.send('Este es mi mensaje de ayuda personalizado')

keep_alive()
client.run(os.environ['token'])
