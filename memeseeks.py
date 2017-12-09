"""Use the Master of All Science API."""

from random import randint
from base64 import b64encode

import requests

# endpoints of interest
ENDPOINT_MAP = {
    "mrmemeseeks": "https://masterofallscience.com",
    "frinkiac": "https://frinkiac.com",
    "morbotron": "https://morbotron.com",
}

RESPONSE_MAP = {
    "mrmemeseeks": "Caaann Do!",
    "frinkiac": "Mm-hai",
    "morbotron": "DOOOOOOOOOOMMMM",
}


def initial_response(command, response_url):
    """Respond to slack to avoid timeouts."""
    requests.post(response_url, json={"text": RESPONSE_MAP[command]})


def respond_to_slack(response_url, payload):
    """Respond with URL that unfurls."""
    requests.post(response_url, json={
        "response_type": "in_channel",
        "text": f'{payload}'
    })


def random_gen(resp_items):
    """Generate psuedo random number."""
    min = 1
    max = resp_items
    return randint(min, max)


def img_search(command, query):
    """Find image based on search string."""
    res = requests.get(f'{ENDPOINT_MAP[command]}/api/search?q={query}')
    choice = random_gen(len(res.json()))
    episode = res.json()[choice]["Episode"]
    timestamp = res.json()[choice]["Timestamp"]
    return episode, timestamp


def img_select(command, query, meme_text):
    """Select image and append meme text."""
    episode, timestamp = img_search(command, query)
    image_text = b64encode(bytes(meme_text, 'utf-8'))
    image_text = image_text.decode('utf-8')
    image = f'{ENDPOINT_MAP[command]}/meme/{episode}/{timestamp}.jpg?b64lines={image_text}'
    return image
