"""Use Flask & ngrok to test command."""

from flask import Flask, request
import memeseeks

app = Flask(__name__)


@app.route("/mrmemeseeks", methods=['POST'])
def mrmemeseeks():
    """Execute the mrmemeseek slack command."""
    response_url = request.form.get('response_url')
    command = request.form.get('command')[1:]
    memeseeks.initial_response(command, response_url)
    query = request.form.get('text').split(";")[0]
    meme_text = request.form.get('text').split(";")[1]
    payload = memeseeks.img_select(command, query, meme_text)
    memeseeks.respond_to_slack(response_url, payload)
    return 'All Done!'


@app.route("/frinkiac", methods=['POST'])
def frinkiac():
    """Execute the mrmemeseek slack command."""
    response_url = request.form.get('response_url')
    command = request.form.get('command')[1:]
    memeseeks.initial_response(command, response_url)
    query = request.form.get('text').split(";")[0]
    meme_text = request.form.get('text').split(";")[1]
    payload = memeseeks.img_select(command, query, meme_text)
    memeseeks.respond_to_slack(response_url, payload)
    return 'All Done!'


@app.route("/morbotron", methods=['POST'])
def morbotron():
    """Execute the mrmemeseek slack command."""
    response_url = request.form.get('response_url')
    command = request.form.get('command')[1:]
    memeseeks.initial_response(command, response_url)
    query = request.form.get('text').split(";")[0]
    meme_text = request.form.get('text').split(";")[1]
    payload = memeseeks.img_select(command, query, meme_text)
    memeseeks.respond_to_slack(response_url, payload)
    return 'All Done!'


# only needed for local dev
if __name__ == "__main__":
    app.run()
