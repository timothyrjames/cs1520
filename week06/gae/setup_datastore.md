# Setting Up Remote Datastore Access

## Introduction

This tutorial will walk you through setting up remote Cloud Datastore 
access. Note that if you intend to use the Cloud Datastore Emulator, you can
skip this tutorial.

## Installation

First off, you'll need to install the cloud storage package. This will allow
you to leverage the appropriate modules to connect to Cloud Datastore
directly.

```bash
pip3 install --upgrade google-cloud-storage
```

Make sure you have a project set; you can use the following command to set
your project ID.

```bash
gcloud config set project your-project-id
```

You'll need a service account; this is the account that will be 
authorized to use the Cloud Datastore. Note that ```mydatastore``` is your
account name; you can change this if you prefer.

```bash
gcloud iam service-accounts create mydatastore
```

## Associate Your account

Now that the account is created, use the following command to add your account
to your project. You'll want to substitute your project ID, and the name of 
your service account.

```bash
gcloud projects add-iam-policy-binding your-project-id --member "serviceAccount:mydatastore@your-project-id.iam.gserviceaccount.com" --role "roles/owner"
```

## Generate Service Account Keys

Now that we have associated the account with our project, we want to generate
service keys. These will automate the authentication of our application using
a generated key.  Remember to enter your service account below.

```bash
gcloud iam service-accounts keys create service-acct-keys.json --iam-account mydatastore@your-project-id.iam.gserviceaccount.com
```

Store your JSON file somewhere that you'll be sure not to check into a git 
repository. Note the location of the file, and set an environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-acct-keys.json
```

Once you've done all of this, you should be able to connect to the Cloud
Datastore remotely, for independent applications or development purposes.

