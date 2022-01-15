from email.message import EmailMessage
import smtplib
import textwrap

import config
from config import EMAIL_SERVER, EMAIL_USERNAME, EMAIL_PASSWORD, VALID_EMAIL_DOMAINS

from discord.ext import commands
import discord

class NewPlayerRegistration(commands.Cog):
    def __init__(self, bot, db, log):
        self.bot = bot
        self.db = db
        self.log = log

    def is_valid_email(self, address):
        try:
            return (
                len(address.split("@")) == 2
                and address.split("@")[1] in VALID_EMAIL_DOMAINS
                and "," not in address
            )
        except:
            return False


    def send_confirmation(self, address, token):
        body = f"""
Welcome to the OSUSEC CTF League! In order to verify your membership, please send the following command in a private message to the OSUSEC bot that messaged you:

$verify {token}

Message a coach if you have any questions. Thanks, and welcome!
        """  # noqa: E501

        msg = EmailMessage()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = address
        msg["Subject"] = "OSUSEC CTF League Discord Email Confirmation"

        msg.set_content(textwrap.dedent(body))

        with smtplib.SMTP_SSL(EMAIL_SERVER, 465) as server:
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

    @commands.command(name='register', help='Sends a registration email')
    @commands.check(lambda ctx: isinstance(ctx.channel, discord.channel.DMChannel))
    async def register(self, ctx, email):
        # Patching this out for this challenge because y'all are already verified anyway

#        # check if we got a valid @osu email
#        if self.is_valid_email(email):
#            # email is valid
#            # check if its from a verified user
#            if self.db.is_user_verified(ctx.author.id):
#                # email is from verified user
#                # check if email is the same, if yes, re-add member
#                if self.db.get_email(ctx.author.id) == email:
#                    # email checks out
#                    await ctx.channel.send("This account is already verified, re-adding Member role")
#
#                    guild = list(filter(lambda g: g.id == config.GUILD_ID, self.bot.guilds))[0]
#                    member = guild.get_member(ctx.author.id)
#                    await member.add_roles(
#                        discord.utils.get(guild.roles, id=config.ROLES["verified"])
#                    )
#                else:
#                    # wrong email
#                    await ctx.channel.send("This account was verified with a different email address. Please provide the original email.")
#            else:
#                # new user, add to DB and send token
#                self.db.new_member(ctx.author.id, f"{ctx.author.name}#{ctx.author.discriminator}".encode('unicode-escape').decode())
#                self.db.set_email(ctx.author.id, email)
#                self.send_confirmation(email, self.db.get_token(ctx.author.id))
#
#                await ctx.channel.send(f"Emailed a confirmation token to {email}. Please reply with `$verify <token>` to get verified!")
#        else:
#            await ctx.channel.send("Invalid email.\nMake sure to provide your OSU email address (`@oregonstate.edu`).")

        # email is valid
        # check if its from a verified user
        if self.db.is_user_verified(ctx.author.id):
            # email is from verified user
            await ctx.channel.send("This account is already verified, re-adding Member role")

            guild = list(filter(lambda g: g.id == config.GUILD_ID, self.bot.guilds))[0]
            member = guild.get_member(ctx.author.id)
            await member.add_roles(
                discord.utils.get(guild.roles, id=config.ROLES["verified"])
            )
        else:
            # new user, add to DB and send token
            self.db.new_member(ctx.author.id, f"{ctx.author.name}#{ctx.author.discriminator}".encode('unicode-escape').decode())
            self.db.set_email(ctx.author.id, 'patched')

            await ctx.channel.send(f"Thanks for registering! Please reply with `$verify me` to get verified!")

    @commands.command(name='verify', help='Verifies your verification token')
    @commands.check(lambda ctx: isinstance(ctx.channel, discord.channel.DMChannel))
    async def verify(self, ctx, token):
        if self.db.verify_member(ctx.author.id, token) == 1:
            # this person had that message as their token, they are now verified
            guild = list(filter(lambda g: g.id == config.GUILD_ID, self.bot.guilds))[0]
            member = guild.get_member(ctx.author.id)
            await member.add_roles(
                discord.utils.get(guild.roles, id=config.ROLES["verified"])
            )

            await ctx.channel.send(f"Verification successful!\nThank you for verifying. I've updated your roles, and you should have access to all of the channels now.")

        # message wasn't a valid token
        else:
            await ctx.channel.send("Invalid token.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.log.log(f"New member joined: {member.name}#{member.discriminator}")
        # if user is already verified, give them the role
        if self.db.is_user_verified(member.id):
            guild = list(filter(lambda g: g.id == config.GUILD_ID, self.bot.guilds))[0]
            await member.add_roles(
                discord.utils.get(guild.roles, id=config.ROLES["verified"])
            )
        else:
            await member.send(
                "Welcome to the OSUSEC CTF League Discord Server!\n"
                "In order to gain full server access, you'll need to verify your email.\n"
                "Reply with `$register me` and I'll register you."
            )
