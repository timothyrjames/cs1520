import flask
import json
import slidata

from shoppinglistitem import ShoppingListItem


app = flask.Flask(__name__)


def log(msg):
    """Log a simple message."""
    # Look at: https://console.cloud.google.com/logs to see your logs.
    # Make sure you have "stdout" selected.
    print('main: %s' % msg)


@app.route('/get-data')
def get_data():
    responseJson = json.dumps({
        'Text': 'This content was loaded from the server.',
    })
    # we use the Response object here so that we can easily set the mimetype
    # without mimetype, some browsers may not handle the response properly.
    return flask.Response(responseJson, mimetype='application/json')


@app.route('/')
def shopping_list():
    return flask.redirect("/static/index.html", code=302)


@app.route('/load-sl-items')
def load_sli_items():
    # first we load the list items

    log('loading list items.')
    sli_list = slidata.get_list_items()
    json_list = []

    # then we convert it into a normal list of dicts so that we can easily turn
    # it into JSON
    for sl_item in sli_list:
        d = sl_item.to_dict()
        d['id'] = str(sl_item.id)
        json_list.append(d)

    responseJson = json.dumps(json_list)
    return flask.Response(responseJson, mimetype='application/json')


@app.route('/save-item', methods=['POST'])
def save_item():
    # retrieve the parameters from the request
    q = flask.request.form['quantity']
    title = flask.request.form['title']
    item_id = None
    if 'id' in flask.request.form:
        item_id = flask.request.form['id']
    json_result = {}

    try:
        if item_id:
            item = ShoppingListItem(item_id, title, q)
            log('saving list item for ID: %s' % item_id)
            slidata.save_list_item(item)
        else:
            log('saving new list item')
            slidata.create_list_item(ShoppingListItem(None, title, q))
        json_result['ok'] = True
    except Exception as exc:
        log(str(exc))
        json_result['error'] = 'The item was not saved.'

    return flask.Response(json.dumps(json_result), mimetype='application/json')


@app.route('/delete-item', methods=['POST'])
def delete_item():
    # retrieve the parameters from the request
    sli_id = flask.request.form['id']
    json_result = {}
    try:
        log('deleting item for ID: %s' % sli_id)
        slidata.delete_list_item(sli_id)
        json_result['ok'] = True
    except Exception as exc:
        log(str(exc))
        json_result['error'] = 'The item was not removed.'

    return flask.Response(json.dumps(json_result), mimetype='application/json')


# here we use a Flask shortcut to pull the itemid from the URL.
@app.route('/get-item/<itemid>')
def get_item(itemid):
    log('retrieving item for ID: %s' % itemid)
    item = slidata.get_list_item(itemid)
    d = item.to_dict()
    d['id'] = itemid
    return flask.Response(json.dumps(d), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
