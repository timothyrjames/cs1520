import flask


app = flask.Flask(__name__)


@app.route('/')
@app.route('/swap')
def root():
    return flask.redirect("/s/swap-div.html", code=302)


@app.route('/sandwich')
def sandwich():
    return flask.redirect('/s/sandwich-generator.html', code=302)


@app.route('/cow')
def cow():
    return flask.redirect('/s/cow-clicker.html', code=302)


@app.route('/drag')
def drag():
    return flask.redirect('/s/cow-dragger.html', code=302)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
