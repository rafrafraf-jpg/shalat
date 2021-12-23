from flask import Flask
from flask_socketio import SocketIO, emit
from flask_mobility import Mobility

import os

app = Flask(__name__)
Mobility(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'hello world'

@socketio.on('mouse')
def mouse(data):
    print(0)
    if data.get('passw') == os.getenv('pass'):
        print(1)
        emit('move', {'x': data.get('x'), 'y': data.get('y')}, broadcast=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
