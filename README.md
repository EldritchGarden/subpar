# Sub-Par
A discord bot for you stomach. Sub-Par lets you know the current Publix Deli Sub
Sandwich sale for the week. You can get info on the sub, and even get notifications
when a sub you like goes on sale.

## Introduction
Sub-Par is a discord bot and therefore runs on discord. No need to run the code to
use it (unless you want to), you can simply add it to your discord server
[here](https://discord.com/api/oauth2/authorize?client_id=776888684845727804&permissions=10304&scope=bot).

Sub-Par currently provides the following features:
* Show sale info
* Subscribe to notifications when a sub goes on sale
* Rate a sub with a reaction

## Usage
The bot uses the command prefix `?` to run commands:
* `?help`
  * Show the bot help message
* `?deal`
  * Show the current sub on sale and its description.
  * React to the message with a thumbs up/down to rate the sub
* `?subscribe`
  * Get notifications (in your DMs) when a sub goes on sale
* `?unsubscribe`
  * Like `?subscribe` but... 'un'

## The Package
All the important code is in `src/` and can (should) be run using `main.py` in the root.
The `src/` directory contains the python files, as well as a sub-folder `cogs/` and the bot's token.
The token should be in a file named `bot.token` and is used to authenticate the bot with Discord.
The `cogs/` directory contains the definitions for the commands and listeners to register to the bot,
and are organized logically by scope.

### Installation
Dependencies are listed in the `requirements.txt` file, and local copies of each dependency
have been downloaded to `lib/`. There are two methods for installation:

1. `pip install -r requirements.txt`
2. `pip install -r requirements.txt --no-index --find-links file://lib/`

Method 1 is a simple online install downloading the requirements, whereas method
2 uses the local copies of the required packages. 

NOTE: `requirements.txt` and `lib/` should be the paths to requirements.txt
and lib/.

### Data Storage
The 'database' is stored in `db/` and stores all data that needs to be saved. This is
the most important for backups.
