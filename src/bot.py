"""
Define bot and add cogs. This module should be treated as main when running.
"""

from discord.ext import commands

prefix = '?'  # TODO make configurable
bot = commands.Bot(prefix)

# setup cogs
# each cog should have setup function
#

# start bot
bot.run('token')  # TODO add token