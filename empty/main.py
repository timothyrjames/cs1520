import flask
import json


app = flask.Flask(__name__)


@app.route('/')
def root():
    pd = PageData('Welcome!')
    return show_page('index.html', pd)


@app.route('/json/sample')
def json_sample():
    jd = JsonData()
    jd.set_data({
        'sample_property': 'some value'
    })
    return show_json(jd)


def show_page(filename, pagedata):
    return flask.render_template(filename, pd=pagedata)


def show_json(json_data):
    response_dict = {
        'errors': json_data.errors,
        'status': json_data.status,
        'data': json_data.data,
    }
    responseJson = json.dumps(response_dict)
    return flask.Response(responseJson, mimetype='application/json')


class PageData(object):
    def __init__(self, title):
        self.title = title
        self.errors = []
        self.p = {}

    def add_error(self, error):
        self.errors.append(error)

    def set_param(self, key, value):
        self.p[key] = value


class JsonData(object):
    def __init__(self):
        self.errors = []
        self.status = []

    def add_error(self, error):
        self.errors.append(error)

    def add_status(self, status):
        self.status.append(status)

    def set_data(self, data):
        self.data = data


def log(msg):
    """Log a simple message."""

    print('main: %s' % msg)
