"""Use Flask & ngrok to test command."""

from flask import Flask, request
from memeseeks import initial_response, respond_to_slack, img_select

app = Flask(__name__)


@app.route("/mrmemeseeks", methods=['POST'])
# @app.route("/mrmemeseeks")
def mrmemeseeks():
    """Execute the mrmemeseek slack command."""
    response_url = request.form.get('response_url')
    initial_response(response_url)
    payload = img_select()
    respond_to_slack(response_url, payload)


# only needed for local dev
if __name__ == "__main__":
    app.run()
