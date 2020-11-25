"""
Interface to SQLite3 Database

Interface operations are prefixed with the operation scope:
    r for Read operations
    w for Write operations
    rw for Read/Write operations
"""

import sqlite3
import src.publix
from src import DB_PATH


def r_current_sale() -> src.publix.WeeklySale:
    """Reads the current sale from database and returns a WeeklySale object"""

    con = sqlite3.connect(DB_PATH)  # db connection
    cur = con.cursor()  # create cursor

    ## Execute SQL commands ##
    # cur.execute("""SQL QUERY""")

    # create WeeklySale object from data

    con.close()  # close connection

    # return WeeklySale object


def r_subscribed_users(sub: str) -> list:
    """Return list of users subscribed to a specific sub"""

    # RETURN EMPTY LIST TODO REMOVE THIS
    return []

    con = sqlite3.connect(DB_PATH)  # db connection
    cur = con.cursor()  # create cursor

    ## Execute SQL commands ##
    # cur.execute("""SQL QUERY""")

    # validate sub entry exists
    # get list of users

    con.close()  # close connection

    # return list of user id's (ID'S SHOULD BE INT)


def w_current_sale(sale: src.publix.WeeklySale):
    """Overwrite current sale in db with provided WeeklySale object"""

    con = sqlite3.connect(DB_PATH)  # db connection
    cur = con.cursor()  # create cursor

    # convert WeeklySale object into SQL query

    ## Execute SQL commands ##
    # cur.execute("""SQL QUERY""")

    con.commit()  # commit changes
    con.close()  # close connection


def w_subscribed_users(sub: str, users: list):
    """Append users to list of subscribed users for a specific sub"""

    con = sqlite3.connect(DB_PATH)  # db connection
    cur = con.cursor()  # create cursor

    ## Execute SQL commands ##
    # cur.execute("""SQL QUERY""")

    # validate currently subscribed users
    # read currently subscribed users
    # append 'users' to currently subscribed
    # write new list

    con.commit()  # commit changes
    con.close()  # close connection


def rw_new_current_sale(sale: src.publix.WeeklySale):
    """Updates the current sale with a new object"""

    con = sqlite3.connect(DB_PATH)  # db connection
    cur = con.cursor()  # create cursor

    ## Execute SQL commands ##
    # cur.execute("""SQL QUERY""")

    # update old sale to current=False
    # create new entry for sale with current=True

    con.commit()  # commit changes
    con.close()  # close connection
