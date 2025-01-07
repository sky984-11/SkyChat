'''
Description: 
Author: sky
Date: 2025-01-07 10:14:40
LastEditTime: 2025-01-07 17:05:19
LastEditors: sky
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import eventlet
eventlet.monkey_patch() 


app = Flask(__name__)
app.secret_key = "skychat"  # 设置一个 secret key
socketio = SocketIO(app)

# 页面路由
@app.route('/')
def index():
    return render_template('index.html')

# 监听消息事件
@socketio.on('send_message')
def handle_message(data):
    print(f"Received message: {data['message']}")
    emit('receive_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888, debug=True, allow_unsafe_werkzeug=False)
