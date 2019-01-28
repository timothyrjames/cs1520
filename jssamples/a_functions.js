// Comments in JavaScript are just like in Java
// You can use 2 forward slashes for a one line comment

/*
 * OR YOU CAN USE a forward slash followed by an asterisk to create a
 * multiline comment - just close it with an asterisk followed by a
 * forward slash, like this:
 */

// There are JsDoc comments, like javadoc, but they aren't standard :(


// In JavaScript, we use the "function" keyword to declare a function.
function firstFunction() {
  console.log("Functions don't have to return values.");
}

function secondFunction() {
  console.log("Functions *can* return values, though.");
  return 1;
}

function thirdFunction(a, b, c) {
  console.log("They can also take parameters.");
  return a + b + c;
}

function fourthFunction() {
  console.log("There is also an arguments array that can be used for ");
  console.log("variable numbers of parameters.");
  return arguments.length;
}

