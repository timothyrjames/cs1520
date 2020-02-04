# Serving Static Files Tutorial

## Introduction

This tutorial explains how to deploy an application that serves static files
in Google App Engine.

## Our app.yaml File

In our app.yaml file, our handlers are resolved in order. Our original /.* 
handler will catch all requests to our web application. We'll want to add
another handler that will direct the user requesting a resource to a set of
static files on the filesystem. Unlike our Python code, which will respond to
a request by dynamically executing some code, these files will be transmitted
to the user exactly as they are.

We do this by using the "static_dir" property as illustrated below.

```yaml
runtime: python37

handlers:
- url: /static
  static_dir: staticfiles

- url: /.*
  script: auto
```

If a user requests any resource in our web application that starts with the
path ```/static```, the application will look in the ```staticfiles``` 
directory for that resource and send it.

## Testing Static Files

Before, our entire application was entirely in Flask, so we could run it with
the following command (make sure you're in the project1 directory):

```bash
python3 main.py
```

Try using Web Preview to see your dynamically served content, as well as your
static content at ```/static/index.html``` - what happens?

If you try to see the static files, you'll likely find that they are not served
properly. You might get "Not Found" errors in your browser. That's because the
way that pure Flask and Google App Engine serve static files is a bit 
different.

Use Ctrl+C to exit your application; then, to run your application and test the
static file serving, try this instead:

```bash
dev_appserver.py app.yaml
```

Now you should be able to open the Web Preview and see your dynamically served
application, as well as the static index.html page at ```/static/index.html```.

As usual, Ctrl+C will exit your application.


## Deploying and Viewing Your Application 

Once you've done this, you can deploy easily:

```bash
gcloud app deploy
```

After this completes, you can find your application by navigating to the 
following URL in your browser: 

```
http://YOUR-APPLICATION-ID.appspot.com/ 
```

You can also enter the command below to view your live application:

```bash
gcloud app browse
```

Try this link to see your static content:

```
http://YOUR-APPLICATION-ID.appspot.com/static/index.html
```
