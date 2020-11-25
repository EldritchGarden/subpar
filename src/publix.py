"""
Interface for getting data from the Publix weekly ad.
"""

from html.parser import HTMLParser
import re
import logging
import requests
from dataclasses import dataclass
from datetime import date, timedelta

log = logging.getLogger('publix')

AD_URL = """https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?ListingSort=8&StoreID={}&CategoryID=5232526"""


class PageParser(HTMLParser):
    """Parse HTML tags

    Implements the HTMLParser class to parse out the Publix weekly ad Sub and its description.
    Override handler methods for functionality.
    """

    r = re.compile('^Publix Deli .*? Sub', re.IGNORECASE)
    sFlag = False  # trigger flag when sub is found
    dFlag = False  # trigger flag when description is found
    cFlag = False  # trigger when feed should close
    sub_name = None
    sub_desc = None

    def handle_starttag(self, tag, attrs):
        if not self.cFlag and self.sFlag:
            for a in attrs:  # search for div class="description"
                if a[1] == 'description':
                    self.dFlag = True

    def handle_endtag(self, tag):
        if self.sFlag and self.dFlag:
            self.cFlag = True

    def handle_data(self, data):
        if not self.cFlag and self.dFlag:
            self.sub_desc = data
        elif not self.cFlag and self.r.match(data):
            self.sub_name = data
            self.sFlag = True


@dataclass
class Sub:
    """Represents a Publix Deli Sub Sandwich"""

    name: str  # name of the sub
    description: str  # description of the sub


class WeeklySale:
    """Represent a weekly Publix Sale

    Initialization:
        [Sub] sub | sub object representing sub for this week
        [int] score=0 | popularity score starts at 0
        [datetime] start_date=None | optionally define sale start date (datetime)
    """

    def __init__(self, sub: Sub, score=0, start_date=None):
        # date range
        if not start_date:
            today = date.today()

            start_delta = (today.weekday() - 3) % 7  # delta last thursday
            start_date = today - timedelta(days=start_delta)

            end_delta = (today.weekday() - 2) % 7  # delta next wednesday
            end_date = today + timedelta(days=end_delta)
        else:
            end_date = start_date + timedelta(days=6)

        # formatted date range as str
        self.week = "{} - {}".format(start_date.strftime("%m/%d/%y"), end_date.strftime("%m/%d/%y"))

        self.sub = sub

        self.score = score  # TODO who handles score?


def weekly_sub(store_id='2500492') -> Sub:
    """Fetch the current sale on subs from the Publix Deli Weekly Ad.

    Arguments:
        [str] store_id='2500492' | Publix store ID. Default Plantation Square.

    Returns:
        [Sub] | Sub dataclass object
    """

    url = AD_URL.format(store_id)  # insert store id
    page = requests.get(url)  # get html source for url

    error_msg = "There was an error processing your request. Please try again later."
    if error_msg in page.text:
        raise ValueError("Invalid Store Id %s" % store_id)  # handle invalid store ids

    parser = PageParser()
    parser.feed(page.text)  # parse html

    if not parser.sub_name or not parser.sub_desc:  # check that parser found the sub
        sub = "N/A"
        desc = "N/A"
    else:
        sub = parser.sub_name
        desc = parser.sub_desc.strip()

    return Sub(name=sub, description=desc)
