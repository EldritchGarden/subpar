"""
Define bot and add cogs. This module should be treated as main when running.
"""

import logging
from discord import Intents
from discord.ext import commands
from src import TOKEN_PATH
from src.cogs import base, scheduler, test_com

log = logging.getLogger("bot")


def start_bot():
    """Start the bot"""

    # create intent with everything EXCEPT presences intent
    intent = Intents.all()
    intent.presences = False

    prefix = '?'  # TODO make configurable
    bot = commands.Bot(prefix, intents=intent)

    # setup cogs
    base.register(bot)
    scheduler.register(bot)
    test_com.register(bot)

    # Read Token
    with open(TOKEN_PATH, 'r') as tk_file:
        token = tk_file.read()

    # start bot
    bot.run(token)
