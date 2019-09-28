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

import sources

try:
    sources.bot.run(sources.TOKEN)
except KeyboardInterrupt:
    print("\n\n************************************\n\n")
