from datetime import datetime
import os
from flask import Flask
from suds.client import Client

app = Flask("__name__")
server_uri = os.environ.get("SERVER_URI")
client = Client(server_uri, cache=None)


@app.route('/')
def index():
    return client.service.HelloWorldService()


if __name__ == "__main__":
    app.run(debug=True)
