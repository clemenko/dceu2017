from flask import Flask, render_template, request, jsonify, redirect, url_for
import os, requests

app = Flask(__name__)
server_name = os.getenv('HOSTNAME')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/', methods=['POST'])
def shutdown():
    shutdown_server()
    requests.post('http://gitlab.dockr.life/api/v4/projects/2/trigger/pipeline?token=2d090f6205949c5ece178675c679a0&ref=master')
    return 'works', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
