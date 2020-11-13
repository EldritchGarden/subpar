"""
Defines the basic bot commands
"""

import logging
from discord.ext import commands
import src.publix

log = logging.getLogger("cogs.base")


class Commands(commands.Cog):
    """Defines the basic commands and listeners used by the bot

    Properties:
        [commands.Bot] bot | parent bot instance
        [publix.WeeklySale] current_deal | current week's deal

    Methods:
        deal(self, ctx)
    """

    def __init__(self, bot):
        self.bot = bot  # bot context
        self.current_deal = None  # track deal

    @commands.command(help="Show the sale for this week")
    async def deal(self, ctx):
        """Fetch and display information about the current Publix Sub on sale

        Arguments:
            ctx | discord context
        """

        # TODO check ctx for store_id set in db?

        try:
            sub = src.publix.weekly_sub()
        except ValueError as e:  # catch invalid store id
            log.error(e)
            await ctx.send(e)
            return

        await ctx.send(
            "Sub: {}\nDescription: {}\n\nYou can thumbs up/down this message to rate the sub".format(
                sub.name, sub.description)
        )  # send sub message


def register(bot: commands.Bot):
    """Register the cog to the bot.

    Arguments:
        [str] bot | bot instance to register cog to.
    """

    bot.add_cog(Commands(bot))
