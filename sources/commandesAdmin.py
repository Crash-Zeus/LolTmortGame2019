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
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende", "Dev")
async def clear(channel, amout = 1):
    await channel.channel.purge(limit=amout + 1)

@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende", "Dev")
async def addplayer(ctx, player = None):
    if player is None:
        await ctx.send("Pseudo du joueur manquant")
    else:
        with open(fichier, "r") as json_data:
            data = json.load(json_data)
        data[player] = "0"
        with open(fichier, 'w') as file:
            json.dump(data, file, indent=2)
        await ctx.send(player + " ajouter. Score de " + player + " : 0")
        print("add " + player + " to game")


@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende", "Dev")
async def kickplayer(ctx, player = None):
    if player is None:
        await ctx.send("Pseudo du joueur manquant")
    else:
        with open(fichier, 'r') as file:
            data = json.load(file)
        del data[player]
        with open(fichier, 'w') as file:
            json.dump(data, file, indent=2)
        await ctx.send(player + " supprimer")
        print("delete " + player + " from game")

@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende", "Dev")
async def mort(ctx, player = None):
    if player is None:
        await ctx.send("Pseudo du joueur manquant")
    else:
        with open(fichier, 'r') as file:
            json_data = json.load(file)
        nbrMort = int(json_data[player]) + int(1)
        json_data[player] = nbrMort
        with open(fichier, 'w') as file:
            json.dump(json_data, file, indent=2)
        await ctx.send(player + " est mort. Score de " + player + " : " + str(json_data[player]))
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            if ctx.voice_client is None:
                        if ctx.author.voice:
                            vc = await channel.connect(timeout=600,reconnect=False)
            player = await YTDLSource.from_url("https://www.youtube.com/watch?v=InBZINtS0ec", loop=bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(
                'Player error: %s' % e) if e else None)
            while ctx.voice_client.is_playing():
                await asyncio.sleep(0.5)



@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende", "Dev")
async def retard(ctx, player = None):
    if player is None:
        await ctx.send("Pseudo du joueur manquant")
    else:
        with open(fichier, 'r') as file:
            json_data = json.load(file)
        scoreAjout = int(json_data[player]) + int(10)
        json_data[player] = scoreAjout
        with open(fichier, 'w') as file:
            json.dump(json_data, file, indent=2)
        await ctx.send(player + " à été absent ou en retard. Score de " + player + " : " + str(json_data[player]))

@bot.command()
@commands.has_any_role("Conseil des Oracles", "Oracle", "Leader", "Nitro Booster", "Légende", "Dev")
async def stop(ctx):
    if ctx.voice_client is not None:
        await bot.voice_clients[0].disconnect()
    else:
        await ctx.send("le bot est déjà déconnecté de tout les salons vocaux")

@clear.error
@kickplayer.error
@addplayer.error
@mort.error
@retard.error
@stop.error
async def notPerm(ctx, player):
    await ctx.send("{}, tu n'a pas le droit d'utiliser cette commande.".format(ctx.message.author.mention))