import datetime
from config import SCOREBOARD_CHANNEL_ID

####
# I am genuinely sorry you have to see this ugly mess
####

class Scorekeeper:
    def __init__(self, db, log):
        self.db = db
        self.log = log

    def first_bloods(self, uid, solves, challenges):
        first_blood_ctr = 0
        for chal in challenges:
            chal_solves = list(filter(lambda solve: solve[1] == chal[0], solves))
            earliest_time = datetime.datetime.now()
            first_solve = ()
            for s in chal_solves:
                if s[0] < earliest_time:
                    earliest_time = s[0]
                    first_solve = s
            if uid in first_solve:
                first_blood_ctr += 1
        return first_blood_ctr

    def calculate_decay(self, points, submission_time, release_time, num_weeks):
        print(submission_time - release_time)
        # First 24 hours: 100%
        if submission_time <= release_time + datetime.timedelta(days=(7 * (num_weeks - 1) + 1)):
            return points
        # First 48 hours: 75%
        if submission_time <= release_time + datetime.timedelta(days=(7 * (num_weeks - 1) + 2)):
            return int(0.75 * points)
        # After 48 hours: 50%
        return int(0.5 * points)

    async def scoreboard(self, guild):
        solves = self.db.sql_fetchall("SELECT submission_time,name,points,release_time,num_weeks," + ",".join(["player_" + str(i) for i in range(21)]) + " FROM solves INNER JOIN teams ON solves.team_id=teams.team_id INNER JOIN challenges ON solves.chal_id=challenges.chal_id;")
        filtered_solves = self.db.sql_fetchall("SELECT submission_time,name,points,release_time,num_weeks," + ",".join(["player_" + str(i) for i in range(21)]) + " FROM solves INNER JOIN teams ON solves.team_id=teams.team_id INNER JOIN challenges ON solves.chal_id=challenges.chal_id WHERE is_first_blood_eligible=1;")
        nicknames = self.db.sql_fetchall("SELECT * FROM users;")
        challenges = self.db.sql_fetchall("SELECT name FROM challenges;")
        scores = []
        for nickname in nicknames:
            score = 0
            uid = nickname[0]
            for solve in solves:
                to_add = 0
                if(uid in solve):
                    to_add = self.calculate_decay(solve[2], solve[0], solve[3], solve[4])
                score += to_add

            #add solo_scores
            solo_scores = self.db.sql_fetchall("select points,submission_time,release_time,num_weeks from solo_solves INNER JOIN challenges ON challenges.chal_id=solo_solves.chal_id WHERE discord_id=%s", val=(uid,))
            solo_points = 0
            if solo_scores:
                for solo_score in solo_scores:
                    solo_points += self.calculate_decay(solo_score[0], solo_score[1], solo_score[2], solo_score[3])
            print(solo_points)

            #calculate writeup scores
            writeup_scores = self.db.sql_fetchone("select SUM(approved) from writeups where user_id=%s", val=(uid,))
            if writeup_scores:
                if writeup_scores[0]:
                    writeup_scores = writeup_scores[0] * 100
                else:
                    writeup_scores = 0
            # Don't give first blood bonuses to players who have "graduated"
            is_first_blood_eligible = self.db.sql_fetchone("SELECT is_first_blood_eligible FROM members WHERE id=%s", val=(uid,))[0]
            score += int(solo_points / 2) + writeup_scores
            if is_first_blood_eligible == 1:
                score += 150 * self.first_bloods(uid, filtered_solves, challenges)
            scores.append((nickname, int(score)))
        scores.sort(key = lambda x: x[1], reverse=True)
        res = "RANK  NICKNAME" + (" " * (22 - len("NICKNAME"))) + "SCORE\n"
        scorelines = ["  ".join([str(rank+1) + (" " * (4 - len(str(rank+1)))), str(scores[rank][0][1]) + (" " * (20 - len(scores[rank][0][1]))), str(scores[rank][1])]) for rank in range(len(scores))]
        res += "\n".join(scorelines) + "\n"

        chan = guild.get_channel(SCOREBOARD_CHANNEL_ID)
        # delete old scoreboard messages
        await chan.purge(limit=4)
        msg_limit = 2000 - 10
        msg_parts = []
        idx = 0
        while idx < len(res):
            if len(res[idx:]) > msg_limit:
                last = res[:msg_limit].rindex('\n')
                msg_parts += ["```" + res[idx:last+1] + "```"]
                idx = last
            else:
                msg_parts += ["```" + res[idx:] + "```"]
                break

        await guild.get_channel(SCOREBOARD_CHANNEL_ID).send("**Live Scoreboard: http://scoreboard.ctf-league.osusec.org/**" )
        for msg_part in msg_parts:
            await guild.get_channel(SCOREBOARD_CHANNEL_ID).send(msg_part)
