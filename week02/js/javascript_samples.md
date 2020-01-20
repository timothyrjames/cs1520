# JavaScript Tutorial

## JavaScript Tutorial - Samples Walkthrough

This tutorial explains each of the JavaScript samples. Each step will explain 
one area of the JavaScript language.

You can view the execution of the functions described here by going to
[this link](http://cs1520a.appspot.com/javascript_samples.html) in your
browser.

To run this tutorial, enter the following command inside the Cloud Shell:

```bash
teachme javascript_samples.md
```

## Comments

Comments in JavaScript are remarkably similar to Java. Single line comments are
quite common.

```JavaScript
// Comments in JavaScript are just like in Java.
// You can use 2 forward slashes for a one line comment.
```

Multi-line comments are also common in JavaScript.

```JavaScript
/*
 * OR YOU CAN USE a forward slash followed by an asterisk to create a
 * multiline comment - just close it with an asterisk followed by a
 * forward slash, like this:
 */
```

[JsDoc](https://jsdoc.app/about-getting-started.html) is not standard but is 
reasonably popular.

```JavaScript
// There are JsDoc comments, like javadoc, but they aren't standard :(
```

## Functions

In JavaScript, we use the "function" keyword to declare a function.

```JavaScript
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
```

There are alternatives; arrow functions are becoming quite common in
JavaScript.

```JavaScript
(a, b) => {
    return a + b;
}
```

Anonymous functions are also becoming more popular for certain operations.

```JavaScript
function(x) {
  return x + 1;
});
```

## Operators

Operators in JavaScript are similar to Java.

```JavaScript
function operators() {
  console.log(3 + 3);
  console.log(9 - 4);
  console.log(7 * 6);
  console.log(9 / 4);
  console.log(Math.floor(9 / 4)); 
}
```

## Boolean Operators

Boolean operators in JavaScript are also very similar to Java.

```JavaScript
function booleanOperators() {
  console.log(3 > 5);
  console.log(3 > 5);
  console.log(12 / 2 == 6);
  console.log(12 / 3 != 4);
  console.log(7 <= 3);
  console.log(4 == 2 * 2 && 2 == 3 / 2);
  console.log(false || true);
  console.log(true && true);

  // In JavaScript, there's the === operator for equivalence in value & type
  console.log(3 == '3');
  console.log(3 === '3');
  console.log(3 != '3');
  console.log(3 !== '3');
}
```

## Strings

Strings in JavaScript behave mostly similarly to Java.

```JavaScript
function strings() {

  var s = 'abcdefghijklmnopqrstuvwxyz'
  console.log(s.length);
  console.log(s.charAt(12));
  console.log(s.substring(-1));    // anything < 0 will be treated as 0
  console.log(s.substring(2, 4));
  console.log(s.substring(13));
  console.log(s.substring(0, 8));
  console.log(s.substring(-1, 3)); // again, < 0 becomes 0.
  console.log(s.substring(0, -4)); // this basically does nothing.

}
```

## Variables

Variables can be declared a few ways in JavaScript. Historically they've been
declared using the "var" keyword; more and more you will see "let" as it has
some built-in protection.

```JavaScript
function variables() {

  // in JavaScript, we use "var" to declare variables
  var num = 4;
  var word = 'cats';

  // "let" declares a variable, but with checking.  Probably better.
  let otherNum = 3.2;

  // for example, try uncommenting the following line:
  // let num = 5.0;
  
  // in JavaScript, if we don't declare a variable, it becomes global.
  sentence = num + ' ' + word;

  console.log(sentence);
}
```

You can also use the const keyword, but be careful as const (as well as let)
have only been well supported in browsers for a few years and older browsers
will not support them.

```JavaScript
const SALES_TAX_RATE = 0.7;
```

## Types

JavaScript is a weakly typed language; it will automatically try to convert
types for you (especially when combining different types) and this can lead to
some unpredictable and challenging situations. 

There is a typeof function that you can use to determine the underlying type
of data.

```JavaScript
function types() {
  
  console.log(typeof(true));
  console.log(typeof(3));
  console.log(typeof(98.6));
  console.log(typeof('A string'));
  console.log(typeof(null));

  // probably as important in JavaScript is instanceof - see Objects.
}
```

## If Statements

If statements in JavaScript work syntactically the same as Java.

```JavaScript
function ifStatements() {
  let x = 10;
  let y = 13;

  let num = prompt('Enter a number.');

  if (num > 1000) {
    console.log('That\'s a really big number!.');
    if (num > 10000) {
      console.log('That\'s a really really big number!');
    }
  }

  num = prompt('Enter another number.');

  if (num < 0) {
    console.log(num + ' is negative.');
  } else if (num > 0) {
    console.log(num + ' is positive.');
  } else {
    console.log(num + ' is zero.');
  }
}
```

## While Loops

While loops in JavaScript are syntactically the same as in Java.

```JavaScript
function whileLoops() {
  let i = 0;
  while (i < 10) {
    console.log(i);
    i++;                // JavaScript supports the ++ operator
  }

  while (i >= 0) {
    console.log(i);
    if (i > 2) {
      i /= 2;
    } else {
      i -= 2;
    }
  }
}
```

## For Loops

Basic, iterating for loops in JavaScript are syntactically the same as Java.

```JavaScript
function forLoops() {

  for (var i = 0; i < 10; i++) {
    console.log(i * 10);
  }

  // count from 50 up to 100 (noninclusive) by 5
  for (var i = 50; i < 100; i += 5) {
    console.log(i);
  }

  // print every character in the string 'words' as upper case
  for (var i = 0; i < 'words'.length; i++) {
    console.log('words'[i].toUpperCase());
  }
}
```

JavaScript does support a for-each loop; however it's been deprecated and is
of limited value in practice.  It is typically used with objects; its 
behavior can sometimes yield unexpected results.

```JavaScript
for (let i in x) {
    console.log(i);
}
```

for-of loops are supported for several years and should be mostly safe to use
in your JavaScript.  The code below will output each of the values in "x".

```JavaScript
let x = ['a', 'b', 'c'];
for (let i of x) {
    console.log(i);
}
```

## Arrays

JavaScript has arrays that are dynamic; they look like Java arrays, but you can
easily add or remove values from them.

```JavaScript
function arrays() {
  let names = ["Kanye", "Eminem", "Jay-Z"];
  console.log(names);

  let myList = new Array();
  myList.push(5);             // use "push" instead of "append"
  myList.push(3.2);
  myList.push(true);
  myList.push('something');

  console.log(myList);

  let numList = [];           // just like in Python, this is common

  for (var i = 0; i < 10; i++) {
    numList.push(i * 100);
  }

  console.log(numList);
  console.log(numList.slice(3, 5));
  console.log(numList.slice(3));
}
```

## Maps

[Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) 
are a new concept in JavaScript; they provide improvements over just using 
objects as if they were maps, but have only been supported for a few years.

```JavaScript
function maps() {
  
  // Map is a new construct in JavaScript; historically
  // people have used plain old objects.

  let states = {
    "NY": "Newyork",
    "NJ": "New Jersey",
    "IA": "Iowa",
    "PA": "Pennsylvania"
  };

  console.log(states);

  states["NY"] = "New York";
  console.log(states);

  states["CT"] = "Connecticut";
  console.log(states);

  // "in" also works in JavaScript
  console.log("NY" in states);
  console.log("New York" in states);

  // note that order here will probably be the order in which these keys
  // were defined.
  for (var stateCode in states) {
    console.log(stateCode + ": " + states[stateCode]);
  }
}
```

## Objects

The oldest and most common way to build classes in JavaScript is to use a 
function as a constructor. It's awkward but works in really old browsers.

```JavaScript
function objects() {
  function Pet(name, age) {
    this.name = name;
    this.age = age;

    this.toString = function() {
      return this.name + ' is ' + this.age;
    };
  }


  let pets = [
    new Pet('Fido', 4),
    new Pet('Spot', 7),
    new Pet('Bubbles', 1)
  ];

  console.log(pets[0].toString());
  console.log(pets[1] instanceof Object);
  console.log(pets[2] instanceof Pet);
}
```

Also common is to declare objects in JSON format.

```JavaScript
let bubbles = {
    name: 'Bubbles',
    age: 11,
    toString: function() {
        return this.name + ' is ' + this.age;
    }
}
console.log(bubbles.toString());
```

A new way to declare classes in JavaScript is to use the
[class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
keyword; however, as with let and const, this has only been supported for a few
years, so be careful as it is not universally supported in older browsers.
