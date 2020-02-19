import flask
import json


app = flask.Flask(__name__)


def log(msg):
    """Log a simple message."""
    # Look at: https://console.cloud.google.com/logs to see your logs.
    # Make sure you have "stdout" selected.
    print('main: %s' % msg)


@app.route('/')
@app.route('/index.html')
def root():
    return flask.render_template('index.html', page_title='Main Page')


@app.route('/authtoken', methods=['POST'])
def authtoken():
    log('Token: ' + request.form.get('token'))
    d = {
        'message': 'Auth Token received at server.',
    }
    return flask.Response(json.dumps(d), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
