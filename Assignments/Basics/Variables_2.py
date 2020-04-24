# variables in python:
counter = 100
miles = 1000.0
name = 'Mousmita'
# they are not constants since their value can be changed. 
# for eg: redeclare counter with some other value subsequently and 
# its value will be changed

print(counter)
print(miles)
print(name)

# multiple assignments :
a=b=c=1
# Here, an integer object is created with the value 1,
# and all three variables are assigned to the same memory location.

# here ordered assignment takes place, where variables in order
# are assigned to  their values in the same sequence orderly fashion
# a gets assigned the first value after =
# b gets assigned the second values after =
# c gets assigned the third value after = 
# values being comma seperated.
a,b,c=1,'mousmita','sarma'
print(a)
print(b)
print(c)

#delete variable
del a
# if we were to write print(a) here, 
# it will produce an error declaring that 'a' is not defined
