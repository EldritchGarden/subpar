"""
Handles scheduled actions and messages
"""

import asyncio
from discord import DMChannel
from discord.ext import commands
import aiocron


class Cron(commands.Cog):
    """Scheduled notifications"""

    def __init__(self, bot):
        self.bot = bot

    @aiocron.crontab('0 4 * * 4', start=False)  # every thursday at 4am
    async def notify(self):
        """Scheduled notifications for weekly sale"""

        # get subscriber list for current sub
        # foreach send direct message

    async def _dm(self, user_id: str, msg: str):
        """Send direct message to user

        Args:
            user_id : the discord id of the user
            msg     : message to be sent
        """

        user = self.bot.get_user(user_id)  # get user object
        channel = user.create_dm()  # create dm channel

        await channel.send(content=msg)  # send msg


def register(bot: commands.Bot):
    """Register the cog to the bot.

    Arguments:
        [str] bot | bot instance to register cog to.
    """

    bot.add_cog(Cron(bot))
