from flask import Flask, render_template, send_file, request, make_response
from flask_socketio import SocketIO, send
from flask_cors import CORS, cross_origin
from os import environ
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)
socket_io = SocketIO(app)
HOST = environ.get('NODE_HOST')
PORT = environ.get('PORT')


@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response


@app.route('/')
def index():
    return f'Flask running on {HOST}, and port {PORT}'


@app.route('/image')
def image():
    return send_file('source.gif', mimetype='image/gif')


@app.route('/chat')
@cross_origin(headers=['Content-Type', 'Authorization'])
def chat():
    return render_template('index.html')


@socket_io.on('connect')
def client_connect():
    send(f'Client connected to ({HOST}):{PORT}')


@socket_io.on('message')
def handle_message(message):
    send(f'({HOST}): {message}')


if __name__ == '__main__':
    print(f"Starting Webserver on Port {PORT} with host Name {HOST}")
    socket_io.run(app, host='0.0.0.0', debug=True)
