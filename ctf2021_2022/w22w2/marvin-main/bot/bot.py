#!/usr/bin/python3

import discord
from discord.ext import commands
import subprocess
import os
import random
import datetime
import time

from config import BOT_TOKEN, BOT_PREFIX, DB_CONFIG

import CtfDatabase
import Logger
import GeneralCommands
import NewPlayerRegistration
import Member
import Scorekeeper

log = Logger.Logger()
db = CtfDatabase.CtfDatabase(DB_CONFIG, log)
sk = Scorekeeper.Scorekeeper(db, log)
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
bot.add_cog(GeneralCommands.GeneralCommands(bot, db, log))
bot.add_cog(NewPlayerRegistration.NewPlayerRegistration(bot, db, log))
bot.add_cog(Member.Member(bot, db, log, sk))

bot.run(BOT_TOKEN)
