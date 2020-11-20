from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from github actions'

@app.route('/v2')
def v2():
    return 'Hello from auto apdate'

@app.route('/ssh')
def ssh():
    return 'Hello from auto apdate with ssh'
