# JavaScript Samples

## JavaScript Samples

This tutorial explains each of the JavaScript samples. Each step will explain 
one area of the JavaScript language.

## Comments

```JavaScript
// Comments in JavaScript are just like in Java.
// You can use 2 forward slashes for a one line comment.
```

```JavaScript
/*
 * OR YOU CAN USE a forward slash followed by an asterisk to create a
 * multiline comment - just close it with an asterisk followed by a
 * forward slash, like this:
 */
```

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

## Varibles

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

## Types

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

## Arrays

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
