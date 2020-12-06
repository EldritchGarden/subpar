"""
Defines the basic bot commands
"""

import logging
from discord.ext import commands
import src.publix
import src.database

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

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """Track sub ratings

        Triggers when a user reacts to a message from the bot triggered by ?deals

        Arguments:
            reaction | discord.reaction passed automatically
            user     | discord.user passed automatically
        """
        msg = reaction.message
        if msg.author.id == 776888684845727804:  # ensure message author was self
            if reaction.emoji == '👍':  # if thumbs up
                val = 1
            elif reaction.emoji == '👎':  # thumbs down
                val = -1
            else:
                return

            # update score in db
            sale = src.database.r_current_sale()
            sale.score = int(sale.score) + val
            src.database.w_update_score(sale)

    @commands.command(help="Show the sale for this week")
    async def deal(self, ctx):
        """Fetch and display information about the current Publix Sub on sale

        Arguments:
            ctx | discord.context passed automatically
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
