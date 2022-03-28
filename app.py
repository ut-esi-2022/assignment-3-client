import os
from datetime import datetime
from wsgiref.simple_server import server_version
from flask import Flask, request
from suds.client import Client

app = Flask("__name__")
server_uri = os.environ.get("SERVER_URI")


@app.route('/')
def index():
    global server_uri
    return f"Server URL: {server_uri}"


@app.route('/showip', methods=['GET'])
def host():
    client = Client(server_uri, cache=None)
    domain_name = request.args.get('domain_name')
    if domain_name is None:
        domain_name = 'google.com'
    return client.service.res_name(domain_name)


@app.route('/dns', methods=['GET'])
def dns():
    client = Client(server_uri, cache=None)
    domain_name = request.args.get('domain_name')
    if domain_name is None:
        domain_name = 'google.com'
    return client.service.more_info(domain_name)


if __name__ == "__main__":
    app.run(debug=True)
