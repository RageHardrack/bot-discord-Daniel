import discord
import os
from discord.ext import commands, tasks
from botToken import tokenBot

# Bot HK-47 creado por Daniel Colmenares el 22 de septiembre de 2020

HK47_bot = commands.Bot(command_prefix='!', description="Este es un bot creado por Daniel Colmenares usando Python")

# Cogs
@HK47_bot.command()
async def load(ctx, extension):
    HK47_bot.load_extension(f'cogs.{extension}')

@HK47_bot.command()
async def unload(ctx, extension):
    HK47_bot.unload_extension(f'cogs.{extension}')

@HK47_bot.command()
async def reload(ctx, extension):
    HK47_bot.load_extension(f'cogs.{extension}')
    HK47_bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        HK47_bot.load_extension(f'cogs.{filename[:-3]}')

# Token de HK-47
HK47_bot.run(tokenBot)