from discord.ext import commands
import discord
from config import ROLES, ANNOUNCEMENTS_CHANNEL_ID, GUILD_ID, TIME_OFFSET_FROM_UTC
import datetime
import time
from tabulate import tabulate

class Member(commands.Cog):
    def __init__(self, bot, db, log, sk):
        self.bot = bot
        self.db = db
        self.log = log
        self.sk = sk

    async def is_verified(self, ctx):
        verified_res = self.db.sql_fetchone("SELECT verified FROM members WHERE id=%s", val=(ctx.author.id,))
        if not verified_res or verified_res[0] != 1:
            await ctx.send('You must be verified to use this command.')
            return False
        return True

    @commands.command(name='info', help='gets info for a specified challenge')
    async def info(self, ctx, name):
        # check that user is verified
        if not await self.is_verified(ctx):
            return

        chal_details = self.db.sql_fetchone("SELECT name,category,points,download,access,description FROM challenges WHERE name='%s'" % name)
        if(not chal_details):
            await ctx.send("chal not found")
            return
        labels = ["NAME", "CATEGORY", "POINTS", "DOWNLOAD LINK", "ACCESS", "DESCRIPTION"]
        await ctx.send("\n".join([labels[i] + ": " + str(chal_details[i]) for i in range(len(labels))]))

    @commands.command(name='challenges', help='retrieves a list of challenges')
    async def challenges(self, ctx):
        # check that user is verified
        if not await self.is_verified(ctx):
            return

        chal_details = [['NAME', 'CATEGORY', 'POINTS']]
        for chal in self.db.sql_fetchall("SELECT name,category,points,release_time FROM challenges"):
            chal = list(chal)
            if chal[3] != None:
                chal[3] = chal[3].date()
                chal_details.append(chal[:-1])

        await ctx.send('```\n' + tabulate(chal_details, tablefmt='grid') + '\n```')

    @commands.command(name='writeup', help='submits a writeup to the coach approval queue')
    async def writeup(self, ctx, *args):
        # check that user is verified
        if not await self.is_verified(ctx):
            return

        name = args[0]
        writeup = " ".join(args[1:])
        chal_id = self.db.sql_fetchone("SELECT chal_id FROM challenges WHERE name='%s'" % name)
        if(not chal_id):
            await ctx.send('no such challenge')
            return
        self.db.sql_commit("INSERT INTO writeups (chal_id, user_id, text) VALUES (%s,%s,%s)", val=(chal_id[0], ctx.author.id, writeup))
        await ctx.send('writeup submitted')

    @commands.command(name='submit', help='submits a flag')
    async def submit(self, ctx, submitted_flag):
        # check that user is verified
        if not await self.is_verified(ctx):
            return

        # Check if it's too late to submit the flag
        res = self.db.sql_fetchone("SELECT release_time, num_weeks FROM challenges WHERE flag='%s'" % submitted_flag)
        if res:
            release_time = res[0]
            num_weeks = res[1]
            # submissions are open right up until the start of the next week's meeting
            if datetime.datetime.now() > ((release_time + datetime.timedelta(hours=TIME_OFFSET_FROM_UTC)).replace(hour=18,minute=0,second=0,microsecond=0) + datetime.timedelta(days=(7 * num_weeks), hours=-1*TIME_OFFSET_FROM_UTC)):
                await ctx.send("correct!\nunfortunately, that flag is for a challenge that is more than %d weeks old, so you won't receive points for it." % num_weeks)
                return
        else:
            await ctx.send("wrong flag")
            return

        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

        if(ctx.channel.type == discord.ChannelType.private):
            self.db.sql_commit("INSERT INTO users (discord_id, nickname) VALUES (%s, %s) ON DUPLICATE KEY UPDATE nickname=%s", val=(ctx.author.id, ctx.author.name.encode('unicode-escape').decode()[:19], ctx.author.name.encode('unicode-escape').decode()[:19]))

            chal_id = self.db.sql_fetchone("SELECT chal_id FROM challenges WHERE flag='%s'" % submitted_flag)
            if(chal_id): chal_id = chal_id[0]
            # Query all player_x columns to find the team the user is on for this challenge
            sql = "SELECT team_id FROM teams WHERE (" + " OR ".join(["player_" + str(i) + "=%s"  for i in range(10)]) + ") "
            sql += "AND (" + " OR ".join(["chal_id" + str(i) + "=%s" for i in range(3)]) + ")"
            team_id = self.db.sql_fetchone(sql, val=tuple([ctx.author.id for i in range(10)] + [chal_id for i in range(3)]))
            if(team_id):
                await ctx.send("you are already on team " + str(team_id[0]) +" which has been assigned this chal. you may not submit it solo")
                return
            solved = self.db.sql_fetchone("SELECT solve_id FROM solo_solves WHERE discord_id=%s AND chal_id=%s", val=(ctx.author.id, chal_id))
            if(solved):
                await ctx.send("you have already submitted this flag")
                return

            self.db.sql_commit("INSERT INTO solo_solves (discord_id, chal_id, submission_time) VALUES (%s,%s,%s)", val=(ctx.author.id, chal_id, timestamp))
            await ctx.send('correct!')
            guild = list(filter(lambda g: g.id == GUILD_ID, self.bot.guilds))[0]
            await self.sk.scoreboard(guild)
            return

        team_id = self.db.sql_fetchone("SELECT team_id FROM teams WHERE text_channel=%s", val=(ctx.channel.id,))[0]
        chals = self.db.sql_fetchone("SELECT chal_id0,chal_id1,chal_id2 FROM teams WHERE team_id=%s", val=(team_id,))
        chal_id = self.db.sql_fetchone("SELECT chal_id,name FROM challenges WHERE flag='%s'" % submitted_flag)
        if(chal_id and (chal_id[0] in chals)):
            name = chal_id[1]
            chal_id = chal_id[0]
            is_first_blood_eligible = self.db.sql_fetchone("SELECT is_first_blood_eligible FROM members WHERE id=%s", val=(ctx.author.id,))[0]
            # Check if the challenge has already been solved.
            # If so, check if user is not a graduate, update is_first_blood_eligible if not
            solve = self.db.sql_fetchone("SELECT is_first_blood_eligible FROM solves WHERE chal_id=%s AND team_id=%s", val=(chal_id, team_id))
            if solve:
                if solve[0] == 0 and is_first_blood_eligible == 1:
                    self.db.sql_commit("UPDATE solves SET is_first_blood_eligible=1, submission_time=%s WHERE chal_id=%s AND team_id=%s;", val=(timestamp, chal_id, team_id))
                else:
                    await ctx.send('already submitted!')
                    return
            else:
                self.db.sql_commit("INSERT INTO solves (team_id, chal_id, submission_time, is_first_blood_eligible) VALUES (%s,%s,%s,%s)", val=(team_id, chal_id, timestamp, is_first_blood_eligible))
            # update scoreboard
            guild = list(filter(lambda g: g.id == GUILD_ID, self.bot.guilds))[0]
            await self.sk.scoreboard(guild)
            if(len(self.db.sql_fetchall("SELECT is_first_blood_eligible FROM solves WHERE chal_id=%s AND is_first_blood_eligible=1", val=(chal_id,))) == 1):
                await ctx.guild.get_channel(ANNOUNCEMENTS_CHANNEL_ID).send("first blood on " + name + " goes to team " + str(team_id) + "!")
                await ctx.send('first blood!')
                return
            await ctx.send('correct!')
        else:
            await ctx.send('not the flag')

    @commands.command(name='solves', help="gets a lists of challenges you've solved")
    async def solves(self, ctx):
        # check that user is verified
        if not await self.is_verified(ctx):
            return
        solves = self.db.sql_fetchall("SELECT name FROM solves INNER JOIN teams ON solves.team_id=teams.team_id INNER JOIN challenges ON solves.chal_id=challenges.chal_id WHERE %s IN (" + ",".join(["player_" + str(i) for i in range(10)]) + ")", val=(ctx.author.id,))
        solo_solves = self.db.sql_fetchall("SELECT name from solo_solves INNER JOIN challenges ON challenges.chal_id=solo_solves.chal_id WHERE discord_id=%s", val=(ctx.author.id,))
        solves = [item[0] for item in solves if item[0]]
        print(solves)
        solo_solves = [item[0] for item in solo_solves if item[0]]
        print(solo_solves)
        msg = "\n".join(solves + solo_solves)
        if msg == "":
            await ctx.send('no solves yet!')
        else:
            await ctx.send(msg)
