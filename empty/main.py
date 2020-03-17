import flask


app = flask.Flask(__name__)


@app.route('/')
def root():
    return show_page('index.html', 'Welcome!', [])


def show_page(page_name, page_title, errors):
    return flask.render_template(page_name, title=page_title, errors=errors)
