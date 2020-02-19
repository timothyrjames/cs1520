
function createXmlHttp() {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    if (!(xmlhttp)) {
        alert("Your browser does not support AJAX!");
    }
    return xmlhttp;
}

// this function converts a simple key-value object to a parameter string.
function objectToParameters(obj) {
    var text = '';
    for (var i in obj) {
        // encodeURIComponent is a built-in function that escapes to URL-safe values
        text += encodeURIComponent(i) + '=' + encodeURIComponent(obj[i]) + '&';
    }
    return text;
}


function postParameters(xmlHttp, target, parameters) {
    if (xmlHttp) {
        xmlHttp.open("POST", target, true); // XMLHttpRequest.open(method, url, async)
        var contentType = "application/x-www-form-urlencoded";
        xmlHttp.setRequestHeader("Content-type", contentType);
        xmlHttp.send(parameters);
    }
}

function sendJsonRequest(parameterObject, targetUrl, callbackFunction) {
    var xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            console.log(xmlHttp.responseText);
            var myObject = JSON.parse(xmlHttp.responseText);
            callbackFunction(myObject, targetUrl, parameterObject);
        }
    }
    console.log(targetUrl);
    console.log(parameterObject);
    postParameters(xmlHttp, targetUrl, objectToParameters(parameterObject));
}

// This can load data from the server using a simple GET request.
function getData(targetUrl, callbackFunction) {
    let xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            // note that you can check xmlHttp.status here for the HTTP response code
            try {
                let myObject = JSON.parse(xmlHttp.responseText);
                callbackFunction(myObject, targetUrl);
            } catch (exc) {
                console.log("There was a problem at the server.");
            }
        }
    }
    xmlHttp.open("GET", targetUrl, true);
    xmlHttp.send();
}

function showError(msg) {
    let errorAreaDiv = document.getElementById('ErrorArea');
    errorAreaDiv.display = 'block';
    errorAreaDiv.innerHTML = msg;
}

function hideError() {
    let errorAreaDiv = document.getElementById('ErrorArea');
    errorAreaDiv.display = 'none';
}

// we use this function to send a POST request to the server for updating / 
// creating new list items.
function saveItem(id) {
    let params = {};
    if (id) {
        params['id'] = id;
        params['quantity'] = document.getElementById("edit_item_quantity").value;
        params['title'] = document.getElementById("edit_item_title").value;
    } else {
        // if no ID is supplied this is creating a new item.
        params['quantity'] = document.getElementById("item_quantity").value;
        params['title'] = document.getElementById("item_title").value;
    }
    sendJsonRequest(params, '/save-item', itemSaved);
}

// use this to clear the values in the "add item" form
function clearItemForm() {
    document.getElementById("item_quantity").value = '';
    document.getElementById("item_title").value = '';
}

// this is called in response to saving list item data.
function itemSaved(result, targetUrl, params) {
    if (result && result.ok) {
        console.log("Saved item.");
        clearItemForm();
        loadItems();
    } else {
        console.log("Received error: " + result.error);
        showError(result.error);
    }
}

// when the list items are loaded from the server, we use this function to
// render them on the page
function displayList(result, targetUrl) {
    if (result && result.length) {
        let text = '<ul>';
        for (var i = 0; i < result.length; i++) {
        text += '<li id="li_' + result[i].id + '">';
        text += '<button onclick="editItem(\'' + result[i].id + '\');">edit</button> ';
        text += '<button onclick="deleteItem(\'' + result[i].id + '\');">x</button> ';
        text += result[i].quantity + ') ' + result[i].title;
        text += '</li>';
        }
        text += '</ul>';
        console.log("updating DisplayArea: " + text);
        document.getElementById("DisplayArea").innerHTML = text;
    } else {
        document.getElementById("DisplayArea").innerHTML = 'No list items.';
    }
}

// we use this to trigger a load of the data from the server for this list item
// so we can be sure to edit the latest data.
function editItem(id) {
    getData('/get-item/' + id, itemLoaded);
}

// when the item is loaded, we render an edit form in the list.
function itemLoaded(result, targetUrl) {
    let text = '';
    text += '<input type="number" id="edit_item_quantity" value="' + result.quantity + '"> ) ';
    text += '<input type="text" id="edit_item_title" value="' + result.title + '"> ';
    text += '<button onclick="saveItem(' + result.id + ');">save</button> ';
    text += '<button onclick="loadItems();">cancel</button> ';
    document.getElementById('li_' + result.id).innerHTML = text;
}

function deleteItem(id) {
    if (confirm("Are you sure you want to delete?")) {
        let params = {"id": id};
        sendJsonRequest(params, '/delete-item', itemDeleted);
    }
}

// when we delete an item, we use this to reload the list of items.
function itemDeleted(result, targetUrl, params) {
    if (result && result.ok) {
        console.log("Deleted item.");
        loadItems();
    } else {
        console.log("Received error: " + result.error);
        showError(result.error);
    }
}

function loadItems() {
    getData('/load-sl-items', displayList);
}