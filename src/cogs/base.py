"""
Defines bot the basic bot commands
"""

import logging
from discord.ext import commands

log = logging.getLogger("cogs.base")


class Commands(commands.Cog):
    """Defines the basic commands and listeners used by the bot

    Properties:
        [commands.Bot] bot | parent bot instance
        [publix.WeeklySale] current_deal | current week's deal

    Methods:
        TODO
    """

    @staticmethod
    def register(bot: commands.Bot):
        """Register the cog to the bot.

        Arguments:
            [str] bot | bot instance to register cog to.
        """

        bot.add_cog(Commands(bot))

    def __init__(self, bot):
        self.bot = bot  # bot context
        self.current_deal = None  # track deal

    @commands.command()
    async def deal(self, ctx):
        """Fetch """
