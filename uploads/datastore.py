from google.cloud import datastore


_FILE_ENTITY = 'FileEntity'


def save_file(filename, url):
    client = _get_client()
    key_for_file_entity = _load_key(client, _FILE_ENTITY, filename)
    entity = datastore.Entity(key=key_for_file_entity)
    entity.update({
        'url': url
    })
    client.put(entity)


def get_url_for_file(filename):
    client = _get_client()
    entity = _load_entity(client, _FILE_ENTITY, filename)
    if entity:
        return entity['url']
    return None


def _get_client():
    """Build a datastore client."""

    return datastore.Client()


def _load_key(client, entity_type, entity_id=None, parent_key=None):
    """Load a datastore key using a particular client."""

    key = None
    if entity_id:
        key = client.key(entity_type, entity_id, parent=parent_key)
    else:
        # this will generate an ID
        key = client.key(entity_type)
    return key


def _load_entity(client, entity_type, entity_id, parent_key=None):
    """Load a datstore entity using a particular client, and the ID."""

    key = _load_key(client, entity_type, entity_id, parent_key)
    entity = client.get(key)
    log('retrieved entity: ' + entity_type + ' for ID: ' + str(entity_id))
    return entity


def _new_entity(client, entity_type):
    """Build a new entity of the given type."""

    return datastore.Entity(_load_key(client, entity_type))


def log(msg):
    """Log a simple message."""

    print('datastore: %s' % msg)
