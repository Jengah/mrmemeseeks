"""Use Master of All Science, Frinkiac, and Morbotron APIs for great profit."""

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
    "mrmemeseeks-error": "Nothing found. Your existence is a lie",
    "frinkiac-error": "Nothing found. Try again, for glayvin out loud!",
    "morbotron-error": "Nothing found. Try again puny human!",
    "arg-error": ("This command requires a search string as an argument"
                  "and takes a max of 2 arguments. See usage instructions.")
}


def check_args(slack_args, response_url):
    """Check the arguments passed to slack command are valid."""
    args = slack_args.split(";")
    if args[0] == "" or len(args) > 2:
        ephemeral_response("arg-error", response_url)
        query = meme_text = None
        return query, meme_text
    # If a single argument is sent, just send the image (by passing empty string for meme_text)
    elif len(args) == 1:
        query = args[0]
        meme_text = ""
        return query, meme_text
    else:
        query = args[0]
        if args[1][0] == ' ':
            meme_text = args[1][1:]
        else:
            meme_text = args[1]
        return query, meme_text


def ephemeral_response(command, response_url):
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
    min = 0
    max = resp_items - 1
    return randint(min, max)


def img_search(command, query, response_url):
    """Find image based on search string."""
    res = requests.get(f'{ENDPOINT_MAP[command]}/api/search?q={query}')
    # search strings can return no results. handle that
    if len(res.json()) == 0:
        command = command + "-error"
        ephemeral_response(command, response_url)
        episode = timestamp = None
        return episode, timestamp
    else:
        choice = random_gen(len(res.json()))
        episode = res.json()[choice]["Episode"]
        timestamp = res.json()[choice]["Timestamp"]
    return episode, timestamp


def img_select(command, query, meme_text, response_url):
    """Select image and append meme text."""
    episode, timestamp = img_search(command, query, response_url)
    if episode is None:
        return None
    else:
        image_text = b64encode(bytes(meme_text, 'utf-8'))
        image_text = image_text.decode('utf-8')
        image = f'{ENDPOINT_MAP[command]}/meme/{episode}/{timestamp}.jpg?b64lines={image_text}'
        return image
