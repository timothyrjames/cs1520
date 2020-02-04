# HTML Examples

## Introduction

This tutorial explains how to deploy HTML samples to App Engine.

## Redirecting

The first thing we do in our application is a redirect.

```py
@app.route('/')
def root():
    return redirect("/s/index.html", code=302)
```

This will allow our application to send users directly to our static HTML
content.

You can look at the complete main.py file with this command (make sure your 
current directory is project2):

```bash
edit main.py
```

By returning the redirect with HTTP status code 302, we're directing users
to this new page.

## Running Our Application

Again, make sure your current directory is project2, and you can run the 
dev_appserver:

```bash
dev_appserver.py app.yaml
```

Now you should be able to open the Web Preview.

Try [this link](https://ssh.cloud.google.com/devshell/proxy?authuser=0&port=8080&environment_id=default)
to view it directly. It's useful to look at the HTML as it's rendered in your
browser, as well as the source code within the code editor.


## HTML - index.html

Let's start with our index.html.  You can view it in the editor with this 
command:

```bash
edit staticfiles/index.html
```

Note that HTML is usually made up of "tags" or "elements" - named values, 
surrounded by angle brackets. You'll usually see the "HTML" element first.
Note that tags and elements are often used interchangeably - there is no
real difference in the terminology.

```html
<html>
```

Below the HTML element, you may see the "HEAD" element. This usually contains
headers, directives, scripts, stylesheets, and other things we might not see 
_directly_ as content. For this file, we just have a "TITLE" element - this 
will be what's displayed in your browser tab.

Note the _closing_ tag - ```</head>``` - lots of HTML elements have both open
and close tags.

```html
<head>
    <title>HTML samples</title>
</head>
```

Below that we have the "BODY" element. It holds the actual content we will
display to the user.

```html
<body>
    <header>
        <h1>HTML Samples</h1>
    </header>
    <nav>
        <a href="links.html">Link Samples</a>
        <a href="images.html">Image Samples</a>
        <a href="lists.html">List Samples</a>
        <a href="sections.html">Section Samples</a>
        <a href="tables.html">Table Samples</a>
        <a href="forms.html">Form Samples</a>
    </nav>
    <section>
        This is an HTML file, and it is full of links to samples.
    </section>
</body>
```

There are bunch of new elements here; let's look at them one by one.
* header: this is a structural element. It doesn't do anything on its own, but we will use it later.
* h1: this is a top level heading. You can also use h2, h3, h4, h5, and h6.
* nav: this is another structural element. 
* a: this is an "anchor" element. It's used to provide links. ```href``` is an attribute on this element; it identifies _where_ the link goes. The file named in ```href``` is appended to the end of the path of the current URL. The text inside the open and close anchor tags is the text displayed for the link.
* section: another structural element.

Each of these links shows us some more HTML.

## HTML - links.html

Next let's look at links.html. On your HTML page, click the "Link Samples"
link.

The source code can be viewed here:

```bash
edit staticfiles/links.html
```

Since we discussed a lot of the file in the last step, we'll focus on new 
elements here.

```html
<section>
    <p id="top">
        Links
    </p>
    <a href="http://amazon.com">This is a link to a website.</a>
    <br>
    <a href="tables.html">This is a link to another page on this website.</a>
    <br>
    <a href="tables.html" target="_blank">
        This is a link to another page on this website, but it in a new window.
    </a>
    <br>
    <a href="/static/lists.html">
        This is an <strong>absolute</strong> link to another page on this website.
    </a>
    <br>
    <em>
        Note that it starts with a forward slash.
    </em>
    <br>
    <a href="#bottom">This is a link to an ID at the bottom of the page.</a>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <p id="bottom">
        This is the bottom of the page.
    </p>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
    <a href="#top">This is a link back to the top.</a>
    <p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p><p>.</p>
</section>
```

* p: a very common element. ```p``` is for paragraph - it identifies a new paragraph of content. Note that any tag can have an ```id``` attribute.
* a: though we talked about anchor tags in the previous step, the ```target``` attribute allows us to open the link somewhere else; in this case, ```target="_blank"``` opens in a new window.
  * Using the octothorpe, we can also link to elements on the same page by including their ID. We use ```href="#top"``` and ```href="#bottom"``` in this example.
* br: an element for line breaks. Unlike ```p``` the ```br``` tag does not have a closing tag.
* em: an element used to emphasize certain text.

Try clicking the different links to see how they behave in your browser.

## HTML - images.html

Next, let's move on to the images example.

```bash
edit staticfiles/images.html
```

Images allow us to display graphical content on our page. We we typically use 
the ```img``` element for this purpose.  Take a look at the code below.

```html
<section>
    Images should have a few attributes set.
    You should minimally set the alt, width, and height attributes.<br>
    <img src="slides_header.png" alt="header for slides" width="1133" height="361"><br><br>
    <img src="gae-logo.png" alt="app engine logo" width="237" height="211"><br><br>
    You can also use width and height to warp / resize (though this isn't a great way to do it).
    <br><br>
    <img src="slides_header.png" alt="header for slides" width="500" height="361">
</section>
```

There are a few interesting new concepts in this sample.

* img: the image element.
  * It should always populate the ```src``` attribute. This shows the (relative) location of the file.
  * The ```alt``` attribute should also be populated; this shows alternate text if the image can't be displayed.
  * The ```width``` and ```height``` attributes should probably also be populated; these allow the browser to allocate space for the image before it's downloaded.

## HTML - lists.html

Moving on to the List Samples, we can see how we can create unordered and 
ordered lists.  You can open the source:

```bash
edit staticpages/lists.html
```

See the HTML below. 

```html
<section>
    This is an ordered list.
    <ol>
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
        <li>Item D</li>
        <li>Item E</li>
        <li>Item F</li>
    </ol>
</section>
<section>
    This is an unordered list.
    <ul>
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
        <li>Item D</li>
        <li>Item E</li>
        <li>Item F</li>
    </ul>
</section>
```

* ol: this is the element for an ordered list (i.e., a list that is numbered).
* ul: this is the element for an unordered list (i.e., a list with bullet points).
* li: for either list, this is the element for list items.

## HTML - sections.html

The Sections Samples show some of the structural elements in HTML; we will use
these a bit more when we get into CSS.

Try opening the file and viewing the source:
```bash
edit staticpages/sections.html
```

The relevant HTML code is below. All of these are structural elements, so their
display will not be very compelling until we start styling them in different 
ways using CSS.

```html
<section>
    This is a section.
</section>
<section>
    This is another section.
    <div>This is a div inside of the section.</div>
    <div>This is another div inside of the section.</div>
</section>
<article>
    This is an article.
    <span>This is a span inside the article</span>
    <span>This is a 2nd span inside the article.</span>
</article>
<aside>
    This is an aside.
</aside>
<footer>
    This is the footer.
    <p>
        <em>This is a bit disappointing, isn't it?</em>
    </p>
</footer>
```

* div: a _very_ common structural element. In HTML5 we probably use ```div``` elements more than others; they're typically used as a container for styling or for interaction.
* article: a basic structural element. Usually an ```article``` would be self-contained and not necessarily within the flow of the document.
* span: another common element; unlike the ```div``` element, ```span``` elements are inline. A ```div``` will be separated onto its own line, whereas ```span``` elements continue one after another.
* aside: a basic structural element. Usually this would define some kind of sidebar.
* footer: a basic structural element. Usually defines a footer in your document.

## HTML - tables.html

Continuing on, we'll look at how to build tables in HTML.

```bash
edit staticpages/tables.html
```

Tables use a few elements to define the parts of the table.

```html
<section>
    <h1>First Table</h2>
    <table>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
        <tr>
            <td>This is a plain old cell.</td>
            <td>This is a 2nd cell.</td>
            <td>This is one more cell.</td>
        </tr>
        <tr>
            <td>Cell</td>
            <td>Cell</td>
            <td>Cell</td>
        </tr>
        <tr>
            <td>One</td>
            <td>more</td>
            <td>row</td>
        </tr>
    </table>
</section>
<section>
    <h1>Second Table</h2>
    <table>
        <tr>
            <td>No header in this one.</td>
            <td>We're going to use it to demo rowspan and colspan.</td>
            <td>They'll be in the following rows.</td>
            <td>Look below.</td>
        </tr>
        <tr>
            <td colspan="3">This takes up 3 columns.</td>
            <td>We only need 2 TDs here.</td>
        </tr>
        <tr>
            <td>Another cell.</td>
            <td rowspan="3">This takes up 3 rows.</td>
            <td colspan="2">This takes up 2 columns.</td>
        </tr>
        <tr>
            <td>We only need</td>
            <td>3 cells in this row</td>
            <td>because of the rowspan.</td>
        </tr>
        <tr>
            <td>Same thing</td>
            <td>applies in this</td>
            <td>row.</td>
        </tr>
    </table>
</section>
```

The common elements you'll see when building tables are:

* table: the main element that groups all cells together into a single table.
* tr: table row; defines a new row in the table.
* th: table header; identifies the header for a column of cells in the table.
* td: table data; represents a single cell in the table.
  * The ```colspan``` attribute allows a cell to span multiple columns, beyond its normal bounds.
  * The ```rowspan``` attribute allows a cell to make up multiple rows.

## HTML - forms.html

Forms can get a bit more complex; we'll continue to use these throughout the term.

```bash
edit staticpages/forms.html
```

For forms, it's probably best to take a look at the content in your browser to
see how differnt form elements behave. Most form elements are defined using the
```input``` element with different types. Some, like ```select``` and 
```textarea``` have their own specific elements.

```html
<section>
    <h1>Form Elements</h1>
    Form elements typically will have a <em>name</em> or <em>id</em> attribute,
    and they all support the <em>disabled</em> attribute.
    <form>
        <section>
            <h2>Textareas</h2>
            Common attributes:
            <ul>
                <li>cols: how many character columns should be in this texatarea</li>
                <li>readonly: set to "readonly" to make the textarea read-only</li>
                <li>rows: how many character rows should be in this textarea</li>
            </ul>
            <br>
            This textarea has 30 columns and 8 rows.
            <br>
            <textarea cols="30" rows="8">Text inside the textarea element.</textarea>
        </section>
        <section>
            <h2>Select Fields</h2>
            Common attributes:
            <ul>
                <li>multiple: set to "multiple" to allow multiple selections</li>
                <li>size: how many values are displayed in the select box</li>
            </ul>
            <br>
            This select box is plain.
            <br>
            <select>
                <option>A</option>
                <option>B</option>
                <option>C</option>
            </select>
            <br><br>
            This select box has size = 3 and multiple = multiple.
            <br>
            <select size="3" multiple="multiple">
                <option>Option 1</option>
                <option>Option 2</option>
                <option>Option 3</option>
                <option>Option 4</option>
                <option>Option 5</option>
                <option>Option 6</option>
            </select>
        </section>
        <section>
            <h2>Button</h2>
            input type="button"<br>
            Buttons probably should have a value.    We usually connect them to JavaScript.
            <br>
            <input type="button" value="My Button Value">
        </section>
        <section>
            <h2>Checkbox</h2>
            input type="checkbox"<br>
            Checkboxes are pretty straightforward.<br>
            <input type="checkbox">A checkbox<br>
            <input type="checkbox">Another checkbox<br>
            <input type="checkbox">Still 1 more checkbox<br>
        </section>
        <section>
            <h2>Color</h2>
            <input type="color"<br>
            You can set the default color with the "value" attribute.<br>
            <input type="color" value="#f981f3">
        </section>
        <section>
            <h2>Date</h2>
            <input type="date"<br>
            Dates are pretty straightforward - usually a special control for entering a date.<br>
            <input type="date">
        </section>
        <section>
            <h2>Email</h2>
            input type="email"<br>
            Validates that this is a properly formatted email address.<br>
            <input type="email" error="abcd">
        </section>
        <section>
            <h2>Number</h2>
            input type="number"<br>
            Validates that this is a number.<br>
            <input type="number">
        </section>
        <section>
            <h2>Password</h2>
            input type="password"<br>
            Masks the input.<br>
            <input type="password">
        </section>
        <section>
            <h2>Radio</h2>
            input type="radio"<br>
            Radio buttons with the same name are automatically grouped.<br>
            Usually different radio buttons have different "value" attributes.<br>
            <input name="radio1" type="radio">First
            <input name="radio1" type="radio">Second
            <input name="radio1" type="radio">Third
        </section>
        <section>
            <h2>Range</h2>
            input type="range"<br>
            You may see these used with max, min, step, and value attributes.<br>
            This one has max="250", min="0", step="50", and value="200".<br>
            <input type="range" max="250" min="0" step="50" value="200">
        </section>
        <section>
            <h2>Text</h2>
            input type="text"<br>
            The most basic input.<br>
            <input type="text">
        </section>
        <section>
            <h2>Time</h2>
            input type="time"<br>
            Special input control for entering time.<br>
            <input type="time">
        </section>
        <section>
            <h2>URL</h2>
            input type="url"<br>
            Validates that this is a URL.<br>
            <input type="url">
        </section>
    </form>
</section>
```