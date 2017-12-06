"""Use Flask & ngrok to test command."""

from flask import Flask, request
import memeseeks

app = Flask(__name__)


@app.route("/mrmemeseeks", methods=['POST'])
def mrmemeseeks():
    """Execute the mrmemeseek slack command."""
    response_url = request.form.get('response_url')
    memeseeks.initial_response(response_url)
    payload = memeseeks.img_select()
    memeseeks.respond_to_slack(response_url, payload)
    return 'All Done!'


# only needed for local dev
if __name__ == "__main__":
    app.run()
