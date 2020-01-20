from flask import Flask
from flask import Response


app = Flask(__name__)

@app.route('/')
def root():
    return Response('This is NOT HTML.', mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
