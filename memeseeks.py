"""Use the Master of All Science API."""

import requests

# endpoints of interest: search, caption
MOAS_API_URL = "https://masterofallscience.com/api/"


# Basic search query
def img_search():
    """Find image based on search string."""
    query_string = "tiny rick"
    res = requests.get(f'{MOAS_API_URL}search?q={query_string}')
    episode = res.json()[0]["Episode"]
    timestamp = res.json()[0]["Timestamp"]
    return episode, timestamp


def img_select():
    """Get to image caption page."""
    episode, timestamp = img_search()
    res = requests.get(f'{MOAS_API_URL}caption?e={episode}&t={timestamp}')
    print(res.json())


img_select()
