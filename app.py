import os
from datetime import datetime
from wsgiref.simple_server import server_version
from flask import Flask, request
from suds.client import Client

app = Flask('app')
server_uri = os.environ.get('SERVER_URI')
client = Client(server_uri, cache=None)


@app.route('/', methods=['GET'])
def index():
    global server_uri
    domain_name = request.args.get('domain_name')
    if domain_name is None:
        domain_name = 'www.facebook.com'
    return client.service.ping_host(domain_name)


@app.route('/showip', methods=['GET'])
def host():
    global server_uri
    domain_name = request.args.get('domain_name')
    if domain_name is None:
        domain_name = 'google.com'
    return client.service.dns_lookup(domain_name)


@app.route('/dns', methods=['GET'])
def dns():
    global server_uri
    domain_name = request.args.get('domain_name')
    if domain_name is None:
        domain_name = 'google.com'
    return client.service.dig_more(domain_name)


if __name__ == '__main__':
    app.run(debug=True)
