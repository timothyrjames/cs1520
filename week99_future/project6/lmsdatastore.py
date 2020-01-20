from google.cloud import datastore

import lmsdata


_PROJECT_ID = 'coding4us'
_USER_ENTITY = 'LmsUser'
_COURSE_ENTITY = 'LmsCourse'
_LESSON_ENTITY = 'LmsLesson'


def _get_client():
    """Build a datastore client."""

    return datastore.Client(_PROJECT_ID)


def log(msg):
    """Log a simple message."""

    print('lmsdatastore: %s' % msg)


def _load_key(client, entity_type, entity_id=None, parent_key=None):
    """Load a datastore key using a particular client, and if known, the ID.  Note
    that the ID should be an int - we're allowing datastore to generate them in 
    this example."""

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
    log('retrieved entity for ' + str(entity_id))
    return entity


def _course_from_entity(course_entity):
    """Translate the Course entity to a regular old Python object."""

    code = course_entity.key.name
    name = course_entity['name']
    desc = course_entity['description']
    course = lmsdata.Course(code, name, desc, [])
    log('built object from course entity: ' + str(code))
    return course


def _lesson_from_entity(lesson_entity, include_content=True):
    """Translate the Lesson entity to a regular old Python object."""

    lesson_id = lesson_entity.key.id
    title = lesson_entity['title']
    content = ''
    if include_content:
        content = lesson_entity['content']
    lesson = lmsdata.Lesson(lesson_id, title, content)
    log('built object from lesson entity: ' + str(title))
    return lesson


def load_course(course_code):
    """Load a course from the datastore, based on the course code."""

    log('loading course: ' + str(course_code))
    client = _get_client()
    course_entity = _load_entity(client, _COURSE_ENTITY, course_code)
    log('loaded course: ' + course_code)
    course = _course_from_entity(course_entity)
    query = client.query(kind=_LESSON_ENTITY, ancestor=course_entity.key)
    for lesson in query.fetch():
        course.add_lesson(_lesson_from_entity(lesson, False))
    log('loaded lessons: ' + str(len(course.lessons)))
    return course


def load_courses():
    """Load all of the courses."""

    client = _get_client()
    q = client.query(kind=_COURSE_ENTITY)
    q.order = ['-name']
    result = []
    for course in q.fetch():
        result.append(course)
    return result


def load_lesson(course_code, lesson_id):
    """Load a lesson under the given course code."""

    log('loading lesson detail: ' + str(course_code) + ' / ' + str(lesson_id))
    client = _get_client()
    parent_key = _load_key(client, _COURSE_ENTITY, course_code)
    lesson_entity = _load_entity(client, _LESSON_ENTITY, lesson_id, parent_key)
    return _lesson_from_entity(lesson_entity)


def load_user(username, passwordhash):
    """Load a user based on the passwordhash; if the passwordhash doesn't match
    the username, then this should return None."""

    client = _get_client()
    q = client.query(kind=_USER_ENTITY)
    q.add_filter('username', '=', username)
    q.add_filter('passwordhash', '=', passwordhash)
    for user in q.fetch():
        return lmsdata.User(user['username'], user['email'], user['about'])
    return None


def load_about_user(username):
    """Return a string that represents the "About Me" information a user has
    stored."""

    user = _load_entity(_get_client(), _USER_ENTITY, username)
    if user:
        return user['about']
    else:
        return ''


def load_completions(username):
    """Load a dictionary of coursecode => lessonid => lesson name based on the
    lessons the user has marked complete."""

    client = _get_client()
    user_entity = _load_entity(client, _USER_ENTITY, username)
    courses = dict()
    for completion in user_entity['completions']:
        lesson_entity = client.get(completion)
        course_entity = client.get(completion.parent)
        code = course_entity.key.name
        if code not in courses:
            courses[code] = dict()
        courses[code][completion.id] = lesson_entity['title']
    return courses


def save_user(user, passwordhash):
    """Save the user details to the datastore."""

    client = _get_client()
    entity = datastore.Entity(_load_key(client, _USER_ENTITY, user.username))
    entity['username'] = user.username
    entity['email'] = user.email
    entity['passwordhash'] = passwordhash
    entity['about'] = ''
    entity['completions'] = []
    client.put(entity)


def save_about_user(username, about):
    """Save the user's about info to the datastore."""

    client = _get_client()
    user = _load_entity(client, _USER_ENTITY, username)
    user['about'] = about
    client.put(user)


def save_completion(username, coursecode, lessonid):
    """Save a completion (i.e., mark a course as completed in the 
    datastore)."""

    client = _get_client()
    course_key = _load_key(client, _COURSE_ENTITY, coursecode)
    lesson_key = _load_key(client, _LESSON_ENTITY, lessonid, course_key)
    user_entity = _load_entity(client, _USER_ENTITY, username)
    completions = set()
    for completion in user_entity['completions']:
        completions.add(completion)
    if lesson_key not in completions:
        user_entity['completions'].append(lesson_key)
    client.put(user_entity)


def create_data():
    """You can use this function to populate the datastore with some basic
    data."""

    client = _get_client()
    entity = datastore.Entity(client.key(_USER_ENTITY, 'testuser'),
                              exclude_from_indexes=[])
    entity.update({
        'username': 'testuser',
        'passwordhash': '',
        'email': '',
        'about': '',
        'completions': [],
    })
    client.put(entity)

    entity = datastore.Entity(client.key(_COURSE_ENTITY, 'Course01'),
                              exclude_from_indexes=['description', 'code'])
    entity.update({
        'code': 'Course01',
        'name': 'First Course',
        'description': 'This is a description for a test course.  In the \
future, real courses will have lots of other stuff here to see that will tell \
you more about their content.',
    })
    client.put(entity)
    entity = datastore.Entity(client.key(_COURSE_ENTITY, 'Course02'),
                              exclude_from_indexes=['description', 'code'])
    entity.update({
        'code': 'Course02',
        'name': 'Second Course',
        'description': 'This is also a course description, but maybe less \
wordy than the previous one.'
    })
    client.put(entity)
    entity = datastore.Entity(
         client.key(_COURSE_ENTITY, 'Course01', _LESSON_ENTITY),
                    exclude_from_indexes=['content', 'title'])
    entity.update({
        'title': 'Lesson 1: The First One',
        'content': 'Imagine there were lots of video content and cool things.',
    })
    client.put(entity)
    entity = datastore.Entity(
         client.key(_COURSE_ENTITY, 'Course01', _LESSON_ENTITY),
                    exclude_from_indexes=['content', 'title'])
    entity.update({
        'title': 'Lesson 2: Another One',
        'content': '1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11',
    })
    client.put(entity)
    entity = datastore.Entity(
         client.key(_COURSE_ENTITY, 'Course02', _LESSON_ENTITY),
                    exclude_from_indexes=['content', 'title'])
    entity.update({
        'title': 'Lesson 1: The First One, a Second Time',
        'content': '<p>Things</p><p>Other Things</p><p>Still More Things</p>',
    })
    client.put(entity)
    entity = datastore.Entity(
         client.key(_COURSE_ENTITY, 'Course02', _LESSON_ENTITY),
                    exclude_from_indexes=['content', 'title'])
    entity.update({
        'title': 'Lesson 2: Yes, Another One',
        'content': '<ul><li>a</li><li>b</li><li>c</li><li>d</li><li></ul>',
    })
    client.put(entity)
