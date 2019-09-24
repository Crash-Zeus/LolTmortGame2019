"""
Work on python 3.6
"""
# -*- coding: utf-8 -*-
import discord
import sys
import json
import os
import random
import asyncio
from discord.ext import commands


client = discord.Client()
TOKEN = ""
bot = commands.Bot(command_prefix='²')

os.system('setterm -cursor off')

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(name='voler des bot')
        )
    print('Bot {0.user} online'.format(bot))
    print('<-------------->')


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Voldebot", description="Wallah t'es mort frère <:innocent:625807221250326528>",
        color=0xeee657, inline=False
        )
    embed.add_field(name="Commandes", value="²score, ²mort [pseudo], ²info", inline=False)
    embed.add_field(name="Pseudo des joueur reconnue par le bot", value="crash, fred, tsuna, easy, iruhn, shiyu", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def score(ctx):
    with open("score.json", "r") as json_data:
        data_dict = json.load(json_data)
    score = str(data_dict).replace("[", " ").replace("]", " ").replace("{", " ").replace("}", " ").replace("'", " ").replace(",", "\n")
    score = discord.Embed(
        title="Score des morts", description=score,
        color=0xFF0000
    )
    await ctx.send(embed=score)

@bot.command()
async def mort(ctx, player):
     fichier = 'score.json'
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
             "Taper le mobs comme ça : \n"
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
             "Défi global : Pas le droit d'utiliser les mécaniques de sa classe.",
             "Pour un Combat : tous vos sorts offensifs lancés doivent être précédés par un 'DEUS VULT!' envoyé dans le tchat.",
             "Crossover : Vous n'avez le droit de taper un ennemie que si aucun ennemie ou allié n'est en ligne de votre cible.",
             "Pour un combat : Vous devez générer aléatoirement le nombre de PA et de PM que vous pouvez utiliser dans chaque tour ( deux rolls différents, zéro inclus )",
             "Vous devez crafter 400 kamas à partir de minerais de fer.",
             "Pour 5 minutes : Vous devez rester assis.",
             "Demander 100 kamas pour le Zaap (n'est validé que si vous les obtenez)",
             "KARAOKE !"
             ]
    choose = random.choice(gages)+" ! Have Fun with LOLTMORTGAME <:innocent:625807221250326528>"
    await ctx.send(str(choose))

try:
    bot.run(TOKEN)
except KeyboardInterrupt:
        print("\n\n************************************\n\n")
