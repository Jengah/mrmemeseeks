"""Use the Master of All Science API."""

import requests

# endpoints of interest: search, caption
MOAS_API_URL = "https://masterofallscience.com/api/"
MOAS_URL = "https://masterofallscience.com/"


def initial_response(response_url):
    """Respond to slack to avoid timeouts."""
    resp = "Caaann Do!"
    requests.post(response_url, json={'text': resp})


def respond_to_slack(response_url, payload):
    """Respond with URL that unfurls."""
    requests.post(response_url, json={
        "response_type": "in_channel",
        "text": f'{payload}'
    })


# Basic search query
def img_search():
    """Find image based on search string."""
    query_string = "tiny rick"
    res = requests.get(f'{MOAS_API_URL}search?q={query_string}')
    episode = res.json()[2]["Episode"]
    timestamp = res.json()[2]["Timestamp"]
    return episode, timestamp


def img_select():
    """Get to image caption page."""
    episode, timestamp = img_search()
    image = f'{MOAS_URL}img/{episode}/{timestamp}.jpg'
    return image
