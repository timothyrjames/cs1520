# File Upload Tutorial

## Uploading Files Using GCS

This tutorial explains how to upload files to Google Cloud Storage, where you
can serve them using Google App Engine. 

## Creating a GCS Bucket for Your Files

The first thing you'll want to do is create a storage bucket - this is a place
where GCS can store the files that users upload. You do this using the gsutil 
command (be sure to change "your-bucket-name" to something meaningful):

```bash
gsutil mb gs://your-bucket-name
```

You should see a brief message before you're returned to the command prompt.


## Adding Permissions

Now that we have a storage bucket, we need to allow anybody to read it.  We do
this using the gsutil command, too. Make sure you use the same storage bucket 
name in the command below as you used in the last step.

```bash
gsutil defacl set public-read gs://your-bucket-name
```

## Setting Requirements

_Note: All code is available on [GitHub](https://github.com/timothyrjames/cs1520/tree/master/uploads)._

You'll need some values for your requirements.txt file. Of course you'll need
Flask, and if you want to store in the Datastore, you'll need the Datastore
library; you'll also need google-cloud-storage, gunicorn, and 
google-cloud-core.

Your requirements.txt file should have the following:

```
Flask==1.1.1
google-cloud-datastore==1.7.3
google-cloud-storage==1.26.0
gunicorn==20.0.4
google-cloud-core
```

## HTML Form

You'll need a specific kind of HTML form to prepare for file upload. Your form
method should be "post" but you'll need a new attribute - enctype. We will give
it the value "multipart/form-data" - this identifies that your form submission
may include entire files.

```HTML
<form method="post" action="/upload" enctype="multipart/form-data">
    Select a File:<br>
    <input type="file" name="file">
    <br><br>
    <input type="submit" value="Upload!">
</form>
```

## Handling the Upload

Now that you've uploaded a file, you'll need to handle the request in your 
Python code; you want to get the uploaded file and its content type:

```Python
uploaded_file = flask.request.files.get('file')
content_type = uploaded_file.content_type
```

Next you'll want to store this file in GCS. The available libraries make this
easy:

```Python
gcs_client = storage.Client()
storage_bucket = gcs_client.get_bucket('your-bucket-name')
blob = storage_bucket.blob(uploaded_file.filename)
blob.upload_from_string(uploaded_file.read(), content_type=content_type)
```

## Serving the GCS File

Serving the file is also easy - the blob will have a public URL that you can 
use to embed in an ```img``` element. Just use ```blob.public_url```

```Python
url = blob.public_url
```

and embed the result in the ```src``` attribute like this:

```HTML
<img src="{{ url }}">
```
