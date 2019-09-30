# FICHIER COMMANDES ALL BOT
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

client = discord.Client()
TOKEN = ""
bot = commands.Bot(command_prefix='²')
fichier = 'score.json'


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(
            name='voler des bot')
    )
    print('Bot {0.user} online'.format(bot)+"\n<-------------->")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="**Voldebot**", description="Bot développé par Crash à l'occasion du LOLTMORTGAME 2019, français corrigé par Fred \n",
        color=0xeee657, inline=False
    )
    embed.add_field(
        name="**Préfix du bot**",
        value="Toujours utilisé le préfixe **²** pour appeler une commande de ce bot",
        inline=False
    )
    embed.add_field(
        name="**Commandes all**",
        value="loltmort \n score \n info \n horaire \n decide \n sur \n jadorelamusique \n echecmode nom_du_joueur \n",
        inline=False
    )
    embed.add_field(
        name="**Commandes admin seulement (et Crash lul logik)**",
        value="clear nbr_messages_clear \n mort pseudo_du_joueur \n addplayer pseudo_du_joueur \n kickplayer pseudo_du_joueur \n stop \n",
        inline=False
    )
    embed.add_field(
        name="**Pseudo des joueurs reconnu par le bot**",
        value="crash, fred, tsuna, easy, iruhn, shiyu",
        inline=False
    )
    embed.set_thumbnail(
        url="https://i.pinimg.com/originals/73/c1/e6/73c1e6eefc15fcc928d111d3e87f19f8.jpg")
    await ctx.send(embed=embed)


@bot.command()
async def score(ctx):
    with open(fichier, "r") as json_data:
        data_dict = json.load(json_data)
    scores = str(data_dict).replace("[", " ").replace("]", " ").replace(
        "{", " ").replace("}", " ").replace("'", " ").replace(",", "\n")
    scoreEmbed = discord.Embed(
        title="Premier gage :",
        description="Easy - Fail challenge facile",
        color=0xFF0000, inline=False
    )
    scoreEmbed.add_field(
        name="Score des morts",
        value=scores,
        inline=False
    )
    await ctx.send(embed=scoreEmbed)


@bot.command()
async def shana(ctx):
    message = "**BIP BIP ! **" + \
        "http://image.noelshack.com/fichiers/2019/39/7/1569765622-shana.jpeg"
    await ctx.send(message)


@bot.command()
async def fred(ctx):
    message = "**UP HUPPERMAGE WHEN ? **" + \
        "http://image.noelshack.com/fichiers/2019/39/7/1569766833-fred.jpeg"
    await ctx.send(message)


@bot.command()
async def addRSA(ctx):
    await ctx.send("http://image.noelshack.com/fichiers/2017/30/4/1501150374-1455211242-mario-non.png")


@bot.command()
async def suicide(ctx):
    await ctx.send("https://starecat.com/content/wp-content/uploads/man-su-looking-at-suicide-instead-of-success-red-dress-meme.jpg")


@bot.command()
async def wakfu(ctx):
    await ctx.send("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5OltV8auJDomF4BQ8O9jGk30fJojXwqpwDprCP6x7KFbQYlDR")


@bot.command()
async def horaire(ctx):
    await ctx.send("http://image.noelshack.com/fichiers/2019/39/5/1569612439-screenshot-20190927-212652.png \n\n")
    await ctx.send("**Les horaire fournis sont une base pour pouvoir monter un event de manière cohérent, veuillez PREVENIR au plus tôt si il y a des changements a faire ou des évenement spéciaux (absence)**")
    await ctx.send("**Pour toute abscence non prévenue le joueur se verras attribuer +10 à sont score, vous comprennez qu'une abscence oblige tout le monde à ne pas pouvoir jouer.**")

# VOCAL


@bot.command()
async def jadorelamusique(ctx):
 if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
                if ctx.author.voice:
                    vc = await channel.connect(timeout=600,reconnect=False)
    async with ctx.typing():
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=NcKAdFENqig", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
    await ctx.send('{}'.format(player.title))
    print('{}'.format(player.title))
    while ctx.voice_client.is_playing():
        await asyncio.sleep(1)
 else:
    await ctx.send("Vous devez être en vocal pour utiliser cette commande")


@bot.command()
async def decide(ctx):
 if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
                if ctx.author.voice:
                    vc = await channel.connect(timeout=600,reconnect=False)
    async with ctx.typing():
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=N_VUkp_DmA4", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
    await ctx.send('{}'.format(player.title))
    print('{}'.format(player.title))
    while ctx.voice_client.is_playing():
        await asyncio.sleep(1)
 else:
    await ctx.send("Vous devez être en vocal pour utiliser cette commande")


@bot.command()
async def sur(ctx):
 if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
                if ctx.author.voice:
                    vc = await channel.connect(timeout=600,reconnect=False)
    async with ctx.typing():
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=-hUyGo2y-pc", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
    await ctx.send('{}'.format(player.title))
    print("MAIS CT SUR PTN")
    while ctx.voice_client.is_playing():
        await asyncio.sleep(1)
 else:
    await ctx.send("Vous devez être en vocal pour utiliser cette commande")
