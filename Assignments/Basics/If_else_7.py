# initialize two variables:
x = 5
y = 10
# apply comparison condition using if-else statements:
if x > y:
    print('x is greater than y')
else:
    print('y is greater than x')

# more variables:
x = 5
y = 10
z = 22

# compare x,y in similar fashion, but use an elif to check for x less than z condition as well:
if x > y:
    print('x is greater than y')
# "elif" statement allows to check multiple statements for true condition:
elif x < z:
    print('x is less than z')
else:
    print('if and elif never ran...')

# if x was given a value greater than y, say 11, then it would print
# x is greater than y and not go the elif or else statements.    

