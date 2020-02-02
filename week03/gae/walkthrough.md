# First Deployment Tutorial

## Your First Google App Engine Project

This tutorial explains how to deploy your first application to Google App 
Engine. If you've made it this far, you most likely already have the project0
application cloned from github.

You'll want to start by installing Flask.

```bash
pip3 install Flask==1.1.1
```

Once you've got Flask installed, you can easily test your first application 
by running the following command.

```bash
python3 main.py
```

Your application can be tested by using the web preview; there's a button to 
open it in the top-right corner of your screen.

## Deploying Your Application

If you haven't created a project yet, you can do that from the command line.

To create your project, enter the command below, but following "gcloud projects
create" you need to enter a project ID. It will need to be unique for all of
App Engine.

```bash
gcloud projects create 
```

If you _have_ created a project, you'll need to set it using the gcloud command
- but enter your project ID following the "gcloud config set project" text:

```bash
gcloud config set project
```

Once you've done this, you can deploy easily:

```bash
gcloud app deploy
```

Now you can find your application by navigating to the following URL in your 
browser: 

http://YOUR-APPLICATION-ID.appspot.com/ 

