"""
Source code for the sub-par discord bot.
<Describe file tree>
"""

import logging
from pathlib import Path
import time

# path globals
ROOT_PATH = Path(__file__).parent.absolute()
LOG_PATH = Path(ROOT_PATH.parent / "logs")
TOKEN_PATH = Path(ROOT_PATH / 'bot.token')
DB_PATH = Path(ROOT_PATH.parent / 'db' / 'data.db')

if not LOG_PATH.exists():
    LOG_PATH.mkdir()  # create log dir if necessary

# configure logging
log_file = time.strftime("%m%d%y-%H%M") + '.log'

# noinspection PyArgumentList
logging.basicConfig(
    level=logging.INFO,
    format="%(module)s %(levelname)s: %(message)s",
    handlers=[  # define both stream and file handlers
        logging.StreamHandler(),
        logging.FileHandler(str(Path(LOG_PATH / log_file)))
    ]
)
