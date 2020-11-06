"""
Interface for getting data from the Publix weekly ad.

Methods:
    [str] weekly_sub(store_id='2500584')
"""

import re
import logging
import requests

log = logging.getLogger('publix')

AD_URL = """https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/\
?ListingSort=8&StoreID={}&CategoryID=5232526"""


def weekly_sub(store_id='2500584'):
    """Fetch the current sale on subs from the Publix Deli ad.

    Arguments:
        [str] store_id (default='2500584') | Publix store ID. Not the same as store number.

    Returns:
        [str] | name of sub on sale
    """

    url = AD_URL.format(store_id)
    html = requests.get(url)  # get html source for url

    sub_search = re.compile('Publix Deli .*? Sub', re.IGNORECASE)  # Case insensitive regex search; non-greedy

    match = sub_search.search(html.text)  # try to find match

    # TODO: re.search will return None if no match was found, this case must be handled
    if not match.group():
        log.error("Could not find match in weekly ad")

    return match.group()
