import datetime
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! time is ' + str(datetime.datetime.now())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
