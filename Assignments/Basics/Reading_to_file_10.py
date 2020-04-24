# read from our file used above using read() function, store the data
# in a variable and print it:
readMe = open('exampleFile.txt','r').read()
print(readMe)

# Using readlines() instead of read() will store the data of the file
# in a python list, as evident from the output of printing that: (returns a list)
readMe = open('exampleFile.txt','r').readlines()
print(readMe)
