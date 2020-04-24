# define a function which prints a variable holding value (3+9):
def example():
    print('this code is an example of how to write functions')
    z = 3 + 9
    print(z)

# define a function taking two parameters, with addition of them both within
# the scope of the function along with display of the subsequent result:
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is:', num1)
    print(answer)

# call first function
example()

# call second function with two integer values as parameters:
simple_addition(5,3)

# call second function with parameters defined selectively:
simple_addition(num2=3,num1=5)

# additionally, the second function can also be used to concatenate strings:
simple_addition("hi","hey")
