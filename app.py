from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def info(server_name=None):
    return server_name + ' DockerconEU is awesome ! ', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
