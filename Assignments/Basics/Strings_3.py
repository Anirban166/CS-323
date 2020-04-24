# initialize a string:
str = "mousmita sarma"
# print the string:
print (str)
# print the first character of the string, or the one at 0th index:
print (str[0])
# print third character of string, at 2th index: (indices start from 0,
# following c-style arrays or a c++ std::array, unlike varrays in oracle,
# which start from 1)
print (str[2])
# print characters after the 4th character in str: (or after 4-1= 3rd index)
print (str[4:])
# print characters falling between the 2nd and 9th character in str:
# equivalent to a combination of str[2:] and str[:9]
print (str[2:9])
# print string twice: (without seperating character)
print (str * 2)
# append string "sarma" after string str:
print (str + " sarma")

# declare a variable holding a string:
var1 = "Hello Mousmita"
# print that string:
print (var1)
# print the below in order, with [:6] extracting the first 6 characters from var1"
print ("Updating string :-", var1[:6] + "sarma")

# Use the string formatting operator to assign values of different types accordingly: (a string and an int)
print ("My name is %s and weight is %d" % ("Mou",49))

# Writing multiple lines using triple quotes, with a \t for tab indentation and \n for newline, like typical escape characters.
# There is an automatic newline character generation following the text being written in newlines within triple quotes.
para_string = """ This is an example of triple qoutes, which
helps to write multiple lines, tab \t and 
also newlines exclusively given or wrote like this \n is also dispalyed"""
print (para_string)
