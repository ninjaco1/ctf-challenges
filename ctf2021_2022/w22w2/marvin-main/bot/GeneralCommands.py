from discord.ext import commands
import discord
import traceback

class GeneralCommands(commands.Cog):
    def __init__(self, bot, db, log):
        self.bot = bot
        self.db = db
        self.log = log

    @commands.Cog.listener()
    async def on_ready(self):
        guilds = '\n'.join([guild.name for guild in self.bot.guilds])
        self.log.log(f"{self.bot.user} has connected to the following guilds:\n" + guilds)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

