"""
Work on python 3.6
"""
# -*- coding: utf-8 -*-
import discord, sys, json, os, random, asyncio, youtube_dl

from discord.ext import commands
from discord.voice_client import VoiceClient
from src.music import YTDLSource
from src.cmd import *

try:
    bot.run(TOKEN)
except KeyboardInterrupt:
        print("\n\n************************************\n\n")
