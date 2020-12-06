"""
Interface to SQLite3 Database

Interface operations are prefixed with the operation scope:
    r for Read operations
    w for Write operations
    rw for Read/Write operations
"""

import csv
from datetime import datetime, timedelta
import src.publix
from src import SALE_PATH, SUB_PATH


def r_current_sale() -> src.publix.WeeklySale:
    """Reads the current sale from database and returns a WeeklySale object"""

    def in_range(start_date, end_date):
        today = datetime.today().date()
        start_date = datetime.strptime(start_date, "%m%d%Y").date()
        end_date = datetime.strptime(end_date, "%m%d%Y").date()

        # check that today is within date range
        # start day is same or before current day (positive timedelta)
        # end day is same or after current day (negative timedelta)
        if ((today - start_date).days >= 0) and ((today - end_date).days <= 0):
            return True
        else:
            return False

    with open(SALE_PATH, newline='') as csvfile:
        c_reader = csv.reader(csvfile, delimiter=',')
        sale = None
        for row in c_reader:
            if in_range(row[0], row[1]):
                sale = row
                break

        if not sale:
            sub = src.publix.weekly_sub()
            sale = src.publix.WeeklySale(sub)
            w_sale(sale)
        else:
            sub = src.publix.Sub(sale[2], sale[3])
            sale = src.publix.WeeklySale(sub, score=sale[4], start_date=datetime.strptime(sale[0], "%m%d%Y"))

        return sale


def r_subscribed_users(sub: str) -> list:
    """Return list of users subscribed to a specific sub"""

    with open(SUB_PATH, newline='') as csvfile:
        c_reader = csv.reader(csvfile, delimiter=',')
        user_list = []
        for row in c_reader:
            if row[0] == sub:
                user_list = row[1].split(':')
                break

        return [int(u) for u in user_list]


def w_sale(sale: src.publix.WeeklySale):
    """Write a new sale to the db"""

    with open(SALE_PATH, 'w', newline='') as csvfile:
        c_writer = csv.writer(csvfile, delimiter=',')
        c_writer.writerow(
            [sale.start.strftime("%m%d%Y"),
             sale.end.strftime("%m%d%Y"),
             sale.sub.name,
             sale.sub.description,
             sale.score]
        )


def w_subscribed_users(sub: str, users: list, overwrite=False):
    """Append users to list of subscribed users for a specific sub"""

    # combine and cast to str
    if overwrite:
        temp = users
    else:
        temp = r_subscribed_users(sub)
        temp.extend(users)

    temp = [str(u) for u in temp]

    # filter duplicates
    user_list = []
    for u in temp:
        if u not in user_list:
            user_list.append(u)

    with open(SUB_PATH, newline='') as inf:
        c_reader = csv.reader(inf.readlines(), delimiter=',')

    with open(SUB_PATH, 'w', newline='') as csvfile:
        c_writer = csv.writer(csvfile, delimiter=',')
        write_flag = False  # has the list been written

        for row in c_reader:
            if row[0] == sub:
                c_writer.writerow([row[0], ':'.join(user_list)])
                write_flag = True
            else:
                c_writer.writerow(row)

        if not write_flag:  # add a new row if one didnt exist for sub
            c_writer.writerow([sub, ':'.join(user_list)])


def w_update_score(sale: src.publix.WeeklySale):
    with open(SALE_PATH, newline='') as inf:
        c_reader = csv.reader(inf.readlines(), delimiter=',')

    with open(SALE_PATH, 'w', newline='') as csvfile:
        c_writer = csv.writer(csvfile, delimiter=',')
        start = sale.start.strftime("%m%d%Y")
        write_flag = False

        for row in c_reader:
            if row[0] == start:
                c_writer.writerow([row[0], row[1], row[2], row[3], sale.score])
                write_flag = True
            else:
                c_writer.writerow(row)

        if not write_flag:
            w_sale(sale)  # write new sale if not found in db
