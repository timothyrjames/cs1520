import datetime
import logging

from google.cloud import datastore
from google.cloud.datastore.key import Key
from shoppinglistitem import ShoppingListItem


# We need to identify the entity type for our list items.
# note that this is arbitrary and can be whatever you like.
SLI_ENTITY_TYPE = 'ShoppingListItem'
PROJECT_ID = 'coral-box-229919'


def convert_to_object(entity):
  sli_id = entity.key.id_or_name
  return ShoppingListItem(sli_id, entity['title'], entity['quantity'])


def load_key(client, item_id=None):
  key = None
  if item_id:
    key = client.key(SLI_ENTITY_TYPE, int(item_id))
  else:
    key = client.key(SLI_ENTITY_TYPE)
  return key


def load_entity(client, item_id):
  key = load_key(client, item_id)
  entity = client.get(key)
  log('retrieved entity for ' + item_id)
  return entity


def get_list_items():
  client = datastore.Client(PROJECT_ID)
  log('retrieving list')
  query = client.query(kind=SLI_ENTITY_TYPE)
  sli_items = list(query.fetch())
  result = list()
  for item in sli_items:
    result.append(convert_to_object(item))

  log('list retrieved. %s items' % len(result))
  return result


def create_list_item(shopping_list_item):
  client = datastore.Client(PROJECT_ID)
  key = load_key(client)
  log('created key for new entity')
  shopping_list_item.id = key.id_or_name
  entity = datastore.Entity(key)
  log('loaded entity')
  entity['quantity'] = shopping_list_item.quantity
  entity['title'] = shopping_list_item.title
  client.put(entity)
  log('saved entity')


def save_list_item(shopping_list_item):
  client = datastore.Client(PROJECT_ID)
  entity = load_entity(client, shopping_list_item.id)
  entity.update(shopping_list_item.to_dict())
  client.put(entity)
  log('entity saved')


def get_list_item(sli_id):
  client = datastore.Client(PROJECT_ID)
  log('retrieving object for: ' + sli_id)
  entity = load_entity(client, sli_id)
  return convert_to_object(entity)


def delete_list_item(sli_id):
  client = datastore.Client(PROJECT_ID)
  key = load_key(client, sli_id)
  log('key loaded: ' + sli_id)
  client.delete(key)
  log('key deleted')


def log(msg):
  print('slidata: ' + msg)
