from flask import Flask, render_template, send_file, request, make_response
from flask_socketio import SocketIO, send
from flask_cors import CORS, cross_origin
from os import environ

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
socket_io = SocketIO(app, cors_allowed_origins='*')
HOST = environ.get('NODE_HOST')
PORT = environ.get('PORT')


@app.route('/')
def index():
    return f'Flask running on {HOST}, and port {PORT}'


@app.route('/image')
def image():
    return send_file('source.gif', mimetype='image/gif')


@app.route('/chat')
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
    socket_io.run(app, host='0.0.0.0', debug=True, log_output=True)
