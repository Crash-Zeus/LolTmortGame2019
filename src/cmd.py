# FICHIER COMMANDES BOT
import asyncio
import json
import os
import random
import sys

import discord
import youtube_dl
from discord.ext import commands
from discord.voice_client import VoiceClient

from src.music import YTDLSource

client = discord.Client()
TOKEN = ""
bot = commands.Bot(command_prefix='²')
fichier = 'score.json'


# @bot.command()
# # Command de clear channel posté
# # Nbr de message demandé + 1 (commande clear auto delete)
# async def clear(channel, amout=1):
#     await channel.channel.purge(limit=amout + 1)

# @bot.command()
# async def play(ctx, url):
#     channel = ctx.message.author.voice.channel
#     vc = await channel.connect()
#     async with ctx.typing():
#         player = await YTDLSource.from_url(url, loop=bot.loop)
#         ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
#     await ctx.send('{}'.format(player.title))
#     print('{}'.format(player.title))
#     while ctx.voice_client.is_playing():
#         await asyncio.sleep(0.5)
#     await bot.voice_clients[0].disconnect()

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
        title="Voldebot", description="Wallah t'es mort frère <:innocent:625807221250326528>",
        color=0xeee657, inline=False
    )
    embed.add_field(
        name="Commandes",
        value="²loltmort, ²score, ²mort [pseudo], ²info, ²horaire, ²decide, ²sur, ²musique",
        inline=False
    )
    embed.add_field(
        name="Pseudo des joueur reconnue par le bot",
        value="crash, fred, tsuna, easy, iruhn, shiyu, ruby",
        inline=False
    )
    await ctx.send(embed=embed)


@bot.command()
async def score(ctx):
    with open("score.json", "r") as json_data:
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
async def mort(ctx, player):
    with open(fichier, 'r') as file:
        json_data = json.load(file)
    for item in json_data:
        if item[player]:
            nbrMort = int(item[player]) + int(1)
            item[player] = nbrMort
    with open(fichier, 'w') as file:
        json.dump(json_data, file, indent=2)
    await ctx.send(player + " est mort. Score de " + player + " : " + str(item[player]))


@bot.command()
async def horaire(ctx):
    await ctx.send("http://image.noelshack.com/fichiers/2019/39/5/1569612439-screenshot-20190927-212652.png \n\n")
    await ctx.send("**Les horaire fournis sont une base pour pouvoir monter un event de manière cohérent, veuillez PREVENIR au plus tôt si il y a des changements a faire ou des évenement spéciaux (absence)**")
    await ctx.send("**Pour toute abscence non prévenue le joueur se verras attribuer +10 à sont score, vous comprennez qu'une abscence oblige tout le monde à ne pas pouvoir jouer.**")


@bot.command()
async def musique(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    async with ctx.typing():
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=NcKAdFENqig", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
    await ctx.send('{}'.format(player.title))
    print('{}'.format(player.title))
    while ctx.voice_client.is_playing():
        await asyncio.sleep(0.5)
    await bot.voice_clients[0].disconnect()


@bot.command()
async def decide(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    async with ctx.typing():
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=N_VUkp_DmA4", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
    await ctx.send('{}'.format(player.title))
    print("C PAS TOA QUI DECIDE")
    while ctx.voice_client.is_playing():
        await asyncio.sleep(0.5)
    await bot.voice_clients[0].disconnect()


@bot.command()
async def sur(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    async with ctx.typing():
        player = await YTDLSource.from_url("https://www.youtube.com/watch?v=-hUyGo2y-pc", loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(
            'Player error: %s' % e) if e else None)
    await ctx.send('{}'.format(player.title))
    print("MAIS CT SUR PTN")
    while ctx.voice_client.is_playing():
        await asyncio.sleep(0.5)
    await bot.voice_clients[0].disconnect()


@bot.command()
async def retard(ctx, player):
    with open(fichier, 'r') as file:
        json_data = json.load(file)
    for item in json_data:
        if item[player]:
            scoreAjout = int(item[player]) + int(10)
        item[player] = scoreAjout
    with open(fichier, 'w') as file:
        json.dump(json_data, file, indent=2)
    await ctx.send(player + " à été absent ou en retard. Score de " + player + " : " + str(item[player]))


@bot.command()
async def loltmort(ctx):
    gages = ["rename discord une semaine xXx_d4Rk-sASuk3_xXx",
             "Porter la PP ultime pendant 24h\n"
             "https://cdn.discordapp.com/attachments/163670590828314624/625775865325682688/uchiwa_sasuke_616.png",
             "devoir récolter 5k seau d'eau",
             "monter le métier paysan lvl 10",
             "Jouer l'écran inverser",
             "Devoir ne jouer qu'avec un seul élément pendant la prochaine session",
             "Pour un combat : Vous faites partie de la team adverse",
             "Pour un combat : Vous êtes immobile",
             "Pour un combat : Vous devez par tout les moyens faire les quatre coins du terrain",
             "Porter un vieux costume  choisi  à l'unanimité par les autres pendant toute la session de jeu",
             "Pour 30 minutes : Allouer un seul coeur processeur au jeu",
             "Le premier qui fail le challenge 2 4 6 8 (finir le tour en PA pair) se voit attitrer le titre nul en math dans son pseudo sur discord pendant x temps",
             "[Défi] Un joueur est le roi et doit se suicider par tout les moyens possibles : Si il meurt, les 5 autres ont un gage, s'il survit, il doit se taper un gage",
             "Utiliser le même sort pendant 5 combats et uniquement ce sort",
             "Pour un combat : Vous ne pouvez que dépenser des PA ou que des PM dans le même tour.",
             "Pour un combat : Vous ne devez utiliser que des sorts ayant un coup de PW",
             "Repartir  à astrub et revenir à sa position en marchant ( bateau de astrub à la nation accepté par obligation)",
             "Passer de la barre stasis a la barre wakfu",
             "Jouer au pad pendant 1h",
             "KARAOKE !",
             "Jouer à la tablette graphique pendant une heure",
             "[Défi] Faire tourner Wakfu pendant 1h sans avoir un seul lagspike",
             "Détruire un item de son stuff  et le remplacer par un pourri",
             "Pendant un combat : Jouer sans les interfaces",
             "Ne pas avoir le droit de foirer les challs pendant 5 combats d'affilé ( sinon double dose de gage )",
             "Ne devoir frapper les ennemies qu'en diagonal",
             "Ne devoir frapper les ennemies qu'alligné",
             "Aller au front ( pour les persos distances)  aller  en distance ( pour les persos mélée)",
             "Ne devoir taper les ennemis en étant uniquement en range du cavalier des échecs",
             "Pour un combat : Vous devez faire 'changer de personnage' pendant votre tour, et vous reconnecter.",
             "Ne pas frapper les mobs de face",
             "Ne pas avoir droit aux soins  pendant 5 combats",
             "Pour un combat : Vous devez passer votre tour dès que votre timer atteint les 10 secondes restantes.",
             "Taper le mobs comme ça :\n"
             "https://media.discordapp.net/attachments/625782166822977546/625789769443442698/Screenshot_67.png?width=149&height=145",
             "[Défi] Échecs : Chaque joueur est attribué une pièce des échecs de façon aléatoire, sa range est déterminée par celle de la pièce",
             "Devenir la poubelle de la team pendant toute la durée de la session",
             "Faire un don d'une de ses pièces d'équipement random a astrub / écaflipus",
             "[Défi] Mendier 600 kamas à Astrub pour payer le zaap d'immigration de la team (j'sais que y'a plus de prix aux zaaps, là est l'arnaque)",
             "Lancer un combat contre un bouftou solo et le perdre en se fesant manger le fion ( bouton abandonner interdit)",
             "Pour un combat : Vous devez mettre de l'eurobeat sur le bot à musique.",
             "Pour un combat : Vous devez mettre de la hardbass sur le bot à musique.",
             "Pour un combat : Vous devez mettre du disco sur le bot à musique.",
             "Pour un combat : Vous devez mettre de la musique populaire de merde sur le bot à musique, tubes de l'été recommandés.",
             "Pour un combat : Vous devez déséquiper tout votre équipement ormis main droite et secondaire",
             "Défi pour panda uniquement :  porter un ennemi et ne faire que cette action pendant  un combat complet (  interdit de le reposer )",
             "Défi pour un éliotrope uniquement : vous devez faire en sorte qu'un mob utilise vos portails ( une fois mini )",
             "Défi pour sacrieur uniquement : ne pas attaquer avant d'atteindre - de 20% des pv max",
             "Défis pour iop : Vous ne devez utiliser qu'un seul sort de chaque branche élémentaire",
             "Défi pour Xélor : Vous n'avez pas le droit de jouer votre Cadran.",
             "Défi pour Zobal : Vous n'avez pas le droit de jouer de masques",
             "Défi pour ougi : Vous n'avez pas le droit d'utiliser proie et  le chienchien pendant le combat",
             "Défi global : Pas le droit d'utiliser les mécaniques de sa classe.",
             "Pour un Combat : tous vos sorts offensifs lancés doivent être précédés par un 'DEUS VULT!' envoyé dans le tchat.",
             "Crossover : Vous n'avez le droit de taper un ennemie que si aucun ennemie ou allié n'est en ligne de votre cible.",
             "Pour un combat : Vous devez générer aléatoirement le nombre de PA et de PM que vous pouvez utiliser dans chaque tour ( deux rolls différents, zéro inclus )",
             "Vous devez crafter 400 kamas à partir de minerais de fer.",
             "Pour 5 minutes : Vous devez rester assis.",
             "Demander 100 kamas pour le Zaap (n'est validé que si vous les obtenez)",
             "KARAOKE !"
             ]
    choose = random.choice(
        gages)+" ! Have Fun with LOLTMORTGAME <:innocent:625807221250326528>"
    await ctx.send(str(choose))
