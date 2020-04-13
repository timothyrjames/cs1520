import datastore
import flask
import urllib

from google.cloud import storage


app = flask.Flask(__name__)


@app.route('/')
def root():
    pd = PageData('File Upload')
    return show_page('index.html', pd)


@app.route('/upload', methods=['POST'])
def upload():
    pd = PageData('File Upload')

    uploaded_file = flask.request.files.get('file')
    filename = flask.request.form.get('filename')
    content_type = uploaded_file.content_type

    if not uploaded_file:
        pd.add_error('No file uploaded.')
        return show_page('index.html', pd)

    gcs_client = storage.Client()
    storage_bucket = gcs_client.get_bucket('cs1520-image-uploads')
    blob = storage_bucket.blob(uploaded_file.filename)

    blob.upload_from_string(uploaded_file.read(), content_type=content_type)

    datastore.save_file(filename, blob.public_url)
    return flask.redirect('showfile?name=' + urllib.parse.quote_plus(filename))


@app.route('/showfile')
def showfile():
    pd = PageData('File')
    filename = flask.request.args.get('name')
    pd.p['name'] = filename
    url = datastore.get_url_for_file(filename)
    if url:
        pd.p['url'] = url
    else:
        pd.add_error('File not found.')
    return show_page('showfile.html', pd)


def show_page(filename, pagedata):
    return flask.render_template(filename, pd=pagedata)


class PageData(object):
    def __init__(self, title):
        self.title = title
        self.errors = []
        self.p = {}

    def add_error(self, error):
        self.errors.append(error)

    def set_param(self, key, value):
        self.p[key] = value


def log(msg):
    """Log a simple message."""

    print('main: %s' % msg)
