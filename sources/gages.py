import asyncio
import json
import os
import random
import sys

import discord
import youtube_dl
from discord.ext import commands
from discord.voice_client import VoiceClient

from sources.ytbMusic import YTDLSource
from sources.commandesAll import fichier,bot

@bot.command()
async def loltmort(ctx):
    await ctx.send("**Je choisi mon gage... ** <a:loading:582690307699638297>")
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        if ctx.voice_client is None:
                    if ctx.author.voice:
                        vc = await channel.connect(timeout=600,reconnect=False)
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=o6RQuIbzwJk", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
        print('{}'.format(player.title))
    else:
        await asyncio.sleep(2)
    with open('gages.json') as fp:
        data = json.load(fp)
    nbr = random.choice(list(data))
    choose = data[nbr] + " !\nHave Fun with LOLTMORTGAME <a:SpinMaster:582689451935793177>"
    await ctx.send(str(choose))

@bot.command()
async def echecmode(ctx, player = None):
    if player is None:
        await ctx.send("Pseudo du joueur manquant")
    else:
        with open('pions.json') as fp:
            data = json.load(fp)
        nbr = random.choice(list(data))
        pion = data[nbr]
        joueur = player
        await ctx.send(f'{joueur} incarne ' + str(pion))


@bot.command()
async def gagelist(ctx):
    await ctx.send(file=discord.File('gages.json'))
