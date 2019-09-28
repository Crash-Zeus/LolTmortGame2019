"""
Work on python 3.6
"""
import asyncio
import json
import os
import random
import sys

# -*- coding: utf-8 -*-
import discord
import youtube_dl
from discord.ext import commands
from discord.voice_client import VoiceClient

from src.cmd import *
from src.music import YTDLSource

try:
    bot.run(TOKEN)
except KeyboardInterrupt:
    print("\n\n************************************\n\n")
