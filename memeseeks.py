"""Use the Master of All Science API."""

from random import randint
from base64 import b64encode

import requests

# endpoints of interest: search, caption
MOAS_API_URL = "https://masterofallscience.com/api/"
MOAS_URL = "https://masterofallscience.com/"


def initial_response(response_url):
    """Respond to slack to avoid timeouts."""
    resp = "Caaann Do!"
    requests.post(response_url, json={"text": resp})


def respond_to_slack(response_url, payload):
    """Respond with URL that unfurls."""
    requests.post(response_url, json={
        "response_type": "in_channel",
        "text": f'{payload}'
    })


# Gen random number to help select random image from search result
def random_gen(resp_items):
    """Generate psuedo random number."""
    min = 1
    max = resp_items
    return randint(min, max)


# Basic search query
def img_search(query):
    """Find image based on search string."""
    res = requests.get(f'{MOAS_API_URL}search?q={query}')
    choice = random_gen(len(res.json()))
    episode = res.json()[choice]["Episode"]
    timestamp = res.json()[choice]["Timestamp"]
    return episode, timestamp


# need to import second arg here and b64 dencode
def img_select(query, meme_text):
    """Get to image caption page."""
    episode, timestamp = img_search(query)
    image_text = b64encode(bytes(meme_text, 'utf-8'))
    image_text = image_text.decode('utf-8')
    image = f'{MOAS_URL}meme/{episode}/{timestamp}.jpg?b64lines={image_text}'
    return image
