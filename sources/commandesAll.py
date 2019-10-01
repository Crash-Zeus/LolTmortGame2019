# FICHIER COMMANDES ALL BOT
import asyncio
import json
import os
import random
import sys

import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.voice_client import VoiceClient

from sources.ytbMusic import YTDLSource

client = discord.Client()
TOKEN = "NjI1NjIzOTU0NDQyMTU4MDkw.XZHKxw.U8DmvyFvfiEwuBemUee45vWELnw"
bot = commands.Bot(command_prefix='²')
fichier = 'score.json'


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(
            name='voler des bot')
    )
    print('Bot {0.user} online'.format(bot)+"\n<-------------->")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return await ctx.send("T ki ? la commande existe pas. <:omegalul:582685706267394051>")
    raise error


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="**Voldebot**", description="Bot développé par Crash à l'occasion du LOLTMORTGAME 2019, français corrigé par Fred \n",
        color=0xeee657, inline=False
    )
    embed.add_field(
        name="**Préfix du bot**",
        value="Toujours utilisé le préfixe **²** pour appeler une commande de ce bot \n La commande gagelist vous renverras le fichier json contenant tout les gages du LOLTMORTGAME \n La commande clean prend automatiquement en compte le message de la commande",
        inline=False
    )
    embed.add_field(
        name="**Commandes all**",
        value="loltmort \n score \n info \n horaire \n decide \n sur \n jadorelamusique \n echecmode *nom_du_joueur* \n gagelist \n",
        inline=False
    )
    embed.add_field(
        name="**Commandes admin seulement (Légende + et Crash lul logik)**",
        value="clear *nbr_messages_clear* \n mort *pseudo_du_joueur* \n addplayer *pseudo_du_joueur* \n kickplayer *pseudo_du_joueur* \n stop \n addgage \"*gage*\" \n",
        inline=False
    )
    with open(fichier, "r") as json_data:
        data_dict = json.load(json_data)
    perso = list(data_dict)
    embed.add_field(
        name="**Pseudo des joueurs reconnu par le bot**",
        value=str(perso).replace("[", "").replace("]", "").replace("'", ""),
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
    with open('Wakmeme.json') as fp:
        data = json.load(fp)
    nbr = random.choice(list(data))
    meme = data[nbr]
    await ctx.send(str(meme) + "\n")


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
                vc = await channel.connect(timeout=600, reconnect=False)
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
                vc = await channel.connect(timeout=600, reconnect=False)
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
                vc = await channel.connect(timeout=600, reconnect=False)
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
