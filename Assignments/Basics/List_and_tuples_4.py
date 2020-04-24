# create two lists with comma seperated values inside [ ] initializer:
biglist = [ "mou", "liza", "sona", '22', "21", "16" ]
tinylist = [ "m", "s" ]

# print the first list:
print (biglist)
# print the first element in the first list:
print (biglist[0])
# print the elements after the 2nd element in the first list:
print (biglist[2:])
# print the element of second list at 1th index: (second element)
print (tinylist[1])
# print the second list:
print (tinylist)
# append elements of first and second list and print them:
print (biglist + tinylist)

# create yet another list, containing non-homogeneous types of elements:
list = ["physics", "chemistry", 1997, 2001]
# print that:
print (list)
# print value at the 2nd index:
print ("Value available at index 2:")
print (list[2])
# change the value:
list[2] = 2003
# re-print it to see the change:
print ("New value available at index 2:")
print (list[2])
# delete element at 1st index (2nd one - string chemistry) from our list:
del list[1]
# print the list to see the change:
print ("after deleting value at index 1 the list looks like this:")
print (list)

# create two tuples:
bigtup = ("mousmita", "sona", 22, 28)
tinytup = (22, 28)
# print them:
print (bigtup)
print (tinytup)
# print elements of first tuple after the 1st element:
print (bigtup[1:])
# print 1st index element (2nd one) of second tuple:
print (tinytup[1])
# append the tuples and print their combined contents:
print (bigtup + tinytup)

# deleting elements of tuple is not permitted
