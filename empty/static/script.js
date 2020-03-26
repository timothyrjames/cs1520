/**
 * Show the errors from the server.
 */
function showErrors(errors) {
    let text = '';
    for (var i = 0; i < errors.length; i++) {
        text += '<div class="Error">';
        text += errors[i];
        text += '</div>';
    }
    updateHtml('ErrorArea', text);
}


/**
 * Utility function to safely update HTML for any element.
 */
function updateHtml(id, text) {
    let e = document.getElementById(id);
    if (e) {
        e.innerHTML = text;
    } else {
        console.log('Element ' + id + ' does not exist.');
    }
}


/**
 * Utility function for retrieving an input field value.
 */
function getFormValue(id) {
    return document.getElementById(id).value;
}


/**
 * Utility function for setting a form value.
 */
function setFormValue(id, value) {
    document.getElementById(id).value = value;
}


/**
 * Utility function for creating an XML Http request object in a multi-browser
 * compatible manner.
 */
function createXmlHttp() {
    let xmlhttp;
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


/**
 * Converts an object to name-value pairs for a URL or POST submission.
 */
function objectToParameters(obj) {
    let text = '';
    for (var i in obj) {
        // encodeURIComponent is a built-in function that escapes to URL-safe values
        text += encodeURIComponent(i) + '=' + encodeURIComponent(obj[i]) + '&';
    }
    return text;
}


/**
 * Send parameters using an AJAX POST request.
 */
function postParameters(xmlHttp, target, parameters) {
    if (xmlHttp) {
        xmlHttp.open("POST", target, true); // XMLHttpRequest.open(method, url, async)
        let contentType = "application/x-www-form-urlencoded";
        xmlHttp.setRequestHeader("Content-type", contentType);
        xmlHttp.send(parameters);
    }
}


/**
 * Create an AJAX request based on the parameter object, target URL, and call
 * the specific callback function on response.
 */
function sendJsonPost(parameterObject, targetUrl, callbackFunction) {
    let xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            console.log(xmlHttp.responseText);
            try {
                let myObject = JSON.parse(xmlHttp.responseText);
                showErrors(myObject.errors);
                callbackFunction(myObject, targetUrl, parameterObject);
            } catch (exc) {
                console.log("There was a problem receiving the response from the server.");
                console.log(exc);
            }
        }
    }
    console.log(targetUrl);
    console.log(parameterObject);
    postParameters(xmlHttp, targetUrl, objectToParameters(parameterObject));
}


/**
 * Create an AJAX request based on the target URL and call the specific
 * callback function on response. This loads data from the server using a 
 * simple GET request.
 */
function getJsonData(targetUrl, callbackFunction) {
    let xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            // note that you can check xmlHttp.status here for the HTTP response code
            try {
                let myObject = JSON.parse(xmlHttp.responseText);
                showErrors(myObject);
                callbackFunction(myObject, targetUrl);
            } catch (exc) {
                console.log("There was a problem receiving a response from the server.");
                console.log(exc);
            }
        }
    }
    xmlHttp.open("GET", targetUrl, true);
    xmlHttp.send();
}
