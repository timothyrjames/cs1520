# Python Samples

## Introduction

This tutorial introduces basic Python language concepts.  

To run this example inside the Cloud Shell, enter the following command:

```bash
teachme py_samples.md
```

## Hello World

Python uses print statements to easily output content to the user.

```Python
print('What a brave new world that has such things in it.')

print(2 * 2 - 1 / 20 + 11 / 4 - 3)
```

Try it yourself:

```bash
python3 helloworld.py
```

## Comments

Single line comments use the octothorpe:

```Python
# Most comments in Python start w/ an octothorpe (also known as the pound sign)
```

Multi line comments use 3 single quotes or double quotes:
```Python
''' Multi-line comments in Python 
    can be created with 3 single quotes '''

""" 
  Three
  double
  quotes
  is
  also
  ok
"""
```

# Operators

The file operators.py contains execution of basic mathematic operations, which
are similar to Java (except the integer division operator, //).

Take a look at the file operators.py, which shows these operations.

```Python
print(3 + 3)   # Addition
print(9 - 4)   # Subtraction
print(7 * 6)   # Multiplication
print(9 / 4)   # Floating point division
print(9 // 4)  # Integer division
```

Try it yourself:
```bash
python3 operators.py
```

# Boolean Operators

Python supports boolean operators similar to Java. 

```Python
print(3 > 5)                      # False
print(12 / 2 == 6)                # True
print(12 / 3 != 4)                # False
print(7 <= 3)                     # False
```

Note that instead of || or &&, Python uses "and" and "or".

```Python
print(4 == 2 * 2 and 2 == 3 / 2)  # False
```



Another difference from Java: capital letters for "True" and "False".

```Python
print(False or True)              # True
print(True and True)              # True
```

Try it yourself:

```bash
python3 booleanoperators.py
```

# Strings

Strings in Python can be delimited by single or double quotes.

Python supports "slices" - unlike Java, you can treat strings like arrays and
access individual characters or substrings as if they're parts of arrays.

You can even use negative numbers to access values starting from the end of the
string, or omit values in the slice to start at the beginning or continue to
the end.

```Python
s = 'abcdefghijklmnopqrstuvwxyz'
print(len(s))  # 26
print(s[12])   # m
print(s[-1])   # z
print(s[2:4])  # cd
print(s[13:])  # nopqrstuvwxyz
print(s[:8])   # abcdefgh
print(s[-3:])  # xyz
print(s[:-4])  # abcdefghijklmnopqrstuv
```

Try it yourself:

```bash
python3 strings.py
```

# Variables

Variables in Python aren't declared with types. While types are not declared
as part of the variable, Python _is_ pretty particular about types.  For example,
numbers must be explicitly converted to strings with the str() function.

```Python
num = 4
word = 'cats'
other_num = 3.2

sentence = str(num) + ' ' + word

print(sentence)
```

Try it yourself:

```bash
python3 variables.py
```

# Data Types

Python supports some basic data types; you can use the type function to
retrieve the type.

```Python
print(type(True))
print(type(3))
print(type(98.6))
print(type('A string'))
print(type(None))
```

This allows you to use the type literals.  For example:

```Python
print(type(True) is bool)
print(type(3) is int)
print(type(98.6) is float)
print(type('A string') is str)
```

Try it yourself.

```bash
python3 types.py
```

# If statements

In Python, we typically see if statements _without_ parentheses. Note that 
they can be easily nested.

```Python3
x = 10
y = 13

num = int(input('Enter a number.'))

if num > 1000:
    print('That\'s a really big number!.')
    if num > 10000:
        print('That\'s a really really big number!')

num = int(input('Enter another number.'))
```

You can see below that unlike Java, where we would use "else if" - Python has a
keyword "elif" that can be used for else-if continuation of conditionals. Else
works just the same as Java.

```Python3
if num < 0:
    print('%s is negative.' % num)
elif num > 0:
    print('%s is positive.' % num)
else:
    print('%s is zero.' % num)

```

Try it yourself:

```bash
python3 if_statements.py
```

# While Loops

While loops are pretty similar to Java, but again, we don't typically use
parentheses.

```Python3
i = 0
while i < 10:
    print(i)
    i += 1      # note that Python doesn't have a ++ operator

while i >= 0:
    print(i)
    if i > 2:
        i /= 2
    else:
        i -= 2

```

Try it yourself:

```bash
python3 while_loops.py
```


# For Loops

In Python, we don't have the typical for (int i = 0; i < X; i++) style of loop.

Instead, we often use loops for iteration - like the Java for-each loop, or we
use loops in conjunction with a "range" function.

```Python
# range(10) returns 0..9, one by one similar to a Java Iterator
for i in range(10):
    print(i * 10)

# count from 50 up to 100 (noninclusive) by 5
for i in range(50, 100, 5):
    print(i)

# print every character in the string 'words' as upper case
for letter in 'words':
    print(letter.upper())

```

Try it yourself:

```bash
python3 for_loops.py
```
  

# Lists

Python does not have true arrays; it uses lists, which behave like ArrayList 
objects in Java.

In Python lists are commonly declared directly as literals, as "names" is 
declared below.

```Python3
names = ["Kanye", "Eminem", "Jay-Z"]
print(names)

my_list = list()
my_list.append(5)
my_list.append(3.2)
my_list.append(True)
my_list.append('something')

print(my_list)              # lists can contain mixtures of types

num_list = []               # this is more common than list()

for i in range(10):
    num_list.append(i * 100)

```

You can also use slices with lists:

```Python
print(num_list)
print(num_list[3:5])        # just like strings, slices can be used
print(num_list[3:])
print(num_list[:3])
print(num_list[-2:])
print(num_list[:-2])
```

Try it yourself:

```bash
python3 listst.py
```

# Dictionaries

Dictionaries are associative arrays that operate like HashMap objects in Java.

You can reference keys directly, just like arrays in Java.

```Python3
states = {
    "NY": "Newyork",
    "NJ": "New Jersey",
    "IA": "Iowa",
    "PA": "Pennsylvania",
}

print(states)

states["NY"] = "New York"
print(states)

states["CT"] = "Connecticut"
print(states)

print("NY" in states)
print("New York" in states)

for state_code in states:
    print(state_code + ": " + states[state_code])

```

Note that you could also use the following iteration pattern to get keys and
values:

```Python
for state_code, state in states.items():
    print(state_code + ": " + state)

```

Try it yourself:

```bash
python3 dictionaries.py
```

# Functions

Python functions are declared with the def keyword.

```Python
def sum(a, b):
  return a + b

print(sum(4, 5))
```

We call functions in Python exactly like most languages - just use their name 
and supply parameters.  Note one of the interesting capabilities in Python - 
because the + operator works as concatenation and addition, we can use the 
sum function on both str types and int types (as well as float types).

```Python
print(sum('this is ', 'a sentence'))
```

Python allows us to supply default values to functions; Python functions can't
be overloaded, but this defaulting allows us to provide similar capability in 
our functions.

```Python
def product(a, b, c=1):
  return a * b * c

print(product(4, 5))
print(product(2, 3, 4))
```

Note that you can also name parameters when you call a function; this allows
additional flexibility in parameter ordering.

```Python
sum(b='This', a='That')
```

Try it yourself:

```bash
python3 functions.py
```

# Classes and Objects

Classes in Python are declared with the class keyword; by default they should
extend object.

__init__ is a special Python method that is used to initialize properties for
a class. It's often called "dunder init" (dunder, for double underscore).  It
shouldn't return a value and should only be used to set up the class - similar
to a constructor.

Note that all Python methods start with a "self" parameter - this is analogous
to "this" in Java, but is explicitly required.

```Python
class Pet(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
```

There are other special ("dunder") Python methods, like __str__, which is used
to convert the object to a string.

```Python
class Pet(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return self.name + ' is ' + str(self.age)

  def get_name(self):
    return self.name
```

We build objects just by calling them by name.

```Python
pets = [
  Pet('Fido', 4),
  Pet('Spot', 7),
  Pet('Bubbles', 1),
]
```

Because we have a __str__ method, we can print the object directly.
```Python
print(pets[0])
```

Try running it yourself:

```bash
python3 classes.py
```