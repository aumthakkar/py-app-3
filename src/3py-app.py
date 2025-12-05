
from flask import Flask, jsonify
import socket
import time


app = Flask(__name__)

@app.route('/api/v1/info')
# ‘/’ URL is bound with hello_world() function.
def info():
    return jsonify({
        "hostname" : socket.gethostname(),
        "time" : time.ctime(),
        "env": "dev",
        "msg" : "Hello, this is Pranav!!"
    })

@app.route('/api/v1/healthz')
# ‘/’ URL is bound with hello_world() function.
def healthz():
    return jsonify({
        "status" : "up"
    })

# main driver function
if __name__ == '__main__':

    app.run(host="0.0.0.0")