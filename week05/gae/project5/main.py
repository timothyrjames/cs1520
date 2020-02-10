import datetime
import flask
import json


app = flask.Flask(__name__)


@app.route('/')
def root():
    s = '''<html>
    <head>
        <link rel="stylesheet" href="/s/style.css">
        <script src="/s/scripts.js">
        </script>
    </head>
    <body>
        <div id="maincontent">
            This is a simple JSON test.
        </div>
        <div>
            <button onclick="loadServerTime();">Show Server Time</button>
        </div>
        <div>
            Number 1:<br>
            <input type="number" id="number1">
            <br><br>
            Number 2:<br>
            <input type="number" id="number2">
            <br><br>
            <button onclick="multiplyOnServer();">Multiply Numbers on Server</button>
        </div>
    </body>
</html>'''
    return flask.Response(s, mimetype='text/html')


@app.route('/get-data')
def get_data():
    d = dict()
    d['serverTime'] = str(datetime.datetime.now())
    return flask.Response(json.dumps(d), mimetype='application/json')


@app.route('/post-data', methods=['POST'])
def post_data():
    d = dict()
    str1 = flask.request.form.get('num1', 0)
    str2 = flask.request.form.get('num2', 0)

    num1 = 0
    try:
        num1 = float(str1)
    except ValueError as v_err:
        d['error'] = 'Problem parsing the first parameter.'

    num2 = 0
    try:
        num2 = float(str2)
    except ValueError as v_err:
        d['error'] = 'Problem parsing the second parameter.'
    if 'error' not in d:
        d['result'] = num1 * num2

    return flask.Response(json.dumps(d), mimetype='application/json')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
