import datetime
import logging

from google.cloud import datastore
from google.cloud.datastore.key import Key
from shoppinglistitem import ShoppingListItem


# We need to identify the entity type for our list items.
# Note that this data type is arbitrary and can be whatever you like.
SLI_ENTITY_TYPE = 'ShoppingListItem'
PROJECT_ID = 'coral-box-229919'


def log(msg):
  """Log a message using INFO level."""
  # you may find it useful to change "logging.info" to "print" for easy debugging
  logging.info('slidata: %s' % msg)


def convert_to_object(entity):
  """Convert the entity returned by datastore to a normal object."""
  sli_id = entity.key.id_or_name
  return ShoppingListItem(sli_id, entity['title'], entity['quantity'])


def load_key(client, item_id=None):
  """Load a datastore key using a particular client, and if known, the ID.  Note
  that the ID should be an int - we're allowing datastore to generate them in 
  this example."""
  key = None
  if item_id:
    key = client.key(SLI_ENTITY_TYPE, int(item_id))
  else:
    # this will generate an ID
    key = client.key(SLI_ENTITY_TYPE)
  return key


def load_entity(client, item_id):
  """Load a datstore entity using a particular client, and the ID."""
  key = load_key(client, item_id)
  entity = client.get(key)
  log('retrieved entity for ' + item_id)
  return entity


def get_list_items():
  """Retrieve the list items we've already stored."""
  client = datastore.Client(PROJECT_ID)

  # we build a query
  query = client.query(kind=SLI_ENTITY_TYPE)

  # we execute the query
  sli_items = list(query.fetch())

  # the code below converts the datastore entities to plain old objects - 
  # this is good for decoupling the rest of our app from datastore.
  result = list()
  for item in sli_items:
    result.append(convert_to_object(item))

  log('list retrieved. %s items' % len(result))
  return result


def create_list_item(shopping_list_item):
  """Create a new shopping list item entity from the specified object."""
  client = datastore.Client(PROJECT_ID)
  key = load_key(client)
  shopping_list_item.id = key.id_or_name
  entity = datastore.Entity(key)
  entity['quantity'] = shopping_list_item.quantity
  entity['title'] = shopping_list_item.title
  client.put(entity)
  log('saved new entity for ID: %s' % key.id_or_name)


def save_list_item(shopping_list_item):
  """Save an existing list item from an object."""
  client = datastore.Client(PROJECT_ID)
  entity = load_entity(client, shopping_list_item.id)
  entity.update(shopping_list_item.to_dict())
  client.put(entity)
  log('entity saved for ID: %s' % shopping_list_item.id)


def get_list_item(sli_id):
  """Retrieve an object for the ShoppingListItem with the specified ID."""
  client = datastore.Client(PROJECT_ID)
  log('retrieving object for ID: %s' % sli_id)
  entity = load_entity(client, sli_id)
  return convert_to_object(entity)


def delete_list_item(sli_id):
  """Delete the entity associated with the specified ID."""
  client = datastore.Client(PROJECT_ID)
  key = load_key(client, sli_id)
  log('key loaded for ID: %s' % sli_id)
  client.delete(key)
  log('key deleted for ID: %s' % sli_id)
