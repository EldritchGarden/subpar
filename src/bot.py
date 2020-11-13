"""
Define bot and add cogs. This module should be treated as main when running.
"""

import logging
from discord.ext import commands
from src import TOKEN_PATH
from src.cogs import base

log = logging.getLogger("bot")


def start_bot():
    """Start the bot"""

    prefix = '?'  # TODO make configurable
    bot = commands.Bot(prefix)

    # setup cogs
    base.register(bot)

    # Read Token
    with open(TOKEN_PATH, 'r') as tk_file:
        token = tk_file.read()

    # start bot
    bot.run(token)
