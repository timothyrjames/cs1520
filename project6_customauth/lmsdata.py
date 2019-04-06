class Course(object):
    """Represents a course."""

    def __init__(self, code, name, description, lessons):
        self.code = code
        self.name = name
        self.description = description
        self.lessons = lessons

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def to_dict(self):
        d = {
            'code': self.code,
            'name': self.name,
            'description': self.description,
            'lessons': [],
        }
        for lesson in self.lessons:
            d['lessons'].append(lesson.to_dict())
        return d


class Lesson(object):
    """Represents one lesson in a course."""

    def __init__(self, lesson_id, title, content=''):
        self.id = lesson_id
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            'id': self.lesson_id,
            'title': self.title,
            'content': self.content,
        }


class User(object):
    """A user for the application."""

    def __init__(self, username, email, about=''):
        self.username = username
        self.email = email
        self.about = about

    def to_dict(self):
        return {
            'username': self.username,
            'about': self.about,
            'completions': self.completions,
        }
