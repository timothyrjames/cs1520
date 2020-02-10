from flask import Flask, redirect


app = Flask(__name__)

@app.route('/')
def root():
    return redirect("/s/index.html", code=302)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
