"""
Handles scheduled actions and messages
"""

import logging
import aiocron
from discord import Member
from discord.ext import commands
from src import database, publix

log = logging.getLogger("cogs.scheduler")


class Cron(commands.Cog):
    """Scheduled notifications and subscription commands

    Commands:
        force_notify    : manually trigger the notify method
        subscribe       : subscribe user to current sale
        unsubscribe     : unsubscribe user from current sale

    Methods:
        notify  : send dm to subscribed users about sale
        _dm     : send message to user over dm
    """

    def __init__(self, bot):
        self.bot = bot
        cron = aiocron.crontab('0 6 * * 4', func=self.notify)

    async def notify(self):
        """Notifications for weekly sale

        Because the bot's cache seems to be unavailable when run as a aiocron job,
        it's set up as a listener where the scheduled job triggers the event by sending '?notify'

        By doing this we can also easily have a record of the method being triggered.
        """

        await self.bot.wait_until_ready()  # wait for bot to build internal cache

        # get subscriber list for current sub
        sub = publix.weekly_sub()
        message = f"Good news! A sub you like is on sale!\n{sub.name}\n{sub.description}"

        sub_users = database.r_subscribed_users(sub.name)

        # NOTE: using get_user() doesn't always find cached users, so this is a more reliable
        # but slower method
        # maybe also try fetch_user()?
        for user in self.bot.get_all_members():
            if user.id in sub_users:
                await self._dm(user, message)

    @staticmethod
    async def _dm(user: Member, msg: str):
        """Send direct message to user

        Args:
            user : the discord user
            msg  : message to be sent
        """

        if not isinstance(user, Member):  # catch invalid input
            log.error("%s is not type discord.User" % type(user))
        else:
            channel = await user.create_dm()  # create dm channel
            await channel.send(msg)  # send msg

    @commands.command(hidden=True)
    async def force_notify(self, ctx):
        """Manually trigger the notify method"""

        await self.notify()

    @commands.command(help="Subscribe to notifications for future sales of this week's sub")
    async def subscribe(self, ctx):  # TODO some sort of menu for subscribing to any sub
        """Subscribe user to current sale"""

        # add user id to subscriber db
        database.w_subscribed_users(publix.weekly_sub().name, ctx.author.id)

    @commands.command(help="Unsubscribe from notifications for future sales of this week's sub")
    async def unsubscribe(self, ctx):
        """Unsubscribe user from current sale"""

        sub = publix.weekly_sub()
        user_list = database.r_subscribed_users(sub.name)

        user_list.remove(ctx.author.id)  # remove id from list
        database.w_subscribed_users(sub.name, user_list)  # write new user list


def register(bot: commands.Bot):
    """Register the cog to the bot.

    Arguments:
        [str] bot | bot instance to register cog to.
    """

    bot.add_cog(Cron(bot))
