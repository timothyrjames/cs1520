from email.utils import parseaddr
from flask import Flask, redirect, render_template, request, session

import hashlib
import lmsdata
import lmsdatastore

app = Flask(__name__)
app.secret_key = b'oaijrwoizsdfmnvoiajw34foinmzsdv98j234'


@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
def root():
    return show_page('index.html', 'Main Page')


@app.route('/courses')
def courses_page():
    course_list = lmsdatastore.load_courses()
    return show_page('courses.html', 'Course List', courses=course_list)


@app.route('/course/<coursecode>')
def course_page(coursecode):
    course_object = lmsdatastore.load_course(coursecode)
    return show_page('course.html', course_object.name, course=course_object)


@app.route('/lesson/<coursecode>/<lessonid>')
def lesson_page(coursecode, lessonid):
    course_object = lmsdatastore.load_course(coursecode)
    log('loaded course object: ' + str(course_object.code))
    lesson_object = lmsdatastore.load_lesson(coursecode, int(lessonid))
    log('loaded lesson object: ' + str(lesson_object.title))
    title = course_object.name + ' / ' + lesson_object.title
    user = get_user()
    show_completion_link = True
    if user:
        completions = lmsdatastore.load_completions(user)
        if course_object.code in completions:
            if lesson_object.id in completions[course_object.code]:
                show_completion_link = False

    return show_page('lesson.html', title, course=course_object, 
                     lesson=lesson_object, show=show_completion_link)


@app.route('/signup')
def signup():
    return show_page('signup.html', 'Sign Up')


@app.route('/signin')
def signin():
    return show_page('signin.html', 'Sign In')


@app.route('/dosignin', methods=['POST'])
def dosignin():
    username = request.form.get('username')
    password = request.form.get('password')
    passwordhash = get_password_hash(password)
    user = lmsdatastore.load_user(username, passwordhash)
    if user:
        session['user'] = user.username
        return redirect('/')
    else:
        return show_login_page()


@app.route('/signout')
def signout():
    session['user'] = None
    return redirect('/')


@app.route('/register', methods=['POST'])
def register_user():
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    email = request.form.get('email')
    errors = []
    if password1 != password2:
        errors.append('Passwords do not match.')
    email_parts = parseaddr(email)
    if len(email_parts) != 2 or not email_parts[1]:
        errors.append('Invalid email address: ' + str(email))

    user = lmsdata.User(username, email)
    if errors:
        return show_page('/signup.html', 'Sign Up', errors=errors)
    else:
        passwordhash = get_password_hash(password1)
        lmsdatastore.save_user(user, passwordhash)
        session['user'] = user.username
        return redirect('/courses')


@app.route('/about')
def about():
    user = get_user()
    if user:
        about = lmsdatastore.load_about_user(user)
        return show_page('about.html', 'Edit Info for ' + user, text=about)
    return show_login_page()


@app.route('/saveabout', methods=['POST'])
def saveabout():
    user = get_user()
    if user:
        about = request.form.get('about')
        lmsdatastore.save_about_user(user, about)
        return redirect('/user/' + user)
    return show_login_page()


@app.route('/complete/<coursecode>/<lessonid>')
def complete(coursecode, lessonid):
    user = get_user()
    if user:
        lmsdatastore.save_completion(user, coursecode, int(lessonid))
        return redirect('/lesson/' + coursecode + '/' + lessonid)
    return show_login_page()


@app.route('/user/<username>')
def user_page(username):
    about = lmsdatastore.load_about_user(username)
    about_lines = about.splitlines()
    completions = lmsdatastore.load_completions(username)

    # we use the following loop to sort the lessons in lexical order.
    for course in completions:
        lesson_list = []
        for lesson_id in completions[course]:
            lesson_list.append(completions[course][lesson_id])
        lesson_list.sort()
        completions[course] = lesson_list

    return show_page('user.html', username, lines=about_lines,
                     completions=completions)


@app.route('/createdata')
def createdata():
    lmsdatastore.create_data()
    return 'OK'


def get_password_hash(pw):
    """Creating this as a separate method allows us to perform this operation
    consistently every time we use it."""

    encoded = pw.encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()


def get_user():
    return session.get('user', None)


def show_login_page():
    errors = ['You are not signed in.']
    return show_page('/signin.html', 'Sign In', errors)


def show_page(page, title, courses=None, course=None, lesson=None,
              completions=None, show=True, text=None, lines=None, errors=None):
    return render_template(page,
                           page_title=title,
                           user=get_user(),
                           courses=courses,
                           course=course,
                           lesson=lesson,
                           show=show,
                           completions=completions,
                           text=text,
                           lines=lines,
                           errors=errors)


def log(msg):
    """Log a simple message."""

    print('main: %s' % msg)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
