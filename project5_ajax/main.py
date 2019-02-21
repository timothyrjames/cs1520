import json
import slidata

from flask import Flask, Response, render_template, request
from shoppinglistitem import ShoppingListItem


app = Flask(__name__)


def log(msg):
  print('main: ' + msg)


@app.route('/')
@app.route('/index.html')
def root():
  return render_template('index.html', page_title='Load Data Ddemo')


@app.route('/get-data')
def get_data():
  responseJson = json.dumps({
    'Text': 'This content was loaded from the server.',
  })
  # we use the Response object here so that we can easily set the mimetype
  # without mimetype, some browsers may not handle the response properly.
  return Response(responseJson, mimetype='application/json')


@app.route('/shopping_list.html')
def shopping_list():
  return render_template('shopping_list.html', page_title='Shopping List Demo')


@app.route('/load-sl-items')
def load_sli_items():
  sli_list = slidata.get_list_items()
  json_list = []
  for sl_item in sli_list:
    d = sl_item.to_dict()
    d['id'] = str(sl_item.id)
    json_list.append(d)
  responseJson = json.dumps(json_list)
  return Response(responseJson, mimetype='application/json')


@app.route('/save-item', methods=['POST'])
def save_item():
  q = request.form['quantity']
  title = request.form['title']
  json_result = {}
  
  try:
    slidata.create_list_item(ShoppingListItem(None, title, q))
    json_result['ok'] = True
  except Exception as exc:
    log(str(exc))
    json_result['error'] = 'The item was not saved.'

  return Response(json.dumps(json_result), mimetype='application/json')


@app.route('/delete-item', methods=['POST'])
def delete_item():
  sli_id = request.form['id']
  json_result = {}
  try:
    slidata.delete_list_item(sli_id)
    json_result['ok'] = True
  except Exception as exc:
    log(str(exc))
    json_result['error'] = 'The item was not removed.'

  return Response(json.dumps(json_result), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
