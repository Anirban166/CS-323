# print a string written inside " ":
print("Hello Python")

# display the statement below after 2 newlines (given by \n escape character)
# and take an input: (wait further execution until an input is provided)
input("\n\nPress the enter key to exit.")
# Starting from python 3.0, raw_input() was renamed to input(),
# so am using the later instead, since the former became invalid.

# Import the sys library, which provides access to some variables used
# or maintained by the interpreter:
import sys; 

# declare a variable holding a string:
x='foo'; 
# print that variable followed by a newline using stdout.write() function
# from sys library:
sys.stdout.write(x + '\n');
