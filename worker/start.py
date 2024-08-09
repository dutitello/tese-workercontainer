import flask 

app = flask.Flask(__name__)

@app.get('/status')
def status():
    return 'online'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)