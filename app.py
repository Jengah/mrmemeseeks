"""Serve meme-generating Slack slash commands with Flask."""

from flask import Flask, request
import memeseeks

app = Flask(__name__)


@app.route("/mrmemeseeks", methods=['POST'])
def mrmemeseeks():
    """Execute the mrmemeseek slack command."""
    response_url = request.form.get('response_url')
    command = request.form.get('command')[1:]
    text = request.form.get('text')
    query, meme_text = memeseeks.check_args(text, response_url)
    if query is None:
        return ''
    memeseeks.ephemeral_response(command, response_url)
    payload = memeseeks.img_select(command, query, meme_text, response_url)
    if payload is None:
        return ''
    memeseeks.respond_to_slack(response_url, payload)
    return ''


@app.route("/frinkiac", methods=['POST'])
def frinkiac():
    """Execute the frinkiac slack command."""
    response_url = request.form.get('response_url')
    command = request.form.get('command')[1:]
    text = request.form.get('text')
    query, meme_text = memeseeks.check_args(text, response_url)
    if query is None:
        return ''
    memeseeks.ephemeral_response(command, response_url)
    payload = memeseeks.img_select(command, query, meme_text, response_url)
    if payload is None:
        return ''
    memeseeks.respond_to_slack(response_url, payload)
    return ''


@app.route("/morbotron", methods=['POST'])
def morbotron():
    """Execute the morbotron slack command."""
    response_url = request.form.get('response_url')
    command = request.form.get('command')[1:]
    text = request.form.get('text')
    query, meme_text = memeseeks.check_args(text, response_url)
    if query is None:
        return ''
    memeseeks.ephemeral_response(command, response_url)
    payload = memeseeks.img_select(command, query, meme_text, response_url)
    if payload is None:
        return ''
    memeseeks.respond_to_slack(response_url, payload)
    return ''


# only needed for local dev
if __name__ == "__main__":
    app.run()
