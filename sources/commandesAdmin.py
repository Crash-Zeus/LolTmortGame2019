# FICHIER COMMANDES ADMIN BOT
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
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende")
async def clear(channel, amout=1):
    await channel.channel.purge(limit=amout + 1)

@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende")
async def addplayer(ctx, player):
    with open(fichier, "r") as json_data:
        data = json.load(json_data)
    data[player] = "0"
    with open(fichier, 'w') as file:
        json.dump(data, file, indent=2)
    await ctx.send(player + " ajouter. Score de " + player + " : 0")
    print("add " + player + " to game")


@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende")
async def kickplayer(ctx, player):
    with open(fichier, 'r') as file:
        data = json.load(file)
    del data[player]
    with open(fichier, 'w') as file:
        json.dump(data, file, indent=2)
    await ctx.send(player + " supprimer")
    print("delete " + player + " from game")

@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende")
async def mort(ctx, player):
    with open(fichier, 'r') as file:
        json_data = json.load(file)
    nbrMort = int(json_data[player]) + int(1)
    json_data[player] = nbrMort
    with open(fichier, 'w') as file:
        json.dump(json_data, file, indent=2)
    await ctx.send(player + " est mort. Score de " + player + " : " + str(json_data[player]))
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    player = await YTDLSource.from_url("https://www.youtube.com/watch?v=InBZINtS0ec", loop=bot.loop)
    ctx.voice_client.play(player, after=lambda e: print(
        'Player error: %s' % e) if e else None)
    print('{}'.format(player.title))
    while ctx.voice_client.is_playing():
        await asyncio.sleep(0.5)
    await bot.voice_clients[0].disconnect()


@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende")
async def retard(ctx, player):
    with open(fichier, 'r') as file:
        json_data = json.load(file)
    scoreAjout = int(json_data[player]) + int(10)
    json_data[player] = scoreAjout
    with open(fichier, 'w') as file:
        json.dump(json_data, file, indent=2)
    await ctx.send(player + " à été absent ou en retard. Score de " + player + " : " + str(json_data[player]))


@clear.error
@kickplayer.error
@addplayer.error
@mort.error
@retard.error
async def notPerm(ctx, player):
    await ctx.send("{}, tu n'a pas le droit d'utiliser cette commande.".format(ctx.message.author.mention))