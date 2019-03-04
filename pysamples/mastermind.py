#### NOTE: This was written for Python 2, it won't work directly in Python 3.

# we'll use random to generate random numbers.  
# the "import" statement allows us to use other modules in Python.
import random

# even though we don't have *constants* - by convention these can be used as such
TRIES = 12
CODE_SIZE = 4
MAX_VALUE = 6

# this function will simply give us back a random integer between 1 and max
# note that we don't have to identify the type, but it *is* implicit.
def get_random_int(max):
  return int(random.random() * max) + 1


# we can declare classes in Python like this:
class Code():
  # This is the code for a constructor in Python.
  # note that "self" identifies this as method (instead of a class function).
  # "self" is comparable to Java's "this" keyword.
  def __init__(self):
    # list() allows us to create a dynamic array-like structure.
    self.code = list()
    
    # we can use for loops and the range(start, end) function to operate like a Java for loop.
    for i in range(0, CODE_SIZE):
      # we use this to add additional values to our object's code.
      # Note that we'll compare strings to strings, so we convert the output of the 
      # get_random_int function to a string here.
      self.code.append(str(get_random_int(MAX_VALUE)))
      
  # we'll define another method to check the code.
  def check_code(self, guess):
  
    # we will declare a few integers...
    correct = 0
    correct_position = 0
    
    # Let's check to make sure the guess is the proper length
    if len(guess) == len(self.code):
    
      # we'll check to see if our values are in the right position
      for i in range(0, len(guess)):
        if guess[i] == self.code[i]:
          correct_position += 1
      
      # we'll create a copy of self.code so that we can modify it here.
      code_copy = list(self.code)
      for i in range(0, len(guess)):
        # we can use the count(value) function to determine if our object's code contains 
        # each value from the guess.
        if code_copy.count(guess[i]) > 0:
          correct += 1
          # before, we made a copy of our list, so we can remove values safely here.
          code_copy.remove(guess[i])
    
    # we return a tuple here - it's just an ordered collection of values.
    return (correct, correct_position)
          
  # In this method we'll just iterate over the guess and see if it matches our object's 
  # code value.
  def correct_code(self, guess):
    correct = False
    if len(guess) == len(self.code):
      correct = True
      num = 0
      for i in guess:
        if not (i == self.code[num]):
          correct = False
          break
        num += 1
    return correct
      

# now that we've defined our class and our values, we can begin the real program.
# we start by creating a new code and initializing our basic variables.
code = Code()
attempts = 0
guess = []

# We'll tell the user the basic directions here.
print "\nThe code contains " + str(CODE_SIZE) + " values from 1 to " + str(MAX_VALUE) + "."
print "Enter your guess as number separated by commas, as: 1, 2, 3, 4\n"

# Then we'll iterator for TRIES attempts, or until the user guesses correctly.
while attempts < TRIES and not code.correct_code(guess):
  guess_values = []
  # we use this while loop to make sure the user gives us a valid guess.
  while not len(guess_values) == CODE_SIZE:
    raw_guess = raw_input("> Attempt " + str(attempts + 1) + " - enter your guess:")
    # this just separates the user's guess into an actual list
    guess_values = raw_guess.split(",")

  guess = guess_values
  
  # we'll use this for-loop to strip whitespace from the user's input.
  for i in range(0, len(guess)):
    guess[i] = guess[i].strip()

  # we'll check the user's submission and tell them the result.
  (correct, correct_position) = code.check_code(guess)
  print ">>> You got " + str(correct) + " correct."
  print ">>> " + str(correct_position) + " are in the correct position."
  
  # increment the number of attempts.
  attempts += 1
  
# Let the user know the result.
print "The secret code was:" 
print code.code
if code.correct_code(guess):
  print "YOU WIN!!!! :-D :-D yay!"
else:
  print "You lose >:O :("
