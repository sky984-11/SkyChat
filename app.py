'''
Description: 
Author: sky
Date: 2025-01-07 10:14:40
LastEditTime: 2025-01-07 14:41:56
LastEditors: sky
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import eventlet
eventlet.monkey_patch() 


app = Flask(__name__)
app.secret_key = "your_secret_key"  # 设置一个 secret key
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
    # socketio.run(app, host='0.0.0.0', port=8888, debug=True)
    # 在 socketio.run 中添加 allow_unsafe_werkzeug=False
    socketio.run(app, host='0.0.0.0', port=8888, debug=True, allow_unsafe_werkzeug=False)
