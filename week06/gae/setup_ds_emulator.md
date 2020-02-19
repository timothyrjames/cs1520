# Setup Cloud Datastore Emulator

## Introduction

This tutorials walks you through setting up the Cloud Datastore Emulator. This
will allow you to more effectively test your application without having to use
a live Cloud Datastore environment.

## Setup: Java

The Cloud Datastore Emulator requires Java; fortunately your Cloud Shell VM
should already have it installed and configured properly. You can verify that
you have Java 8 with the following command:

```bash
java -version
```

This should show that you are using JDK version 1.8.* - some Java 8 version.

## Installing the Cloud Datastore Emulator

We'll need to install the Cloud Datastore Emulator:

```bash
gcloud components install cloud-datastore-emulator
```

Before starting your emulator, you'll need to set your project.  You'll want
to identify the project you're currently testing or deploying to:

```bash
gcloud config set project YOUR_PROJECT_ID
```

After you've set your project, you can start the emulator in the background
with the following command: 

```bash
gcloud beta emulators datastore start &
```

You'll see lots of output that shows your serving is running.

# Shutting down the Cloud Datastore Emulator

We can easily figure out what the emulator's process ID (PID), and the Java
process ID that's running it, by finding the cloud_datastore process after we
execute a ps command:

```bash
ps
```

You'll see something that looks like this:

```
    PID TTY          TIME CMD
    320 pts/1    00:00:00 bash
   1130 pts/1    00:00:00 python2
   1156 pts/1    00:00:00 cloud_datastore
   1158 pts/1    00:00:02 java
   1192 pts/1    00:00:00 ps
```

Note the PID for cloud_datastore and java. The Java PID should be a number
following the PID for cloud_datastore closely. In the example above, you can 
see that the PID for cloud_datastore is 1156 and the PID for java is 1158.

You can shut down the emulator using the kill command - you'll want to 
substitue your java PID for ```YOUR_PROCESS_ID``` when you execute the
following command:

```bash
kill -9 YOUR_PROCESS_ID
```

# Initialize the Environment

Now that we're up and running and know how to shut the server down (note that
if you practiced shutting down your Cloud Datastore Emulator, you'll need to
start it again), we can configure our datastore.

We will initialize your environment using the gcloud command:

```bash
gcloud beta emulators datastore env-init
```

This will output some commands to set environment variables like the ones 
below. Execute these so that we can connect to our Cloud Datastore properly.

```
export DATASTORE_DATASET=your-project-id
export DATASTORE_EMULATOR_HOST=localhost:8081
export DATASTORE_EMULATOR_HOST_PATH=localhost:8081/datastore
export DATASTORE_HOST=http://localhost:8081
export DATASTORE_PROJECT_ID=your-project-id
```

Alternatively, you can use the command below to automatically set the 
environment variables.

```bash
$(gcloud beta emulators datastore env-init)
```

Once the output of your env-init command is complete, you'll be able to test
your application locally.

## Running Your Application

Use the command below; the dev_appserver.py might *not* pick up the environment
variables automatically, but the command below passes the values you set in
the commands in the previous step.

```bash
dev_appserver.py --env_var DATASTORE_DATASET=$DATASTORE_DATASET --env_var DATASTORE_EMULATOR_HOST=$DATASTORE_EMULATOR_HOST --env_var DATASTORE_EMULATOR_HOST_PATH=$DATASTORE_EMULATOR_HOST_PATH --env_var DATASTORE_HOST=$DATASTORE_HOST --env_var DATASTORE_PROJECT_ID=$DATASTORE_PROJECT_ID .
```

Try [this link](https://ssh.cloud.google.com/devshell/proxy?authuser=0&port=8080&environment_id=default)
to view your application directly.
