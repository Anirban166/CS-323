# Dictionaries are a data structure in Python that are very similar to 
# associative arrays. They are non-ordered and contain "keys" and "values."
# Each key is unique and the values can be just about anything, 
# but usually they are string, int, or float, or a list of these things.


# Create an empty dictionary:
dict = {}
# assign key a key and a value of both string type:
dict['one'] = "This is value for one"
# assign yet another key-value pair:
dict['2'] = "This is value for 2"
# create another dictionary following same format:
tinydict = {'name':'mousmita', 'course':'Phd', 'year':'2014', 'dept':'ECE'}

# print first dictionary:
print (dict)
# print dictionary element with key as 'one': 
print (dict["one"])
# print dictionary element with key as '2':
print (dict['2'])
# print the values for dictionary dict:
print (dict.values())
# print the keys for dictionary dict:
print (dict.keys())
# print the second dictionary:
print (tinydict)
# print the keys for the dictionary tinydict:
print (tinydict.keys())
# print the values for the dictionary tinydict:
print (tinydict.values())


# Add two more key-value pairs to tinydict:
tinydict['field']= 'Speech'
tinydict['second_field']='DNN'
# print that to see the new additions:
print (tinydict)
