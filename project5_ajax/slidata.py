import datetime
import logging

from google.cloud import datastore
from google.cloud.datastore.key import Key
from shoppinglistitem import ShoppingListItem


SLI_ENTITY_TYPE = 'ShoppingListItem'
PROJECT_ID = 'coral-box-229919'


def convert_to_object(entity):
  sli_id = entity.key.id_or_name
  return ShoppingListItem(sli_id, entity['title'], entity['quantity'])


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
  key = client.key(SLI_ENTITY_TYPE)
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
  key = client.key(SLI_ENTITY_TYPE, shopping_list_item.id)
  log('loaded key')
  entity = client.get(key)
  entity.update(shopping_list_item.to_dict())
  entity.put()
  log('entity saved')


def get_list_item(sli_id):
  client = datastore.Client(PROJECT_ID)
  key = client.key(SLI_ENTITY_TYPE, sli_id)
  entity = client.get(key)
  return convert_to_object(entity)


def delete_list_item(sli_id):
  client = datastore.Client(PROJECT_ID)
  key = client.key(SLI_ENTITY_TYPE, sli_id)
  client.delete(key)


def log(msg):
  print('slidata: ' + msg)
