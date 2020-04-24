# initialize a variable to hold text to be written to a file:
text = 'Sample Text to Save\nNew line!'

# open a file (in current directory) by the name specified in first 
# parameter of open(), and mode specified in the second parameter.
# w is for write mode:
saveFile = open('exampleFile.txt','w')

# write to the file using write():
saveFile.write(text)

# Close the file using close():
saveFile.close()
