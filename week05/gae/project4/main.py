from flask import Flask, redirect


app = Flask(__name__)

@app.route('/')
@app.route('/swap')
def root():
    return redirect("/s/swap-div.html", code=302)


@app.route('/sandwich')
def sandwich():
    return redirect('/s/sandwich-generator.html', code=302)


@app.route('/cow')
def cow():
    return redirect('/s/cow-dragger.html', code=302)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
