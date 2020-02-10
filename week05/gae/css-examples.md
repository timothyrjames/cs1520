# CSS Examples

## Introduction

This tutorial explains how to deploy CSS samples to App Engine.

## Redirecting

Similar to the HTML example; the first thing we do in our application is a
redirect.

```py
@app.route('/')
def root():
    return redirect("/s/index.html", code=302)
```

This will allow our application to send users directly to our static HTML
content.

## Running Our Application

Again, make sure your current directory is project3, and you can run the 
dev_appserver:

```bash
dev_appserver.py app.yaml
```

Now you should be able to open the Web Preview.

Try [this link](https://ssh.cloud.google.com/devshell/proxy?authuser=0&port=8080&environment_id=default)
to view it directly. It's useful to look at the HTML and CSS as rendered in your
browser, as well as the source code within the code editor.


## HTML - index.html

Let's start with our index.html.  You can view it in the editor with this 
command:

```bash
edit static/index.html
```

There are few differences between the last example and this one, but I wanted
to call out the one difference below.

```html
<section style="font-weight: bold; font-size: 1.25rem;">
    This is an HTML file, and it is full of links to samples.
</section>
```

Note that often the quickest way to style text is to just add a ```style``` 
attribute to enter some style declarations for _only_ that element.  This is 
generally not a great idea as it's a better practice to separate your styling
from your HTML.

## HTML - links.html

Next let's look at links.html. On your HTML page, click the "Link Samples"
link.  You'll notice a lot of new differences.

The source code can be viewed here:

```bash
edit static/links.html
```

You'll see a lot of new code in the ```style``` attribute within your HTML
```head``` element.

```css
body {
    font-family: Arial;
    font-size: 10pt;
}
a {
    text-decoration: none;
    font-weight: bold;
}
a:hover {
    text-decoration: underline;
}
nav a {
    display: inline block;
    margin: 8px;
    padding: 5px;
    border: 1px solid #0000ff;
    font-weight: normal;
    border-radius: 10px;
}
```

* body: this selector will apply to the body element in your HTML document.
* a: this applies to all anchor elements in your document.
* a:hover: this selector applies when someone hovers over your links.
* nav a: this selector applies to any anchor elements that are within a ```nav``` element.

Note how the ```a``` elements within the nav section behave differently; this 
will hopefully start to illustrate the value of using some of the structural 
HTML elements.


## HTML - sections.html

The next interesting area will be our sections page.

Try opening the file and viewing the source:
```bash
edit static/sections.html
```

The notable change is using an external stylesheet:

```html
<link rel="stylesheet" href="style.css">
```

You can inspect this by looking at the actual CSS file:

```bash
edit static/style.css
```

This file includes a variety of selector types and declarations; try modifying 
some of these to see how they behave and respond.


## HTML - tables.html

Continuing on, we'll look at how to build tables in HTML.

```bash
edit static/tables.html
```

In this example we use a ```style``` element to apply styles to the table.

```html
<head>
    <title>HTML samples</title>
    <style>
        td {
            padding: 2px;
            border: 2px;
            border-style: solid;
            border-color: #000000;
            vertical-align: top;
        }
        th {
            padding: 3px;
            padding-top: 8px;
            font-weight: bold;
            background-color: #404040;
            color: #ffffff;
            border: 1px;
            border-style: solid;
            border-color: #808080;
            vertical-align: bottom;
        }
        h1 {
            font-family: Verdana, sans-serif;
            font-size: 14pt;
            font-weight: bold;
            font-style: italic;
        }
        #highlight {
            border-color: #ff0000;
        }
    </style>
</head>
```

