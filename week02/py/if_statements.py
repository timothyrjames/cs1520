
x = 10
y = 13

num = int(input('Enter a number.'))

if num > 1000:
    print('That\'s a really big number!.')
    if num > 10000:
        print('That\'s a really really big number!')

num = int(input('Enter another number.'))

# If statements in Python don't use parentheses.
if num < 0:
    print('%s is negative.' % num)
elif num > 0:
    print('%s is positive.' % num)
else:
    print('%s is zero.' % num)
