from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def root():
  # use render_template to convert the template code to HTML.
  # this function will look in the templates/ folder for your file.
  return render_template('index.html', page_title='Main Page')


@app.route('/page1.html')
def first_page():
  # We'll use this to demonstrate the error message on our page.
  return render_template('page1.html',
                         page_title='Page 1', 
                         error_message='There was some error')


@app.route('/page2.html')
def second_page():
  fruit_list = [
    'Apples',
    'Bananas',
    'Cherries',
    'Dates',
  ]

  return render_template('page2.html', page_title='Page 2', fruits=fruit_list)


@app.route('/page3.html')
def third_page():
  states_dict = {
    'PA': 'Pennsylvania',
    'OH': 'Ohio',
    'WV': 'West Virginia',
  }
  return render_template('page3.html', 
                         page_title='Third Page',
                         states=states_dict)


@app.route('/cowclicker')
def cow_clicker():
  return render_template('cowclicker.html', page_title='Click the Cow!')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
